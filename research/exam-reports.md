# CCA-F / CCAR-F: What Test Takers Report

Research date: 2026-11-16. Exam name: Claude Certified Architect – Foundations. The code was CCA-F at launch (March 2026). The code is CCAR-F since the move to Pearson VUE (30 June 2026).

Scope: reports from people who say they sat the real exam. This file gives topic-level reports only. It contains no real exam questions.

Labels:
- **First-hand**: a named or pseudonymous person says they sat the exam.
- **Anonymous**: a first-hand claim with no name, or on a vendor-hosted page. We cannot verify it.
- **Vendor**: a seller of prep material wrote it.
- **Official**: Anthropic or Pearson VUE.

---

## Bottom line

- **The format matches the guide.** Many test takers confirm: 60 questions, 120 minutes, 4 scenarios of 15 questions each, scaled 720/1000 to pass. One difference: the official guide v1.0 says "multiple-choice and multiple-response items". Three test takers say every item on their exam was single-answer. Read the "select N" line on each item.
- **The real exam is harder than the official practice material.** Most reports say this. The real items are longer, denser, and have more plausible distractors. Typical drops: 950–1000 on the official practice exam, then 840–890 on the real exam. One person scored 1000 in practice and 590 on the real exam. Anthropic retired the official practice exam on 30 June 2026. Now the official items are only the 12 sample questions in the guide.
- **Claude Code configuration (D3) is the domain that surprises people.** Daily Claude Code users often score lowest there. One passer says specific CLI flags were "the hardest part of the exam by far". Reports also name CI/CD headless mode, the CLAUDE.md hierarchy, and choosing between CLAUDE.md, hooks, and permissions. We found no first-hand report about agent teams, CLAUDE.local.md, hook matcher syntax, permission rule syntax, or XML tags.
- **The same study advice repeats.** "Code must, prompt should": use hooks or gates for guarantees and prompts for guidance. Pick the lightest fix at the root cause. Build something hands-on. Practise at the real pace of 2 minutes per question. Keep a log of wrong answers. Do not trust a high practice score.
- **Third-party question banks get mixed reviews. CertSafari is mid-range.** Some passers on CertSafari's own page say it is "very similar". Others say it "wasn't remotely close", or that its answers are "more clear" than the real ones. One independent passer rated it "medium". Free mocks in general are often called "too basic", AI-generated, or sometimes wrong.

Confidence: **moderate**. Format and "harder than practice" have many consistent first-hand reports. The topic lists are anecdotal and recalled from memory. Some posts predate the 30 June 2026 platform change.

---

## 1. Do test takers describe the real exam? Does it match the guide?

### What the official sources say now

- Guide v1.0 (effective July 2026, CCAR-F): 60 items. "Multiple-choice and multiple-response items; each item states how many responses to select." 4 scenarios drawn from a bank of 6. 120 minutes. Scaled 720 on 100–1,000. $125. Valid 12 months. The score report shows percent correct per domain. Source: the official exam guide PDF.
- The guide gives these domain weights: D1 Agentic Architecture & Orchestration 27%, D2 Tool Design & MCP 18%, D3 Claude Code Configuration & Workflows 20%, D4 Prompt Engineering & Structured Output 20%, D5 Context Management & Reliability 15%. **These match the weights in your brief.**
- The Anthropic FAQ says to plan for "about 135 minutes of total seat time". It says you see your score on screen at the end. It says "The practice exam available on the previous platform was retired in the move to Pearson." The guide says its 12 sample questions are "drawn from the practice test".
- The Pearson VUE page says some exams update on **7 December 2026**, with new guides on **17 November 2026**. It names Associate, Developer and Architect – Professional. **It does not name Architect – Foundations.** One Reddit poster (2 Nov 2026) says that "exams" in general change on 7 December. Check the Pearson page if you sit the exam on or after 7 December.

### What test takers say

