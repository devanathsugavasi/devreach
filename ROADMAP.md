# Roadmap

This roadmap is a direction, not a promise. Priorities change based on what users report.

## v0.1 — Initial collection (current)

- [x] 12 skills, 4 marked core, 8 experimental
- [x] Validator, link checker, unit tests, CI
- [x] Claude Code plugin + marketplace manifests
- [x] `install.sh` for picking individual skills
- [x] 48 automated eval cases (`claude plugin eval`) and first recorded runs ([results](evals/RESULTS.md))
- [ ] Human review of every core skill's eval outputs with the [rubric](evals/rubric.md)
- [ ] Short demo recording

## v0.2 — Earn the "core" label honestly

- [ ] Run the suite with `--runs 3` so single noisy runs don't decide anything
- [ ] Run the baseline arm (with vs. without DevReach) and publish whether the skills beat plain Claude
- [ ] Collect feedback from at least 10 external testers
- [ ] Promote experimental skills that pass the automated graders and human review
- [ ] Merge or remove skills that overlap in practice

## v0.3 — Easier use

- [ ] Windows install script (PowerShell)
- [ ] Voice profile: a reference file of the user's writing samples that drafting skills read
- [ ] Document behavior with other agents that read `SKILL.md`, only after testing them

## Later / ideas

- Conference talk proposal skill
- Changelog-to-release-notes from a git range without a changelog
- Automated checks for banned clichés and unsupported numbers in outputs

Have an idea? Open a [skill request](https://github.com/devanathsugavasi/devreach/issues/new?template=skill_request.yml).
