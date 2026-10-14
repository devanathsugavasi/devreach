## What does this change?

<!-- One or two sentences. Link the issue if there is one: Closes #123 -->

## Type

- [ ] New skill
- [ ] Improvement to an existing skill
- [ ] Example or evaluation case
- [ ] Docs / tooling

## Checklist

- [ ] `python3 scripts/validate_skills.py` passes
- [ ] `python3 scripts/check_links.py` passes
- [ ] `python3 -m unittest discover -s tests` passes
- [ ] For skill changes: I ran `claude plugin eval . --tag <skill> --ablation none` and describe the results below
- [ ] No secrets, personal data, or real customer/employer information in examples
- [ ] The skill never publishes, posts, or sends anything without explicit user approval

## Evaluation notes

<!-- Which cases did you run? What did the output do well or badly? Paste short excerpts if useful. -->
