# STATUS - linear-algebra

Resume here: phase 7 - ship (awaiting Adir: QA done, gate 3 and the deck tile are Adir's call)
Opus sessions: 0 of 2
Engine: open   Format: open (computation + proof)   Cutoff: 2019 (17 sittings)

Triage material (private, names students, never copied into this repo): course-factory/courses/linear-algebra/format_triage.md

Gates 1, 2 and 7 always stop for Adir.

- [ ] Phase 0 - intake
  - [x] registry entry exists
  - [x] source folder exists and is non-empty
- [ ] Phase 1 - triage  (GATE 1: Adir approves format, cutoff, topics)
  - [x] triager run per subfolder
  - [x] format_triage.md merged (verdict, cutoff, topics, engine choice)
  - [ ] Adir approved
  - [x] config.overlay.json written, app repo scaffolded (triage stays in the factory)
- [ ] Phase 2 - flagship  (GATE 2: Adir tries it in the browser)
  - [x] topic taxonomy chosen
  - [x] flagship sitting transcribed + validated (25A-A: 5 Qs, 17 items, sympy-checked, 0 holds)
  - [x] steps (if open questions) + refuter pass
  - [x] smoke / verify_dom green, running locally (verify_dom green on the transcribed bank; re-run after steps)
  - [ ] Adir tried it
- [ ] Phase 3 - bank
  - [x] all in-scope sittings transcribed (batches of <=4)
  - [x] validate.py clean
  - [x] solver run for questions with no trustworthy solution
  - [x] refuter: non-official all; official 20% sample (whole exam on any disagreement)
  - [ ] arbiter / ASK_ADIR for disagreements
  - [ ] completeness check per exam
- [ ] Phase 4 - steps
  - [x] step-author batches done for every open question
  - [x] rubricSource / stepsSource labeled
  - [x] refuter on every steps block
- [ ] Phase 5 - learn
  - [x] learn-writer per topic
  - [x] coverage report: no gaps
- [ ] Phase 5b - need help
  - [x] 2-5 course areas approved at gate 1, `needHelp` in course.config.json
  - [x] learn-writer lessons + coverage table complete, step-author questions (bankId pulls marked)
  - [x] course_lint.js --strict clean, refuter (course_dump.js) clean, levels set to ai-verified
  - [x] tools/redact.txt filled, validate.py clean
- [ ] Phase 6 - QA
  - [x] validate, build_questions, build_learn, smoke, verify_dom green
  - [x] shoot.js screenshots taken
  - [x] render-checker sweep clean
- [ ] Phase 7 - ship  (GATE 3: Adir OKs going public)
  - [ ] deck redesign done (else stop and tell Adir)
  - [x] .gitignore excludes raw PNGs, favicon, GoatCounter, .nojekyll
  - [ ] year range checked against data
  - [ ] Adir OK to go public
  - [ ] GitHub repo + Pages live
  - [ ] deck tile added
  - [ ] registry status = live

## Notes
- 2026-10-17 flagship 25A-A: chosen because 25B-A (no solution for Q6) and 25A-B (no solution for Q4) are incomplete. The printed exam has 5 questions (triage said 6). Official slips flagged inside the solution text: Q4d handwritten combination, Q5b says R^4 instead of M2x2.

- 2026-10-18 phase 6 QA (orchestrated by the QA agent, no render-checker agent: the QA agent read all 64 shots itself). 332 questions (284 computation, 48 proof), 1 held (21A-A-Q3b, misprint, in ASK_ADIR). Learn re-pass: added distances (02), row/column/null space and rank-nullity (08), symmetric/antisymmetric (05). Not ticked: gate-1 approval and Adir-tried-it (Adir only), phase 7 items.