| Item | Guide | Test-taker reports | Match? |
|---|---|---|---|
| Questions | 60 | 60. VGV (Jun 2026), Yu (Aug 2026), INSIGHT LAB (Aug 2026), r/claudeskills (Oct 2026) and others agree. | Yes |
| Time | 120 min | 120 min. Rob Burke says "2 hours for 60 questions" and the practice exam gave 90 min. rogs.me says "2 and a half hours", which is probably seat time. Rob Burke: "hold two and a half hours". | Yes |
| Scenarios | 4 of 6, about 15 questions each | 4 blocks of 15 (VGV, INSIGHT LAB, Rob Burke). **Exception:** one Reddit user (25 Mar 2026) says a scenario on their exam was not in the guide's 6. They say the pool "may draw from up to 13". Rick Hightower repeats this as "community-sourced and not confirmed". No later report confirms it. | Mostly. One unverified early exception. |
| Item type | Multiple-choice and multiple-response | **All single-answer**, per u/OkRelationship3427 (Jul 2026: "no multiple-select questions… single-answer four-choice"), Skool post (undated: "no 'pick two' questions") and u/Rcannotberesolved (Nov 2026: "strictly single-response"). Learning Tree (vendor) says "some questions require selecting more than one answer". | Your brief's "single-answer" matches the reports. The guide allows multi-select. |
| Pass mark | 720/1000, scaled | 720. VGV passed with 738 at 44/60 correct (73% raw). Loginov got 886 at 52/60. Some 2026 scores were corrected upward later (ttsubasa, Jun 2026: 705 became a pass). | Yes |
| Domain weights | 27/18/20/20/15 | Yu (Aug 2026), Akshay Kokane (Jun 2026) and Learning Tree give the same weights. One Apr 2026 post gives 25/20/20/20/15, probably an older draft. | Yes |
| Results | On screen (FAQ) | Before 30 June: no score at the end. Results came after days to weeks (VGV: "the real one shows you nothing when you finish"). After the move, a Reddit thread (Sep 2026) says "You get your results instantly". | Yes, after the move |
| Validity | 12 months | Early sources say 6 months (VGV, Udacity). The FAQ and a GitHub FAQ say credentials earned before 30 June were extended to 12 months. | Yes, now |

---

## 2. Is the real exam different from the guide or the practice tests?

### Harder than the official practice exam (most reports)

- VGV / John Weidner (24 Jun 2026): "the practice exam and the real exam share no questions." The exam "had been harder than I expected." He scored 738 after practice runs of about 850 and 930.
- Anthony West, itone Substack (13 Jul 2026): the real items are "denser and more tricksy" than the official mock or the training material.
- John Mathew, Medium (20 May 2026): "the real exam is cognitively more demanding than the official practice test." The practice items are "more direct".
- Danila Loginov, Medium (2 Jul 2026): 1000/1000 on the practice exam, then 886 on the real exam. "A genuine step up from anything in the practice tests or the guide."
- Big Tech Careers newsletter (25 Jun 2026): 950+ on practice, then 881 on the real exam. Real scenarios have "more layered detail and ambiguity".
- u/Plastic_Safe2016 (12 Jun 2026): about 950 on the official practice, then 843 on the real exam.
- Reddit r/ClaudeAI "CCA-F Questions" (about 27 Apr 2026, first-hand, unverified): 1000/1000 on practice three times, then **590** on the real exam. The poster says the exam was "heavily focused on the Anthropic API and Claude SDK". Note: the guide does cover the Agent SDK and the API. Their claim that the guide does not mention them conflicts with the guide.
- r/claudeskills (9 Oct 2026): "The official practice exam is easier than the real thing."
- Rick Hightower, Substack (16 Jun 2026, secondhand case): 980 on practice, 744 on the real exam. He calls the practice exam "recall" and the live exam "judgment".

**Counter-reports:** Yu (Aug 2026) says his third-party mock scores "tracked the real one closely" (mocks 766–915, real 882). One anonymous CertSafari review (Nov 2026) says "Many exam questions look simpler" than the study questions.

### Trick wording and scenario style

