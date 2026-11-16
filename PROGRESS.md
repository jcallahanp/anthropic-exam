# Progress

## Published pages (update with Artifact `url` = link below; source file = path)
- LEARN (start here): `artifact/patterns.html` → https://claude.ai/artifact/Q2qBxYYfjwEr9hD6gHkVjx
- D3 PLAYBOOK (weakest domain; every guide 3.1-3.6 skill as situation → answer + file map): `artifact/d3.html` → https://claude.ai/artifact/HGYyvQMNR2ynEXeWhK82Zs
- CORE PATTERNS (12 Anthropic design patterns, read once): `artifact/patterns-core.html` → https://claude.ai/artifact/GiwmvHkXbYWuPCWQkSX66q
- TRIAGE (5-min read: high vs low yield + 6 scenarios): `artifact/triage.html` → https://claude.ai/artifact/UaqTgja4pG2AF8daYFTnJb
- TEN-MINUTE SHEET (final scan before exam; cue → pick → decoy rows): `artifact/ten-minute.html` → https://claude.ai/artifact/314NMcfo1XpawuS6D1GW7q
- SPEED RUN (fast lookup during practice tests, one tab per domain): `artifact/speedrun.html` → https://claude.ai/artifact/6JeTiUPbvF9MZYwVzRgw6p
- MISCONCEPTIONS (round 2, thorough backup): `artifact/misconceptions.html` → https://claude.ai/artifact/MvD3BKyQ82zYiy9PPxzwn6
- DRILL: `artifact/cram-station.html` → https://claude.ai/artifact/MfxEtU3WyoXCDkA46HrfZt
- Older: `artifact/blind-spots.html` → https://claude.ai/artifact/ViK8SiURGoiFjWSi3Y9oEa ; `artifact/d1-d2-field-guide.html` → https://claude.ai/artifact/3keyF35TbDuZWYHgRxQq3S
- Anki: `anki/cards.tsv` → `anki/deck.apkg` + `anki/paste.txt` via `python3 anki/build.py` (needs `pip install genanki`).

