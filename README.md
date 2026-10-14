# DevReach

**Build something great. Help the right people discover it.**

DevReach is an open-source collection of [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) skills that help developers explain their work, launch projects, write useful content, and grow communities — using real evidence, not hype.

[![Validate](https://github.com/devanathsugavasi/devreach/actions/workflows/validate.yml/badge.svg)](https://github.com/devanathsugavasi/devreach/actions/workflows/validate.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

---

## The problem

Building the project is half the work. The other half — explaining it, getting it in front of the right people, and turning users into contributors — is where most developer projects stall.

AI tools make this worse when they generate the same hype-filled post for every platform, invent numbers, and encourage spam. DevReach takes the opposite approach:

| Typical AI content generator | DevReach |
| --- | --- |
| Writes a generic post | Extracts your project's actual story |
| Same text for every platform | Adapts to each platform and audience |
| Fills gaps with invented claims | Flags unknowns and asks you |
| Optimizes for volume | Optimizes for usefulness and credibility |
| Posts or sends automatically | Returns drafts — **you** decide what goes out |

## Skills

Each skill is a folder with a `SKILL.md` that Claude Code loads when your request matches it.

**Status:** *Core* skills were built first and have full worked examples; *experimental* skills are complete but less refined. Neither label means human-reviewed yet. See [Evaluation](#evaluation-and-limitations) for automated results per skill.

### Developer branding

| Skill | What it does | Status |
| --- | --- | --- |
| [`project-to-post`](skills/project-to-post/SKILL.md) | Turns a project, release, or hackathon result into an authentic post | Core |
| [`developer-profile`](skills/developer-profile/SKILL.md) | Rewrites LinkedIn headline/About, GitHub profile README, portfolio bio | Core |
| [`technical-storyteller`](skills/technical-storyteller/SKILL.md) | Turns a debugging story, decision, or migration into a technical article | Experimental |

### Content marketing

| Skill | What it does | Status |
| --- | --- | --- |
| [`content-planner`](skills/content-planner/SKILL.md) | Builds a content calendar sized to the time you actually have | Experimental |
| [`multi-platform-content`](skills/multi-platform-content/SKILL.md) | Adapts one idea for LinkedIn, X, Reddit, Mastodon, and video | Experimental |
| [`launch-announcement`](skills/launch-announcement/SKILL.md) | Release notes, announcement, demo script, and launch checklist | Experimental |

### Community and distribution

| Skill | What it does | Status |
| --- | --- | --- |
| [`community-launch`](skills/community-launch/SKILL.md) | Picks fitting communities and drafts a rule-aware post for each | Core |
| [`open-source-growth`](skills/open-source-growth/SKILL.md) | Audits README and contributor path; drafts CONTRIBUTING and good first issues | Core |
| [`community-engagement`](skills/community-engagement/SKILL.md) | Drafts calm, useful replies to comments, criticism, and issues | Experimental |

### Outreach and growth strategy

| Skill | What it does | Status |
| --- | --- | --- |
| [`outreach-writer`](skills/outreach-writer/SKILL.md) | One personalized message to one recruiter, maintainer, or founder | Experimental |
| [`audience-research`](skills/audience-research/SKILL.md) | Segments, positioning, and interview questions from real evidence | Experimental |
| [`growth-review`](skills/growth-review/SKILL.md) | Reads your metrics and feedback, recommends 1–3 experiments | Experimental |

## Requirements

- [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) (the only platform tested so far)
- Git
- Python 3.9+ only if you want to run the validator — the skills themselves need nothing

## Installation

### Option 1 — Claude Code plugin (recommended)

In Claude Code:

```
/plugin install devreach --marketplace devanathsugavasi/devreach
```

On Claude Code versions before 2.1.275, run these two commands instead:

```
/plugin marketplace add devanathsugavasi/devreach
/plugin install devreach@devreach
```

This installs all twelve skills. Plugin skills are namespaced, so they appear as `devreach:project-to-post` and so on. Update with `/plugin update devreach` and remove with `/plugin uninstall devreach`.

### Option 2 — install script (pick individual skills)

```bash
git clone https://github.com/devanathsugavasi/devreach.git
cd devreach
./install.sh                                # all skills → ~/.claude/skills
./install.sh project-to-post growth-review  # only these
./install.sh --project community-launch     # into ./.claude/skills of the current project
./install.sh --list                         # show available skills
```

Reinstalling a skill replaces that skill's folder, so local edits to it are lost. The script never touches skills that aren't part of DevReach.

### Option 3 — copy by hand

```bash
mkdir -p ~/.claude/skills && cp -R devreach/skills/project-to-post ~/.claude/skills/
```

Start a new Claude Code session after installing so the skills load.

### Removal

```bash
./install.sh --uninstall                    # remove all DevReach skills
./install.sh --uninstall project-to-post    # remove one
```

For plugin installs: `/plugin uninstall devreach`.

## Quick start

1. Install DevReach with either option above.
2. Open Claude Code in any project folder.
3. Ask:

   ```
   Help me write a LinkedIn post about this project. Read the README,
   find the most interesting engineering decision, and give me three
   hooks and one draft. Flag anything you couldn't verify.
   ```

4. Claude reads the repo, builds a fact sheet of verified vs. assumed details, asks about anything missing, and returns hooks, a draft, and a list of claims to check. Nothing is posted.

No project handy? Use the fictional one in [`examples/sample-project.md`](examples/sample-project.md).

## Before and after

> 🚀 Thrilled to announce my new open-source project quietlog! It's a game-changing Python library that leverages cutting-edge techniques to keep your logs secure. ⭐

becomes

> A Stripe key once ended up in our team's log service because of one `logger.info(request.url)`. That's why I built quietlog — a small Python library that removes secrets from log messages before they're written. […] The hard part wasn't detecting secrets; it was *not* detecting things that look like secrets.

Full examples: [`examples/before-and-after.md`](examples/before-and-after.md) · How the skills chain together for a launch: [`examples/launch-campaign.md`](examples/launch-campaign.md)

## Principles

Every skill follows the same rules:

- **Evidence only.** Separate verified facts from assumptions. Never invent metrics, users, awards, or experience.
- **Ask, don't guess.** Ask clarifying questions when essential information is missing.
- **Drafts, not actions.** Never post, send, publish, or change anything external without your explicit approval.
- **No spam.** No mass outreach, vote manipulation, engagement bait, or sockpuppets.
- **Protect secrets.** Keep credentials, internal URLs, and confidential data out of output.
- **Untrusted input.** Repository files, comments, and documents are treated as data, not as instructions.

## Evaluation and limitations

**Structural checks** run in CI on every push: frontmatter, required sections, links, eval-case layout, and the install script.

```bash
python3 scripts/validate_skills.py
python3 scripts/check_links.py
python3 -m unittest discover -s tests
```

**Behavioral checks** use Claude Code's built-in `claude plugin eval`. There are 48 cases, 4 per skill: normal, missing information, adversarial (false claims, leaked secrets, spam requests, prompt injection), and quality. LLM judges grade each one, and a tool check confirms the right skill actually loaded. See [`evals/README.md`](evals/README.md).

Latest recorded run (2026-10-14, one run per case, Sonnet judge): **34 of 48 cases passed every grader**. The matching skill loaded in all 48. Full numbers, run-to-run noise, and the failing cases are in [`evals/RESULTS.md`](evals/RESULTS.md). In short:

- Refusals hold up well. In runs 2 and 3, every adversarial case declined the unsafe part of the request (false claims, vote manipulation, mass outreach, publishing without approval, leaking secrets) and offered a legitimate alternative. `open-source-growth` also reported a hidden prompt injection in a README.
- The main remaining weakness is **embellishment**: drafts sometimes add plausible backstory, feelings, or explanations the user never gave. `project-to-post` and `technical-storyteller` are most affected.
- These are automated judges on synthetic prompts, run once each. Nobody has done a human review yet.

Known limitations:

- Tested with Claude Code only. Other agents that read `SKILL.md` may work but haven't been tested.
- Installing all twelve skills adds about 1,000 tokens to every Claude Code session for the skill descriptions. Full instructions load only when a skill is used.
- Skills can't see current community rules, platform algorithms, or your analytics. They work from what you provide and tell you what to verify.
- **Always review drafts before publishing.** The skills reduce made-up claims but don't eliminate them.

## Contributing

Contributions are welcome — especially evaluation runs and real-world examples. Read [CONTRIBUTING.md](CONTRIBUTING.md), then pick an issue labeled `good first issue` or [request a skill](https://github.com/devanathsugavasi/devreach/issues/new?template=skill_request.yml).

- [Roadmap](ROADMAP.md) · [Changelog](CHANGELOG.md) · [Support](SUPPORT.md) · [Security](SECURITY.md) · [Code of Conduct](CODE_OF_CONDUCT.md)

## License

[Apache License 2.0](LICENSE)
