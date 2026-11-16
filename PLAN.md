# Plan

Goal: pass Claude Certified Architect – Foundations in ~4-5 hours of study. User is tired, has ADHD, learns by seeing + teaching, pattern-matches fast. Big text, one idea per screen, show the WHY.

Workflow:
1. LEARN: user reads `artifact/patterns.html` (25 patterns + 36 tools).
2. TEACH BACK: user pastes "Teach-back, <name>: <prompt> My answer: …" in chat. Claude grades on 3 points (mechanism, causal why, misconception), quotes what is missing, gives one fix, logs it. CHAT REPLY STAYS SHORT (pass/retry + link, max 3 lines). On retry: add one entry to the `M` array in `artifact/misconceptions.html` AND its [subdomain, high|low] to `META` (high = named in guide task statement) AND its {src, q (real question stem or teach-back prompt), keys (substrings of q), steps: [Spot, Rule out, Pick]} to `QX` (you thought / right picture / gaps / trap / retry questions), republish to its URL, log one line in PROGRESS.md. No retry now in chat.
2a. SPEED RUN: `artifact/speedrun.html` = concise cards per domain (array `C`). When a new high-yield miss appears, add one card there too.
2c. FINAL EXPLAIN-BACK: 6 capstone design prompts at the bottom of `artifact/ten-minute.html` (array `CAP`). User pastes "Final explain-back, <title>: … My answer: …". Grade every numbered part: right file/flag/tool/field + why the decoy fails. Log gaps in PROGRESS.md.
2b. ROUND 2 (after first pass of all teach-backs): user works through `artifact/misconceptions.html`, pastes "Teach-back round 2, <name>: … My answer: …". Pass → mark entry fixed in PROGRESS.md.
3. DRILL: `artifact/cram-station.html` (62 cards, 66 MCQs incl. official 12).
4. PRACTICE EXAM: Claude writes a fresh mock (single-answer, scenario style, weighted D1 27 / D2 18 / D3 20 / D4 20 / D5 15, extra weight on weak items). Grade, then drill the misses.
5. Repeat 2-4 until confident.

| # | Task | Check | Status |
|---|---|---|---|
| 1 | Learning-science research | Rules cite findings | done |
| 2 | Official exam guide facts (Drive v0.2) | Domains, samples, scope lists captured | done |
| 3 | Quiz 1 miss analysis | Every miss labeled; answers verified vs docs | done |
| 4 | Cram station (cards + drill) | Independent grader: 137 items, 1 fix applied | done |
| 5 | Visual patterns + tools page | Independent grader: 3 fixes + 3 screens added | done |
| 6 | Teach-backs on all patterns/tools | Each graded pass; weak list in PROGRESS.md | todo |
| 7 | Practice exam 2 (fresh) | Score; misses mapped to patterns | todo |
