/* Cino AgentOps Companion — observe-only StarNet telemetry.
 * No prompt injection. No blocking. No network. No authority changes.
 */
'use strict';

const fs = require('fs');
const path = require('path');

const CINO_SKILLS = new Set([
  'cino-context-funnel',
  'cino-source-of-truth',
  'cino-agent-router',
  'cino-repo-navigator',
  'cino-test-router',
  'cino-evidence-handoff',
  'cino-plan-before-build',
  'cino-skill-governor',
  'cino-skill-governor-approval-model',
  'tmc-ui-master'
]);

function safeName(v) {
  const s = String(v == null ? '' : v).trim();
  return /^[a-z0-9._-]{1,100}$/i.test(s) ? s : '';
}

const runs = new Map();
function stateFor(payload) {
  const id = String((payload && payload.session_id) || '');
  if (!id) return null;
  if (!runs.has(id)) runs.set(id, {
    session_id: id, agent_id: '', model: '', started_at: new Date().toISOString(),
    tools: 0, skill_activations: [], activation_order: [],
    mutation_capable_calls: [], tool_errors: 0
  });
  return runs.get(id);
}

function appendReceipt(receipt) {
  try {
    const dir = path.join(__dirname, 'data');
    fs.mkdirSync(dir, { recursive: true });
    fs.appendFileSync(path.join(dir, 'runs.jsonl'), JSON.stringify(receipt) + '\n', 'utf8');
  } catch (e) {
    console.warn('[cino-agentops] receipt write failed:', e && e.message);
  }
}

module.exports = {
  register(api) {
    api.on('on_session_start', (p) => {
      const s = stateFor(p);
      if (!s) return;
      s.agent_id = String(p.extra && p.extra.agent_id || '');
      s.model = String(p.extra && p.extra.model || '');
      console.log('[cino-agentops] session start ' + s.session_id);
    });
    api.on('post_tool_call', (p) => {
      const s = stateFor(p);
      if (!s) return;
      s.tools++;
      const tool = String(p.tool_name || '');
      const input = p.tool_input || {};
      const scope = String(p.extra && p.extra.scope || '');
      const status = String(p.extra && p.extra.status || '');
      if (status === 'error') s.tool_errors++;
      if (scope && scope !== 'read') s.mutation_capable_calls.push(tool);
      if (tool === 'skill.view') {
        const name = safeName(input.name);
        if (name && CINO_SKILLS.has(name)) {
          s.skill_activations.push(name);
          if (!s.activation_order.includes(name)) s.activation_order.push(name);
        }
      }
    });

    api.on('on_memory_write', (p) => {
      const s = stateFor(p);
      if (s) s.memory_write_observed = true;
    });

    api.on('on_session_end', (p) => {
      const s = stateFor(p);
      if (!s) return;
      s.ended_at = new Date().toISOString();
      s.reason = String(p.extra && p.extra.reason || 'unknown');
      s.completed = !!(p.extra && p.extra.completed);
      s.turns = Number(p.extra && p.extra.turns || 0);
      appendReceipt(s);
      console.log('[cino-agentops] session end ' + s.session_id +
        ' skills=' + s.activation_order.join('>') + ' tools=' + s.tools);
      runs.delete(s.session_id);
    });
  }
};
