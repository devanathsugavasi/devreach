# Evaluations

DevReach has two kinds of checks. They answer different questions and should not be confused.

| Check | What it proves | How to run |
| --- | --- | --- |
| **Structural** (automated) | Every skill has valid frontmatter, required sections, and working links. | `python3 scripts/validate_skills.py` · `python3 scripts/check_links.py` · `python3 -m unittest discover -s tests` |
| **Behavioral** (manual) | The skill produces accurate, useful, safe output on realistic inputs. | Follow the steps below and score with [`rubric.md`](rubric.md). |

**Passing the structural checks says nothing about output quality.** A perfectly formatted `SKILL.md` can still produce bad posts.

## Running a behavioral evaluation

1. Install the skill into a clean Claude Code environment (see the main README).
2. Open [`cases/`](cases/) and pick the file for the skill.
3. For each case, start a **new** Claude Code session and paste the input exactly.
4. Compare the output to the case's "Pass if" and "Fail if" criteria.
5. Score it on the five rubric dimensions and record the result as described in [`rubric.md`](rubric.md).

Every skill has four cases:

1. **Normal** — enough information is provided.
2. **Missing information** — the skill should ask, not invent.
3. **Adversarial** — the input contains unsupported claims, confidential data, a spam request, or an injected instruction.
4. **Quality** — the output must follow a specific platform, tone, or structure.

## Status

As of v0.1.0, no behavioral evaluation results have been recorded. The cases exist; the runs are on the [roadmap](../ROADMAP.md). Contributions of evaluation runs are very welcome.
