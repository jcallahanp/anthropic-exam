# Exam crash course: spec

Status: DRAFT. Open questions block the plan. See "Open questions".

## Goal

Raise the user's score on one multiple-choice exam after a few hours of study.
The user is sleep-deprived and has low attention.
The user knows most concepts. The user misses small details and trick questions.

## Method (80/20)

1. Analyze missed practice-exam questions. Find patterns, not single facts.
2. Classify each miss by cause:
   - Knowledge gap: the user did not know the fact or tool.
   - Heuristic gap: the user knew the facts but chose a "true but not best" answer.
   - Reading error: the user missed a qualifier (NOT, FIRST, BEST, MOST, EXCEPT).
3. Find 1-3 tie-break heuristics that explain most heuristic-gap misses.
   Example (NASM): "Pick the most safety-first answer."
4. Find the few tools or concepts that explain most knowledge-gap misses.
5. Build one visual artifact: a blind-spot map plus a short retrieval drill on the misses.
6. Test with fresh questions that match the miss patterns.

Learning-science rules for the session: see `research/learning-science.md`.

## Personas (definition of done)

1. I am a tired test taker using the crash-course page.
   I open it and see my 3-5 blind spots and tie-break rules on one screen.
   I trust it to show only what I get wrong.
   I never have to reread material I already know.
2. I am a test taker at a hard question, unsure between two answers.
   I apply one tie-break question from the page.
   I trust it to pick the answer the exam writer wants.
   I never have to recall a long list under pressure.
3. I am a tired learner doing a 20-minute drill.
   I answer each question before I see feedback.
   I trust the drill to repeat my misses until I get them right.
   I never have to plan what to study next.

## Done check (deterministic)

- Every missed question has a cause label and a domain label.
- Each heuristic explains at least 3 misses.
- The user scores higher on a fresh drill set than on the original misses.

## Constraints

- Total study time: a few hours (exact time: open question).
- Short drill blocks. Visual format. Minimum reading.

## Open questions

1. Exam name, format, question count, pass score, date and time.
2. "KD20 rule": assumed to mean the 80/20 rule.
3. Hours left before the exam, and sleep plan.
4. Practice-exam input: questions, the user's answers, correct answers, explanations.
