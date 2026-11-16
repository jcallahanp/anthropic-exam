# Claude Certified Architect – Foundations (CCAR-F): Exam Facts

Main source: the official Exam Guide v1.0, effective July 2026 ([PDF][g]). It is hosted on Skilljar's content CDN and linked from the Anthropic Partner Academy. An older guide ([v0.x PDF][g0]) and the [FAQ PDF][faq] are cited where they differ.

## Format
- 60 items: multiple-choice and multiple-response. Each item says how many to select. (v0.x: single-answer only, no guessing penalty.)
- 4 scenarios drawn at random from 6: Customer Support Agent, Code Generation with Claude Code, Multi-Agent Research, Developer Productivity, Claude Code for CI, Structured Data Extraction.
- 120 minutes, proctored through Pearson VUE.
- Pass at a scaled 720 on a 100–1,000 scale (criterion-referenced). Percent correct by domain is reported but does not decide pass or fail.
- $125 fee; valid 12 months.

## Domains

| # | Domain | Weight |
|---|---|---|
| 1 | Agentic Architecture & Orchestration | 27% |
| 2 | Tool Design & MCP Integration | 18% |
| 3 | Claude Code Configuration & Workflows | 20% |
| 4 | Prompt Engineering & Structured Output | 20% |
| 5 | Context Management & Reliability | 15% |

## Skills per domain (task statements)
- **D1:** agentic loops driven by `stop_reason` (`tool_use` vs `end_turn`); coordinator–subagent hub-and-spoke; subagent context passing (Task tool, `allowedTools`, explicit context); enforcement with hooks and prerequisite gates, plus handoffs; hooks (PostToolUse, intercepting tool calls); task decomposition (prompt chaining vs dynamic); sessions (`--resume`, `fork_session`).
- **D2:** clear, distinct tool descriptions; structured MCP errors (`isError`, category, retryable); scoped tool sets and `tool_choice`; MCP server scoping (`.mcp.json` vs `~/.claude.json`, env-var expansion, resources); built-in tools (Grep, Glob, Read, Write, Edit).
- **D3:** CLAUDE.md hierarchy and `@import`; slash commands and skills (`context: fork`, `allowed-tools`, `argument-hint`); path-scoped `.claude/rules/`; plan mode vs direct execution; iterative refinement (examples, TDD, interview pattern); CI/CD (`-p`, `--output-format json`, `--json-schema`).
- **D4:** explicit criteria to cut false positives; few-shot examples; structured output through `tool_use` and JSON schema (nullable fields, enums with "other"); validation and retry loops; Message Batches API; multi-pass review and independent reviewers.
- **D5:** keeping key facts through long contexts (a "case facts" block, trimming tool output); escalation triggers; error propagation across agents; context in large codebases (scratchpads, `/compact`, subagents); human review and confidence calibration; provenance and conflicting sources.

## What the exam rewards (from the 12 official sample questions in the [guide][g], §9)
1. **Use code, not prompts, for rules that must always hold.** Q1 ("agent skips get_customer… 12% of cases"): the answer is a prerequisite gate. Prompts and few-shot examples are "probabilistic."
2. **Fix the root cause with the lightest change first.** Q2: better tool descriptions. Q3: escalation criteria with few-shot examples. Heavier options are "over-engineered."
3. **Self-reported confidence and sentiment are unreliable escalation signals** (Q3).
4. **Use documented, scoped config:** `.claude/commands/` (Q4), `.claude/rules/` globs (Q6), `-p` in CI (Q10). Some distractors are made-up features.
5. **Plan mode when complexity is known up front** (Q5).
6. **Find the real culprit:** the coordinator's decomposition was too narrow, not the downstream agents (Q7).
7. **Structured errors; never suppress them or end the whole workflow** (Q8).
8. **Least privilege:** scoped tools for the common case (Q9).
9. **Batch API only for non-blocking work** (Q11).
10. **Per-file passes plus an integration pass,** not a bigger model or a vote (Q12).

## Official prep resources
The [Partner Academy prep page][prep] lists these free courses: AI Fluency: Framework & Foundations, Building with the Claude API, Claude on Google Cloud, Claude Code in Action, Claude 101, Claude with Amazon Bedrock, and Introduction to Model Context Protocol. Mapping to domains: not found. The [FAQ][faq] (older, pre-Pearson) also recommends the 200-level courses, Agent SDK experience, and a score above 900 on the practice exam. Per the guide, the guide's sample questions come from that practice test. Whether the practice exam is still offered: not found.

[g]: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf
[g0]: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1773274827%2FClaude+Certified+Architect+%E2%80%93+Foundations+Certification+Exam+Guide.pdf
[faq]: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/8lsy243ftffjjy1cx9lm3o2bw/public/1773276532/Claude+Certified+Architect+-+Foundations+(CCA-F)+FAQs+(1).pdf
[prep]: https://anthropic-partners.skilljar.com/page/claude-certified-architect-foundations-prep-courses

## Update: user's Drive copy (v0.2, June 30 2026, 37 pages)

Google Drive file id `16EIKI1oY7XnmdKkIg-fzW8r27Do9xMfE` ("Claude_Certified_Architect_-_Foundations_-_Exam_Guide.pdf"). Local copy in `source/` (gitignored; re-download from Drive).
- Format: 60 questions, single answer (1 correct + 3 wrong), 120 min, 4 of 6 scenarios, pass 720/1000.
- Includes all 12 sample questions with explanations, an appendix of technologies, and in-scope / out-of-scope lists.
- Not in the guide's in-scope list: agent teams, `CLAUDE.local.md`, subagent API-error behavior. Quiz-1 misses Q1, Q5, Q16 are likely practice-site extras → low priority.
- Out of scope: fine-tuning, auth/billing, MCP hosting, computer use, vision, streaming, rate limits, pricing math, prompt-caching details, tokenization, embeddings.