## Sources
- Official guide v0.2 (user's Google Drive, file id `16EIKI1oY7XnmdKkIg-fzW8r27Do9xMfE`). Local copy `source/` is gitignored: re-download with the Google Drive connector, extract with pypdf.
- Notes: `research/exam-guide.md`. Answer keys live in the two HTML pages (graded vs the guide).
- Exam keys to the guide where the product differs: skill `allowed-tools` = "restricts"; subagent spawn tool = "Task".

## Results
- Quiz 1: 16/25 (64%). Misses Q1, 5, 9, 10, 16, 17, 19, 22, 23 (`research/miss-analysis-01.md`).
- 6 in-scope misses = 3 ideas: mechanism over prompt, least privilege, tool_choice. Q1, Q5, Q16 are outside the guide → low priority.
- Priority: D1 > D2 > D4 > D3 > D5.

## Teach-back log
(add: pattern/tool | pass/retry | what was missing)

- stop_reason | retry (on misconceptions page) | Thought the loop retries failures. Missing: Claude cannot run tools; your code runs the tool, appends tool_result, resends full history; loop until end_turn. Got right: API holds no memory between calls.
- tool_use → tool_result | pass | Causal why correct (no append → Claude never sees it → repeats call). Slip repeated: said "Claude uses the tool". Added note to stop_reason entry.
- Task tool + allowedTools | retry (on misconceptions page) | Had independence idea only. Missing: several Task calls in ONE response; allowedTools needs "Task"; subagents start with empty context.
- AgentDefinition | pass | All 3 parts and bugs correct (description → wrong agent picked; prompt → out-of-scope behavior; tools → misuse/least privilege).
- PreToolUse hook | pass | Why correct (Claude adapts instead of dead-ending). Thin on mechanism: hook is code, runs before the tool, block is guaranteed; ask/allow go to user.
- PostToolUse hook | pass | Normalize + "cannot block, call already ran" correct. Gave normalize twice; missing 2nd job: trim noisy/verbose fields to save context.
- --resume | pass | Stale tool results after file changes → start fresh. Missing: fresh session gets a structured summary of prior findings; or resume and name the changed files.
- fork_session | pass | Save-game analogy correct: resume = continue same save; fork = copy save, try another path, original untouched. Use case: compare 2 approaches from same analysis.
- tool_choice | pass | auto, any, tool correct (quiz-1 Q23 fixed). Missing: none = no tools, text only.
- JSON schema (tool input) | retry (on misconceptions page) | Why correct. Knowledge gap: could not picture the schema/JSON shape or where it goes. Added picture: form → tool_use JSON → your code.
- Message Batches API | retry (on misconceptions page) | Thought batch could hold the loop and wait. Missing: request ends at tool_use; continuing = new batch; latency × every tool call.
- Validation-retry loop | pass | Fixable = format/structure when data is in source; not fixable = data absent. Missing: send the exact validation error back; retrying absent data can push Claude to INVENT → allow null instead.
- MCP tool | pass | Vague description loses to a richer one. Missing: fix stated explicitly (description: what it does, inputs, returns, when to use vs similar tool); built-ins like Grep also compete.
- MCP resource | retry (on misconceptions page) | Framed resource as a clearer tool description. Missing: resource = read-only content/catalog; tool = action; fixes exploratory calls; no library analogy given.
- isError + structured errors | pass | All 4 reactions right. Needed validation example (bad date format → fix input, retry). Not mentioned: empty result is NOT an error; isError separates failure from "found nothing".
- .mcp.json | retry (on misconceptions page) | Thought a function blurs the token. Unsure which part shares. Missing: committed project file = shared; file holds only ${VAR} text; each machine's env fills it at startup.
- ~/.claude.json | pass | Home folder not in repo → teammates/CI never see it. Did not know "CI"; added definition to patterns page.
- CLAUDE.md (3 levels) | retry (on misconceptions page) | Thought user level applies only inside home folder. Missing: user level = you, all projects; project = team + CI; dir = loads when Claude works on files there.
- @import vs .claude/rules/ | retry (on misconceptions page) | Thought rules trigger by tool/scenario; did not explain @import; thought standards/*.md were rules. Missing: @import pulls file into CLAUDE.md; rules load by paths: glob match.
- .claude/rules/ + paths | retry (on misconceptions page) | Thought folder CLAUDE.md loads everywhere; unclear on "file type". Missing: tests are scattered; folder file covers one folder; **/*.test.tsx covers all.
- /memory | retry (on misconceptions page) | Thought /memory = session/learned memory. Missing: /memory lists loaded CLAUDE.md files; cause = rules at user level; fix = move to ./CLAUDE.md + commit. (Quiz-1 Q10 area.)
- .claude/commands/ | pass | Project .claude/commands/ is committed → whole team. Personal path garbled; correct = ~/.claude/commands/.
- Skills (SKILL.md) | pass | Strong analogy: CLAUDE.md = always-on house rules; skill = recipe loaded on demand. Not mentioned: context: fork, allowed-tools.
- context: fork | retry (on misconceptions page) | Problem right (keep noise out of main). Mechanism wrong: thought it is an interactive side chat. Missing: SKILL.md frontmatter; skill runs in subagent; summary returns. Mixed up with fork_session / git fork.
- allowed-tools | retry (on misconceptions page) | Least privilege right. Did not know "Pattern 1" = mechanism over prompt; missed config-vs-prompt link.
- SKILL.md frontmatter keys | pass | context/allowed-tools/argument-hint matched to problems. Did not know the word "frontmatter"; definition added to patterns page.
- Plan mode | pass | Explore + find dependencies before editing. Missing: plan mode is read-only (no edits); use for big multi-file/architecture change with several valid approaches; small clear fix = direct execution.
- Explore subagent | pass | Noise stays out, summary returns: right. Slip repeated: pictured interactive back-and-forth with user. Explore = read-only subagent Claude starts; reads/greps codebase; returns summary. Note added to context: fork screen.
- /compact | pass | Frees context; loses exact facts in summary; keep facts in files. Exam names: case-facts block, scratchpad file.
- -p (--print) | retry (on misconceptions page) | Thought -p defers a question for human review. Missing: no -p = interactive chat waits for input → CI hangs; -p = run once, print answer, exit.
- --output-format json + --json-schema | retry (knowledge gap, on misconceptions page) | Asked for visuals: prose vs JSON vs JSON+schema, and what "post findings" means. Added 4-step picture.
- Read (Grep → Read order) | pass | Grep first to find files, then Read only those. Missing "why": Read costs context; follow imports from the entry point. Grep has its own card (searches contents; Glob = names).
- Write vs Edit | retry (on misconceptions page) | Thought Write wins for many changes; did not know what makes Edit fail. Missing: Edit needs unique exact old text; repeated/mismatched text → fail → Read + Write.
- Edit | pass | Not unique → cannot know which one. (Learned from Write vs Edit screen.)
- Bash | pass | Most powerful/destructive → PreToolUse hooks guard it. Add: hook inspects the command string (e.g. deny rm -rf on prod); prefer Read/Glob over cat/ls.
- Grep vs Glob | pass | Definitions right. Glob example muddled ("look for a function in a file"); Glob only lists files by name pattern, e.g. **/*.tf.
- Glob | pass | Glob **/*.tf, then Grep "prod" in those.

## Low-confidence quiz items (right but guessed)
- Hook matcher for MCP tools: mcp__billing__(a|b|c) regex, not mcp__billing__.* (on misconceptions page)
- Subagents vs agent teams: memorized, not understood (quiz-1 Q1 topic; appears on practice exams, so not low priority). On misconceptions page.
- AgentDefinition fields: right but unfamiliar with model field (per-subagent model; omit = inherit). On misconceptions page.
- MISSED: hook matcher vs hook code. Matcher = tool name only; argument checks (amount, category) go in hook body via tool_input. On misconceptions page.
- MISSED: resume twice vs fork. Picked generic context-rot answer. Correct: 2nd resume sees 1st exploration → not independent → fork_session. Meta-pattern: answer the question's key word with the tool's mechanism; reject true-but-generic answers.
- MISSED: repeated tool call. History kept only text blocks → Claude never saw tool_use/tool_result → repeats. Passed teach-back but missed under exam wording. On misconceptions page.
- MISSED: run tests → Bash. Avoided Bash because "dangerous". Only Bash executes; guard it with hooks. Bash wrong only when Read/Glob/Grep fit.
- Grep across split lines: right but nearly fell for a distractor. Still Grep; multiline pattern or shorter fragment then Read.
- MISSED: tool description vs similar tool. Feared naming the other tool. Correct: purpose + input format + examples + edge cases + explicit boundary ("use X instead when").
- Path-specific rules for 300-line CLAUDE.md: right but shaky. Added REFRESH screen: frontmatter labeled, file tree, load timeline, @import vs paths.
- MISSED AGAIN (2nd time): scattered *.test.ts → .claude/rules/testing.md with paths: ["**/*.test.ts"]. HIGH PRIORITY for drill. Added glob-reading screen.
- Bash(npm run migrate*) wildcard: lucky guess. Trailing * = prefix match → migrate-cleanup allowed. Fix: exact command, or space before *.
- MISSED: test-driven iteration → write tests first, Claude implements until green. Picked plan mode (true-but-generic again; 2nd time this meta-pattern).
- MISSED: terraform/**/* glob (3rd glob miss). * = one level; ** = any depth. HIGH PRIORITY. Added GLOB DECODER screen with match table.
- MISSED: packages/api conventions → packages/api/CLAUDE.md (one folder). Decision rule: folder scope → folder CLAUDE.md; scattered file type → glob rule. Watch overcorrection toward globs.
- MISSED: interacting issues (same critical section) → send together in one message; independent → sequential. (3.5)
- Batch custom_id: guessed right. Unique in batch, 1-64 chars, [a-zA-Z0-9_-]; results in any order → match by custom_id.
- MISSED (new topic, 4.2): examples read as live request → wrap context/instructions/examples/request in separate XML tags.

## Weak subdomains (high-priority misses, from misconceptions page map)
- D3 = 14: 3.3 globs/rules 5 · 3.1 CLAUDE.md 3 · 3.2 skills 2 · 3.5 refinement 2 · 3.6 CI 2
- D2 = 6: 2.5 built-in tools 3 · 2.4 MCP config 2 · 2.1 descriptions 1
- D1 = 5: 1.1 loop 2 · 1.3, 1.5, 1.7 one each
- D4 = 3: 4.1, 4.3, 4.5 (+4.4 guesses)
- D5: practice-site domain quiz = 0 misses. Reasoning slips only (5.3 error payload, 5.4 small lookup). D5 is STRONG; lowest study priority.
- Vendor-contract end<start question: right (4.4).
- detected_pattern granularity: context guess, right (4.4, named in guide). Specific construct → dismissal analysis per rule.
- Batch SLA math (30h SLA − 24h window = submit every 6h): right, confident (4.5).
- MISSED (4.1): categorical criteria = name WHAT KIND of issue counts (in/out list); confidence thresholds (incl. numbers) are not categorical.
- XML tags per category criteria: right by memory, still unclear. Rewrote XML screen: tag = labeled box; 2 uses (examples vs request, per-category criteria). 2nd XML question on practice site.
- Small lookup → Grep directly, no subagent (5.4): right but felt wrong. Proportionality: subagents only for big noisy exploration.
- Subagent error payload (5.3): right, reasoning off (context size). Correct: failure type, attempted, partial results, alternatives → recovery decision.

- MISSED (3.3 family, 6th): rules in .claude/rules/ subfolders ARE discovered recursively (docs: memory page). Folder name does not scope; only paths: does. Card added to speed run.

- MISSED (1.6): fixed + independent steps → parallel calls; orchestrator-workers only when steps vary per input. Card added to speed run D1.

- Niche (LOW): `claude -p --output-format json` already returns total_cost_usd + per-model cost breakdown next to .result (docs: headless page). Not in guide.

## Real-exam reports (research/exam-reports.md, spot-checked by main session)
- Format matches guide (60 items, 120 min, 4 of 6 scenarios, 720). Guide v1.0 (Jul 2026) allows multiple-response items: read "select N". Same task statements as our v0.2.
- Real exam harder than practice (typical: 950+ practice → 840-890 real). Do not trust practice scores.
- D3 catches people; CLI flags "hardest part by far" (rogs.me, verified). Added CLI flags card to speed run.
- Tie-breaker reported: most Claude-native answer, unless constraints say otherwise.
- No first-hand report of agent teams, CLAUDE.local.md, matcher/permission syntax, XML → keep LOW.
- Dec 7 2026 content update does NOT include Architect – Foundations (Pearson page, verified).

## Retake policy (official guide v1.0 + Partner Academy FAQ)
- Wait 14 days after 1st fail, 30 after 2nd, 90 after 3rd. Max 4 attempts per rolling 12 months. Full fee ($125) each attempt (partner discount applies).
- Score report shows % correct per section → use it to target the retake.

## Scope check: Cert Safari questions vs official guide (v0.2 text)
Explicitly out of scope: NONE of the pasted questions.
Core (named in guide task statements) -> HIGH priority:
- resume twice vs fork_session (1.7) | repeated tool call / history (1.1) | refund >$500 hook in code (1.5)
- Bash to run tests, Grep split lines (2.5) | tool description boundaries (2.1)
- path-specific rules, scattered tests glob, terraform glob (3.3) | packages/api CLAUDE.md (3.1)
- test-driven iteration, interacting issues (3.5) | custom_id for correlation (4.5)
Not in guide (practice-site detail) -> LOW priority, skim only:
- agent teams (0 mentions) | AgentDefinition model field (guide lists description, prompt, tools only)
- hook matcher regex syntax mcp__server__(a|b) | Bash(cmd*) permission wildcard syntax
- custom_id format rules (64 chars, charset) | XML tags to fence examples (0 mentions; 4.2 is few-shot)

## Final explain-back log
(format: prompt | parts right / total | gaps)

## Next step
Tools deck: first pass DONE (36/36). Next: Patterns deck teach-backs (25), then round 2 on misconceptions page, then drill, then practice exam 2.