- Almost every item gives a broken production system and four plausible fixes. Rob Burke (20 Jun 2026): the right answer "fixes the root cause with the lightest sufficient intervention". The wrong answers "sound like good engineering".
- Loginov: "every answer is workable, and the question turns on degree." The hardest part was "parsing the questions rather than picking the answers".
- rogs.me (19 Jul 2026): the questions are "convoluted". "After about 45 minutes of dense, twisty questions I was toast."
- Yu: "Same symptom, different mechanism, completely different answer." An extra qualifier in the scenario often rules out some options.
- Reddit thread (Sep 2026, top comment): the exam "skewed heavily towards 'scaled AI implementation' problems". That commenter failed once, then passed.
- u/beethovenzhang (14 Jul 2026, 904): some questions "feel pedantic and opinionated."
- CertSafari failed reviews (anonymous): "So many contradictory words in the questions", "Very very plausible identical answers".

### Topics beyond the guide, or more detail than the guide

- **Claude Code CLI flags.** rogs.me: "They started asking about specific flags and what they do." This was "the hardest part of the exam by far". An anonymous CertSafari fail (640, Oct 2026) says they did not know about "bare" and "append system prompt" in CI/CD. That points to flags such as `--bare` and `--append-system-prompt` (our reading).
- **Implementation detail and outdated syntax.** Loginov: "Some questions get quite specific on implementation detail and land on outdated syntax… (@import)." He also says "some questions get right down to the specs" of the Messages API.
- **Opposite view.** Rick Hightower: the live exam "does not reward you for reciting parameter names or exact enum strings". One passer reports "almost no `stop_reason` enumeration questions" (secondhand).
- **Claude Code itself is weighted more than people expect.** Daily users still lose points here (see section 3).
- **Possible extra scenarios.** One report says the pool may hold up to 13 scenarios (Mar 2026). This is unverified, and no later report confirms it.
- **"Safety and Responsible Deployment" area.** Only Rick Hightower mentions it, and he calls it community-documented. Treat it as unverified.
- **Items from your brief:**
  - Agent teams: **no report found.**
  - CLAUDE.local.md: **no report found.**
  - Hook matcher syntax: **no first-hand report.** Only vendor blogs (certified-architect.com, CertSafari lessons) cover it.
  - Permission rule syntax: **no first-hand report.** CertLand (vendor) claims "The exam tests edge cases around conflicting rules and glob patterns". This is unverified marketing. First-hand reports describe a choice question instead: "CLAUDE.md vs PreToolUse hooks vs settings.json permissions - when to use which" (u/SlayerC20, Sep 2026).
  - XML tags: **no first-hand report.**
  - Specific API parameters: mixed evidence (see the bullets above). Reports do name `stop_reason` and `tool_choice`, and nullable vs optional fields.

---

## 3. Which topics were heavily tested or surprised people?

The topics people name match the guide's task statements. The surprise is the depth and the wording, not new subjects.

**Claude Code configuration (D3) is the most common surprise.**
- VGV: D3 was his weakest domain at 69%, "despite daily use".
- Anthony West: he scored poorly on the areas he uses daily.
- Udacity author (2 Jul 2026): weak areas were "team Claude Code repositories, CI/CD, and large-scale unit testing".
- Akshay Kokane (24 Jun 2026): he studied "Claude Code in GitHub Actions, specifically the non-interactive pipeline mode". He says the practice exam "surface-tested" about a dozen concepts that the real exam "goes deeper on".
- Claude Certification Guide data (vendor, Oct 2026, from its own mock): D3 is the hardest domain. People miss CI/CD, the GitHub Action behaviour, the CLAUDE.md hierarchy, and when to choose a hook versus a prompt.

**Topics from u/SlayerC20's memory list (Sep 2026):**
- Structured output: nullable vs optional fields.
- Tool descriptions and few-shot examples for tool selection.
- Chaining tool calls.
- When to retry a failed tool call and when to surface the error.
- MCP structured errors.
- Where MCP context loads in a session.
- Subagents and context flooding.
- Resuming and forking sessions.
- Plan-first vs direct execution.
- The tool loop: `tool_use`, `tool_result`, `end_turn`.
- CLAUDE.md vs hooks vs permissions.
- Grep vs Glob vs Read.

**Topics on CertSafari "heavy on the exam" tags (anonymous, Sep–Nov 2026):**
- MCP and MCP server scopes.
- CI/CD.
- Escalation to a human.
- JSON schemas.
- Context management.
- Agent SDK.
- Subagents.
- Plan mode vs direct execution.
- Session resumption.
- `tool_choice`.
- Batch API.
- CLAUDE.md.

