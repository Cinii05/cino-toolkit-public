#!/usr/bin/env python3
"""Read-only check of local video files against extracted evidence records."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

VIDEO_SUFFIXES = {".mp4", ".mov", ".m4v", ".mkv", ".webm"}


def fingerprint(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def decode(ffmpeg: str, path: Path, timeout: int) -> tuple[bool, str]:
    try:
        result = subprocess.run(
            [ffmpeg, "-nostdin", "-hide_banner", "-loglevel", "error", "-xerror",
             "-i", str(path), "-map", "0:v:0", "-map", "0:a?", "-f", "null", "-"],
            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE, text=True, timeout=timeout, check=False,
        )
    except subprocess.TimeoutExpired:
        return False, f"Full decode exceeded {timeout} seconds"
    return result.returncode == 0, result.stderr.strip()[:500]


def inspect(item_id: str, media_dir: Path, evidence_dir: Path, ffmpeg: str, timeout: int) -> dict:
    record_path = evidence_dir / item_id / "evidence.json"
    media = [p for p in media_dir.glob(item_id + ".*") if p.suffix.lower() in VIDEO_SUFFIXES]
    issues: list[str] = []
    if not record_path.is_file():
        issues.append("NO_EVIDENCE")
        source = {}
    else:
        try:
            record = json.loads(record_path.read_text(encoding="utf-8"))
            source = record["source"]
            if not isinstance(source, dict) or not isinstance(source.get("filename"), str):
                raise ValueError("Missing source filename")
            if type(source.get("size_bytes")) is not int or source["size_bytes"] < 0:
                raise ValueError("Missing or invalid source size")
        except (OSError, ValueError, KeyError, TypeError):
            issues.append("INVALID_EVIDENCE")
            source = {}
    filename = source.get("filename")
    if filename and Path(filename).name != filename:
        issues.append("INVALID_EVIDENCE")
        filename = None
    path = media_dir / filename if filename else (media[0] if len(media) == 1 else None)
    if len(media) > 1:
        issues.append("AMBIGUOUS_MEDIA")
    if path is None or not path.is_file():
        issues.append("MISSING_MEDIA")
        return {"id": item_id, "status": "ISSUE", "issues": issues,
                "media": str(path) if path else None}
    try:
        size = path.stat().st_size
        expected_size = source.get("size_bytes")
        if expected_size is not None and (type(expected_size) is not int or size != expected_size):
            issues.append("SIZE_MISMATCH")
        expected_hash = source.get("sha256")
        if expected_hash is not None:
            if not isinstance(expected_hash, str) or fingerprint(path) != expected_hash.lower():
                issues.append("HASH_MISMATCH")
        ok, detail = decode(ffmpeg, path, timeout)
        if not ok:
            issues.append("DECODE_ERROR")
    except OSError as error:
        issues.append("READ_ERROR")
        detail = str(error)[:500]
    if issues:
        status = "ISSUE"
    elif not expected_hash:
        status = "LEGACY_NO_HASH"
    else:
        status = "OK"
    result = {"id": item_id, "status": status, "issues": issues,
              "media": str(path), "size_bytes": size,
              "identity_check": "sha256" if expected_hash else "size_only"}
    if detail:
        result["decode_detail"] = detail
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--media-dir", required=True, type=Path)
    parser.add_argument("--evidence-dir", required=True, type=Path)
    parser.add_argument("--id", action="append", dest="ids", default=[],
                        help="Index media ID to check, including IDs with no local file (repeatable)")
    parser.add_argument("--ids-file", type=Path,
                        help="Plain text file with one index media ID per line")
    parser.add_argument("--timeout", type=int, default=300, help="Decode time limit per video")
    parser.add_argument("--json", action="store_true", help="Machine-readable report on stdout")
    args = parser.parse_args()
    media_dir = args.media_dir.expanduser().resolve()
    evidence_dir = args.evidence_dir.expanduser().resolve()
    if not media_dir.is_dir() or not evidence_dir.is_dir() or args.timeout < 1:
        parser.error("Both directories must exist and timeout must be positive")
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        parser.error("ffmpeg is required for a full decode")
    ids = set(args.ids)
    if args.ids_file:
        ids.update(line.strip() for line in args.ids_file.read_text(encoding="utf-8").splitlines()
                   if line.strip() and not line.lstrip().startswith("#"))
    if not ids:
        ids.update(path.stem for path in media_dir.iterdir()
                   if path.is_file() and path.suffix.lower() in VIDEO_SUFFIXES)
        ids.update(path.parent.name for path in evidence_dir.glob("*/evidence.json"))
    if not ids or any(not item or any(char in item for char in "/\\*?[]")
                      or item in {".", ".."}
                      for item in ids):
        parser.error("No valid IDs found; use one media ID per line in --ids-file")
    results = [inspect(item_id, media_dir, evidence_dir, ffmpeg, args.timeout)
               for item_id in sorted(ids)]
    counts = {status: sum(r["status"] == status for r in results)
              for status in ("OK", "LEGACY_NO_HASH", "ISSUE")}
    if args.json:
        print(json.dumps({"counts": counts, "results": results}, indent=2))
    else:
        for row in results:
            reason = ", ".join(row["issues"]) if row["issues"] else ""
            print(f'{row["id"]}: {row["status"]}' + (f" ({reason})" if reason else ""))
        print(f'Summary: {counts["OK"]} OK, {counts["LEGACY_NO_HASH"]} legacy limited, '
              f'{counts["ISSUE"]} issues')
    return 1 if counts["ISSUE"] else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, UnicodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(2)
