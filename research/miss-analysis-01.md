# Miss analysis: practice quiz 1 (16/25, 64%)

Source: user's practice quiz. Answer options were not pasted. Correct answers are inferred from stems, then checked against official docs (see "Verification").

## Domain score vs exam weight

| Domain | Score | Exam weight | Priority |
|---|---|---|---|
| D1 Agentic architecture | 3/6 (50%) | 27% | 1 |
| D2 Tool design & MCP | 2/4 (50%) | 18% | 2 |
| D3 Claude Code config | 4/6 (67%) | 20% | 3 |
| D4 Prompt eng & structured output | 3/5 (60%) | 20% | 3 |
| D5 Context & reliability | 4/4 (100%) | 15% | skip |

## Misses

Cause codes: K = knowledge gap (a doc fact), H = heuristic gap (picked "true but not best").

| Q | Sub | Topic | Cause | Expected answer (pending verification) | Pattern |
|---|---|---|---|---|---|
| 1 | 1.2 | Agents message each other, shared tasks, long session | K | Agent teams (not subagents) | Feature map |
| 5 | 3.1 | Personal per-repo config, never committed | K | `CLAUDE.local.md` (gitignored) | Scope ladder |
| 9 | 1.5 | PreToolUse `deny` + reason | K | Tool call blocked; reason goes to Claude so it can adapt | Mechanism |
| 10 | 3.6 | CI reviews need team test rules every run | K/H | Project `CLAUDE.md` in repo | Scope ladder |
| 16 | 1.2 | Subagent cut off by overload error | K | See verification | Feature map |
| 17 | 2.3 | Router agent calls `process_refund` | H | Remove extra tools; keep only `route_ticket` | Mechanism |
| 19 | 4.2 | Invoice layouts vary; model invents values | H | Few-shot examples of varied layouts, incl. absent → null | Show, not tell |
| 22 | 4.3 | Date formats vary; must be deterministic + testable | H | Extract raw string; normalize in code | Mechanism |
| 23 | 2.3 | Must call a tool every turn | K | `tool_choice: {"type": "any"}` | Mechanism |

## Patterns

1. **Mechanism beats instruction (4-5 misses: Q9, Q17, Q22, Q23, part of Q10).**
   Trigger words: always, never, must, guarantee, deterministic, testable, every.
   Rule: pick the answer that enforces with structure (hook, code, schema, `tool_choice`, removing a tool, config file). Reject "add to the prompt" answers.
   Matches the official sample pattern "use code, not prompts, for rules that must always hold."
2. **Scope ladder (2-3 misses: Q5, Q10, Q17).**
   Ask: who needs it, and is it shared? Pick the narrowest documented place.
3. **Claude Code feature map (3 misses: Q1, Q9, Q16).**
   Doc facts about subagents vs agent teams, hook outputs, failure behavior.
4. **Show, not tell (1 miss: Q19).** When detailed instructions fail on varied inputs, add few-shot examples.

## Verification

Pending: independent agent checks each expected answer against official docs.