**Other single reports:**
- Loginov: D4 (prompt engineering) was his weakest domain at 50%.
- Rob Burke: D5 (context management) was his weakest.
- aiwithsachin (3 May 2026): "Domain 5 caught me off guard."

**Recurring "exam traps" that passers name:**
- Prompt instructions offered for something that must be guaranteed.
- "Bigger model / more agents / more tools / bigger context".
- Fine-tuning.
- "Tell it to be more careful".
- Self-reported confidence.
- Arbitrary iteration caps.
- Escalation based on sentiment.

Sources: u/Plastic_Safe2016, Suraj Khaitan (dev.to), Rob Burke, u/OkRelationship3427 thread ("choosing the bigger model" is always wrong).

---

## 4. Study advice that people repeat

1. **Use a hook or gate for "must" and a prompt for "should".** Named as the key idea by aiwithsachin, Rick Hightower, u/Plastic_Safe2016, Suraj Khaitan and John Mathew.
2. **Pick the smallest fix at the earliest layer.** Distrust options that "sound impressively senior". Sources: Rob Burke, u/Plastic_Safe2016.
3. **Build something hands-on.** Build an agent with the Agent SDK, an MCP server, a Claude Code setup with hooks and rules, and an extraction pipeline. Nearly every passer says this: Udacity, Learning Tree, the March Reddit post, Loginov, VGV.
4. **Read the official exam guide several times.** It sets the scope. Akshay Kokane says to read it "3–4x". Read all six scenarios before the exam (Rob Burke, aiwithsachin).
5. **Study the Claude Code CLI flags and CI/CD headless use.** Do not skip D3 because you use Claude Code daily (rogs.me, VGV, Anthony West).
6. **Practise at the real pace.** You have about 2 minutes per item. Read the question line first, flag hard items, move on, and never leave a blank (John Mathew, Skool post, VGV). Two failed candidates ran out of time or found 2 hours tight.
7. **Keep a log of wrong answers.** Record why you chose each wrong option. Retest later with the options reworded (Yu, Skool post, VGV).
8. **Do not trust a high practice score.** Treat 900+ as a floor, not a forecast (VGV, Rick Hightower). Repeat attempts at a fixed practice set measure memory: "memorization wearing the costume of mastery" (VGV).
9. **Be careful with practice questions that Claude generates.** They are "biased and much easier" (Anthony West). They focus on "easy specifics" (Udacity). Claude's encouraging tone gives "a false sense of readiness" (Learning Tree).
10. **Ask "why are the other options wrong?"** Failed-then-passed candidates say this changed their result (u/crime_master_tj, 696 then 809; Gokula Krishna Subramaniam on CertSafari, failed twice then 899).

---

## 5. Are third-party question banks close to the real exam?

### CertSafari (certsafari.com, about 480 questions, AI-generated)

CertSafari hosts an "exam experiences" page. Users submit the reviews. Some have a verified credential, but most are anonymous. Treat them as weak evidence.
- **Close:**
  - Ali Ahnaf (verified, 893, Nov 2026): "very similar to what I practiced in Cert Safari".
  - Anonymous 787 (Oct 2026): "About 80% felt familiar".
  - Anonymous 830 (Nov 2026): "Very similar to CertSafari."
- **Far:**
  - Anonymous fail, 480 (Oct 2026): "wasn't remotely close".
  - Anonymous fail, 690: "more demanding than the certSafari tests".
  - Anonymous fail, 640: real answers are "more vague"; "in cersafari the answers more clear".
  - Anonymous fail, 711: "I didn't get any of the question common".
  - Anonymous fail, 763: "This test has some incorrect answers as compared to anthropic official guidance."
- **Independent views:**
  - u/Plastic_Safe2016 (Reddit, 12 Jun 2026): CertSafari is "medium, with hundreds of questions".
  - INSIGHT LAB, Raymond (note.com, 27 Aug 2026, passed 773): the questions are AI-generated, so the same items rarely appear on the exam. But they follow the guide closely and are useful for concepts.
  - John Mathew (Medium, May 2026): "Helpful for additional preparation questions".

