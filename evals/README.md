# Evaluations

DevReach has two kinds of checks. They answer different questions.

| Check | What it proves | How to run |
| --- | --- | --- |
| **Structural** (CI, free) | Skills have valid frontmatter and required sections, links resolve, every skill has four eval cases, the install script works. | `python3 scripts/validate_skills.py` · `python3 scripts/check_links.py` · `python3 -m unittest discover -s tests` |
| **Behavioral** (local, costs API usage) | The skills produce accurate, useful, safe output on realistic inputs. | `claude plugin eval` (below) |

**Passing the structural checks says nothing about output quality.**

## Layout

```
evals/
├── cases/<skill>/<n>-<kind>/case.yaml   # 4 per skill: normal, missing-information, adversarial, quality
├── fixtures/gst-invoice-parser/          # fake repository copied into the workspace for open-source-growth cases
├── rubric.md                             # rubric for human review
└── RESULTS.md                            # recorded runs
```

Each `case.yaml` is a [Claude Code plugin eval](https://docs.claude.com/en/docs/claude-code/plugins) case. It holds the user prompt and these graders:

| Grader | Type | Checks |
| --- | --- | --- |
| `case-criteria` | LLM judge | The case-specific "pass if / fail if" conditions |
| `honesty-and-approval` | LLM judge | No invented facts presented as true, no claim of posting or sending |
| `skill-fired` | tool check | The matching DevReach skill was actually loaded |
| `no-secret-echo` | regex | (some adversarial cases) secrets from the prompt are not repeated |

Agents in eval runs only get `Read`, `Glob`, `Grep`, and `Skill` — they cannot run commands, write files, or reach the network.

## Running

From the repository root, with Claude Code 2.1.296 or later:

```bash
# everything (48 cases, ~$10–20 of usage at default settings)
claude plugin eval . --scaffold --ablation none -j 6

# one skill
claude plugin eval . --scaffold --ablation none --tag project-to-post

# compare against Claude without DevReach (doubles the cost)
claude plugin eval . --scaffold --tag community-launch

# readable summary of the newest run, including the failed answers
python3 scripts/eval_summary.py
```

`--scaffold` is needed only for the `open-source-growth` cases. It runs `setup.sh`, which copies the fixture repository into the eval workspace. Read `setup.sh` before you run it, as with any script.

Results are written to `evals/results/<timestamp>/` (gitignored). Add a summary to [`RESULTS.md`](RESULTS.md) with `python3 scripts/eval_summary.py --markdown`.

## Limits of automated grading

- LLM judges are a cheap signal, not ground truth. Before you promote a skill to core, a person should read its outputs and score them with [`rubric.md`](rubric.md).
- Each case runs once by default (`runs: 1`). Model output varies; use `--runs 3` before you draw conclusions from a single failure or pass.
- The fixture and prompts are synthetic. Real users will find failures these cases miss. Please add them as new cases.
