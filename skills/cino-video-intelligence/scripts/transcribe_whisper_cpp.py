#!/usr/bin/env python3
"""Transcribe a local 16 kHz mono PCM WAV with an installed whisper.cpp CLI and model."""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
import wave
from pathlib import Path

TIMING = re.compile(r"^((?:\d{2}:)?\d{2}:\d{2}[.,]\d{3})\s+-->\s+((?:\d{2}:)?\d{2}:\d{2}[.,]\d{3})(?:\s+.*)?$")


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def seconds(stamp: str) -> float:
    parts = stamp.replace(",", ".").split(":")
    if len(parts) == 2:
        minutes, remaining = parts
        return int(minutes) * 60 + float(remaining)
    hours, minutes, remaining = parts
    return int(hours) * 3600 + int(minutes) * 60 + float(remaining)


def parse_vtt(path: Path, duration: float) -> list[dict]:
    contents = path.read_text(encoding="utf-8-sig")
    if not contents.startswith("WEBVTT"):
        raise RuntimeError("Transcriber produced an invalid WebVTT header.")
    segments: list[dict] = []
    for block in re.split(r"\r?\n\s*\r?\n", contents)[1:]:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines:
            continue
        match = next((TIMING.fullmatch(line) for line in lines[:2] if TIMING.fullmatch(line)), None)
        if not match:
            continue
        timing_line = next(i for i, line in enumerate(lines[:2]) if TIMING.fullmatch(line))
        start, end = seconds(match[1]), seconds(match[2])
        text = " ".join(lines[timing_line + 1:]).strip()
        if start < 0 or end <= start or end > duration + 2 or (segments and start < segments[-1]["start"]):
            raise RuntimeError("Transcriber produced out-of-range or unordered timestamps.")
        if text:
            segments.append({"start": round(start, 3), "end": round(end, 3), "text": text})
    if "-->" in contents and not segments:
        raise RuntimeError("Transcriber produced timestamps without readable speech.")
    return segments


def transcribe(
    audio: Path, destination: Path, model: Path, *, cli: str = "whisper-cli",
    language: str = "auto", timeout: int = 1800,
) -> dict:
    audio, model, destination = audio.resolve(), model.resolve(), destination.resolve()
    executable = shutil.which(cli)
    if not executable:
        raise RuntimeError(f"Local whisper.cpp executable unavailable: {cli}")
    if not model.is_file() or model.stat().st_size == 0:
        raise RuntimeError(f"Local whisper.cpp model unavailable or empty: {model}")
    if destination.exists():
        raise RuntimeError(f"Transcription destination already exists: {destination}")
    if timeout < 1 or not re.fullmatch(r"(?:auto|[a-z]{2,3})", language):
        raise RuntimeError("Timeout or language is invalid.")
    try:
        with wave.open(str(audio), "rb") as stream:
            if (stream.getframerate(), stream.getnchannels(), stream.getsampwidth()) != (16000, 1, 2):
                raise RuntimeError("Input must be a 16 kHz mono 16-bit PCM WAV.")
            duration = stream.getnframes() / 16000
            if duration <= 0:
                raise RuntimeError("Input WAV contains no audio frames.")
    except (wave.Error, OSError, EOFError) as error:
        raise RuntimeError(f"Could not read input WAV: {error}") from error

    prefix = destination.with_suffix("")
    try:
        result = subprocess.run(
            [executable, "-m", str(model), "-f", str(audio), "-ovtt", "-of", str(prefix),
             "-l", language, "-ng", "-np"],
            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, timeout=timeout, check=False,
        )
    except subprocess.TimeoutExpired as error:
        raise RuntimeError(f"Local transcription exceeded {timeout} seconds.") from error
    if result.returncode != 0 or not destination.is_file():
        detail = (result.stderr or result.stdout).strip()[:350]
        raise RuntimeError(f"Local transcription failed or produced no VTT: {detail}")
    segments = parse_vtt(destination, duration)
    return {
        "status": "generated" if segments else "empty_unverified",
        "path": destination.name,
        "engine": "whisper.cpp",
        "model_filename": model.name,
        "model_sha256": file_hash(model),
        "language_requested": language,
        "segments": segments,
        "note": (f"Automated local transcription: `{destination.name}`. Check words and timing against audio; "
                 + ("no speech was recognised, which does not prove silence." if not segments else
                    "mark doubtful words rather than silently correcting them.")),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audio", type=Path)
    parser.add_argument("--output", required=True, type=Path, help="New .vtt path")
    parser.add_argument("--model", required=True, type=Path, help="Existing local ggml model")
    parser.add_argument("--cli", default="whisper-cli", help="Trusted local whisper.cpp executable")
    parser.add_argument("--language", default="auto", help="auto or a language code such as en")
    parser.add_argument("--timeout", type=int, default=1800)
    args = parser.parse_args()
    result = transcribe(args.audio, args.output, args.model,
                        cli=args.cli, language=args.language, timeout=args.timeout)
    print(f"{result['status']}: {args.output} ({len(result['segments'])} segments)")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RuntimeError as error:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)