**Verdict: useful for concept drill. It is not reliable as a difficulty match.** Real distractors are reported as vaguer and closer together.

### Other banks

- **Claude Certification Guide (claudecertificationguide.com, free):**
  - rogs.me: "the closest I found", but not identical.
  - Yu: mock scores "tracked the real one closely".
  - u/crime_master_tj used it.
  - u/Plastic_Safe2016: "medium".
  - Note: its owner also posts usage data on Reddit (vendor).
- **CyberSkill mock:** "hard, but very helpful" (u/Plastic_Safe2016).
- **SkillCertPro:** "easy" (u/Plastic_Safe2016).
- **Tutorials Dojo:** one user (forum, 10 Jul 2026) says the real exam "was much harder than I expected based on my preparation". Tutorials Dojo replied that it plans updates.
- **Matt Purcell's CCA-F PDF:** the real items are "way more wordy and harder" (u/inzicv, Aug 2026).
- **Udemy:** "obviously… generated by Claude" (CCAR-P thread, Aug 2026; the comment is about practice exams in general).
- **General verdicts:**
  - rogs.me: free mocks are "way too basic".
  - Anthony West: prep sites have many "questionable" items, and some are "plainly wrong".
  - Learning Tree: "AI-generated and shallow".
  - u/Rcannotberesolved (Nov 2026): they "aren't correlated highly" to the exam. Some use "select two" items, but the real exam is "strictly single-response".
  - March 2026 Reddit post: "of very limited help".

---

## Sources

