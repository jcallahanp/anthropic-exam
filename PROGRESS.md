# Progress

## Published pages (update with Artifact `url` = link below; source file = path)
- LEARN (start here): `artifact/patterns.html` → https://claude.ai/artifact/Q2qBxYYfjwEr9hD6gHkVjx
- MISCONCEPTIONS (round 2): `artifact/misconceptions.html` → https://claude.ai/artifact/MvD3BKyQ82zYiy9PPxzwn6
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

## Next step
User does teach-backs from the patterns page, then drill, then ask for practice exam 2.
