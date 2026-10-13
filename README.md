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

**Status:** *Core* skills have full worked examples and were built first; *experimental* skills are complete but less refined. **No skill has recorded behavioral evaluation results yet** — see [Evaluation](#evaluation-and-limitations).

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

Clone the repository:

```bash
git clone https://github.com/devanathsugavasi/devreach.git
```

**Install one skill for all your projects** (personal skills live in `~/.claude/skills/`):

```bash
mkdir -p ~/.claude/skills && cp -R devreach/skills/project-to-post ~/.claude/skills/
```

**Install all twelve:**

```bash
mkdir -p ~/.claude/skills && cp -R devreach/skills/* ~/.claude/skills/
```

**Install for one project only** (shared with anyone who clones that project):

```bash
mkdir -p .claude/skills && cp -R /path/to/devreach/skills/project-to-post .claude/skills/
```

Restart Claude Code (or start a new session) so it picks up the new skills.

### Removal

```bash
rm -rf ~/.claude/skills/project-to-post
```

Replace the name for other skills, or use `.claude/skills/` for project installs.

### Updating

```bash
cd devreach && git pull && cp -R skills/project-to-post ~/.claude/skills/
```

## Quick start

1. Install `project-to-post` as above.
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

**Automated checks** verify structure only — frontmatter, required sections, and links:

```bash
python3 scripts/validate_skills.py
python3 scripts/check_links.py
python3 -m unittest discover -s tests
```

**Behavioral quality** is evaluated manually. Each skill has four cases in [`evals/cases/`](evals/cases/) (normal, missing information, adversarial, quality) scored with [`evals/rubric.md`](evals/rubric.md). As of v0.1.0, **no evaluation runs have been recorded** — passing the automated checks does not mean the outputs are good.

Known limitations:

- Tested with Claude Code only. Other agents that read `SKILL.md` may work but haven't been tested.
- Skills can't see current community rules, platform algorithms, or your analytics — they work from what you provide and tell you what to verify.
- Output quality depends on the model and on how much real detail you give.
- Skills reduce, but cannot eliminate, the chance of a model stating something unsupported. Always review drafts before publishing.

## Contributing

Contributions are welcome — especially evaluation runs and real-world examples. Read [CONTRIBUTING.md](CONTRIBUTING.md), then pick an issue labeled `good first issue` or [request a skill](https://github.com/devanathsugavasi/devreach/issues/new?template=skill_request.yml).

- [Roadmap](ROADMAP.md) · [Changelog](CHANGELOG.md) · [Support](SUPPORT.md) · [Security](SECURITY.md) · [Code of Conduct](CODE_OF_CONDUCT.md)

## License

[Apache License 2.0](LICENSE)