| URL | Date | Type |
|---|---|---|
| https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf | Jul 2026 (v1.0) | Official |
| https://anthropic-partners.skilljar.com/page/faq-certifications | undated, after 30 Jun 2026 | Official |
| https://www.pearsonvue.com/us/en/anthropic.html | updated 2026-11-12 | Official |
| https://verygood.ventures/blog/passing-the-claude-certified-architect-exam/ | 2026-06-24 | First-hand |
| https://itone.substack.com/p/lessons-from-the-anthropic-architect | 2026-07-13 | First-hand |
| https://levelup.gitconnected.com/how-i-passed-the-claude-certified-architect-foundation-cca-f-exam-in-my-first-real-attempt-b6d24c60a058 | 2026-06-24 | First-hand |
| https://medium.com/@johnelanji/how-i-passed-the-anthropic-claude-certified-architect-foundations-cca-f-exam-a-complete-1108dce46e9b | 2026-05-20 | First-hand |
| https://loginov-rocks.medium.com/build-as-anthropic-claude-certified-architect-foundations-cca-f-04fcd371b8c3 | 2026-07-02 | First-hand |
| https://yu-wenhao.com/en/blog/ccar-f-exam-experience/ | 2026-08-29 | First-hand |
| https://rogs.me/2026/07/how-i-got-claude-certified-and-how-you-can-too/ | 2026-07-19 | First-hand |
| https://robburke.net/side-quests/anthropic-architect-cert/ | 2026-06-20 | First-hand |
| https://newsletter.bigtechcareers.com/p/how-i-passed-claude-architect-certification | 2026-06-25 | First-hand (promotes a book) |
| https://www.udacity.com/blog/the-claude-certified-architect-exam-explained-by-someone-who-passed-it/ | 2026-07-02 | First-hand on a vendor blog |
| https://www.learningtree.com/blog/my-journey-claude-certified-architect-foundations-certification/ | undated | First-hand on a vendor blog (promotes a course) |
| https://dev.to/suraj_khaitan_f893c243958/i-passed-the-claude-certified-architect-foundations-cca-f-exam-my-journey-lessons-and-98j | Apr 26 (2026 assumed) | First-hand |
| https://aiwithsachin.substack.com/p/i-passed-the-claude-certified-architect | 2026-05-03 | First-hand |
| https://note.com/insight_lab_tech/n/n856e6c29e343 | 2026-08-27 | First-hand (Japanese) |
| https://note.com/__ttsubasa__/n/n87f85581c7a3 | 2026-06-07 | First-hand (Japanese) |
| https://rickhigh.substack.com/p/anthropics-claude-certified-architect | 2026-06-16 | Unclear. The author is certified but sells a guide. The cases are secondhand. |
| https://www.reddit.com/r/ClaudeAI/comments/1s34iyl/ccaf_the_real_exam_has_more_scenarios_than_the | 2026-03-25 | First-hand, pseudonymous, unverified |
| https://www.reddit.com/r/ClaudeAI/comments/1sxac8o/ccaf_questions | about 2026-04-27 | First-hand, pseudonymous, unverified |
| https://www.reddit.com/r/ClaudeAI/comments/1sgn0cf/passed_anthropics_claude_certified_architect/ | Apr 2026 | First-hand, pseudonymous |
| https://www.reddit.com/r/ClaudeAI/comments/1u43exm/passed_the_claude_certified_architect_foundations | 2026-06-12 | First-hand, pseudonymous |
| https://www.reddit.com/r/ClaudeAI/comments/1uvtx89/on_claude_certified_architect_exam | 2026-07-14 | First-hand, pseudonymous |
| https://www.reddit.com/r/ClaudeAI/comments/1v5zrru/passed_the_ccarf_with_9041000/ | 2026-07-25 | First-hand, pseudonymous |
| https://www.reddit.com/r/ClaudeAI/comments/1vjs351/claude_code_certified_arhitect_foundational_how | 2026-08-09 | First-hand comment, pseudonymous |
| https://www.reddit.com/r/ClaudeAI/comments/1w04zq6/passed_ccaf_on_my_second_attempt_sharing_what | 2026-08-27 | First-hand, pseudonymous |
| https://www.reddit.com/r/ClaudeAI/comments/1weg67m/just_took_anthropics_architect_foundations_exam | 2026-09-12 | First-hand, pseudonymous, with comments |
| https://www.reddit.com/r/claudeskills/comments/1x1o45h/i_passed_anthropics_claude_architect_foundations | 2026-10-09 | First-hand (promotes a webinar) |
| https://www.reddit.com/r/ClaudeAI/comments/1xlkzzn/both_claude_certified_architect_exams_my | 2026-11-02 | First-hand, pseudonymous |
| https://www.reddit.com/r/ClaudeAI/comments/1xg0ihc/i_analysed_35000_ccarf_practice_answers_from/ | 2026-10-26 | Vendor (data from the poster's own free mock site, not from the real exam) |
| https://www.reddit.com/r/ClaudeAI/comments/1ukcez5/ccaf_has_anyone_elses_claude_certified_architect | 2026-07-01 | First-hand (platform-move issues) |
| https://www.reddit.com/r/ClaudeCertified/comments/1vo909f/passed_ccarp_exam_harder_than_expected | 2026-08-14 | First-hand (CCAR-P; one comment about CCAR-F near-miss scores) |
| https://www.reddit.com/r/ClaudeAI/comments/1vrl9ng/passed_the_claude_certified_architect | 2026-08-18 | First-hand (CCAR-P; comment on Udemy banks) |
| https://www.skool.com/claude-certified/i-passed-4?p=da2d6a28 | undated | First-hand, community post |
| https://www.youtube.com/watch?v=wNoC9jdLKiY | 2026-09-20 | First-hand (failed with 708, then passed) |
| https://www.certsafari.com/exam-experiences/anthropic/claude-certified-architect-foundations | Aug–Nov 2026 entries | Anonymous / some verified, hosted by a vendor |
| https://portal.tutorialsdojo.com/forums/discussion/claude-certified-architect-foundations-cca-f-practice-exams-update/ | 2026-07-10 | Anonymous user plus vendor reply |
| https://certland.net/blog/cca-f-exam-day-experience-what-to-expect/ | 2026-04-08 | Vendor ("composite" stories, not verified) |
| https://certland.net/blog/cca-f-exam-traps-claude-code-context-management | 2026-03-27 | Vendor (claims about permission and glob edge cases are not verified) |
| https://claudearchitectcertification.com/blog/claude-certification-reddit-reviews-what-candidates-actually-say | 2026-08-20 | Vendor aggregation |
| https://github.com/Amey-Thakur/CLAUDE-CERTIFICATIONS/blob/main/guide/faq.md | undated | Unclear (community summary of official FAQ) |
