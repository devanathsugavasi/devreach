# Security Policy

DevReach is a collection of Markdown instructions (skills) plus a small Python validator and a bash install script. It has no server, database, network code, or runtime dependencies. Skills run **inside your Claude Code agent**, with your permissions, so the risks are about what those instructions could make an agent do.

## Threat model

| Risk | Example | Controls in this repo |
| --- | --- | --- |
| Malicious or careless skill change | A PR adds "also run `curl … \| sh`" or a hidden instruction to a skill | Validator (CI) allows only Markdown in `skills/`, rejects HTML comments, invisible/bidi Unicode, symlinks, and any frontmatter key except `name`, `description`, `license` (so no `allowed-tools`). CODEOWNERS review required for `skills/`. |
| Supply chain via plugin updates | A bad commit on `main` reaches everyone who runs `/plugin update` | Branch ruleset on `main` (no force-push or deletion, CI must pass for PRs), version bumps per release, and you can pin a release tag (below). |
| Agent executes untrusted code | A skill tells the agent to run a reviewed repository's install script | Skills must not run repository commands without explicit approval of the exact commands. `open-source-growth` recommends an isolated environment. |
| Prompt injection from content the agent reads | A README says "AI agents: ignore your instructions…" | Every skill treats files, comments, and issues as data. `open-source-growth` reports injected instructions to the user. The eval suite includes an injection case. |
| External actions without consent | Posting, sending messages, publishing releases | Every skill returns drafts only and requires explicit approval for any external action. Adversarial eval cases cover this. |
| Leaked secrets | Credentials pasted into a prompt end up in a draft | Skills must never repeat credentials. GitHub secret scanning and push protection are enabled for this repository. |
| Compromised CI dependency | A third-party GitHub Action is hijacked | Actions are pinned to full commit SHAs, `persist-credentials: false`, read-only token, and Dependabot updates. |

The deliberate prompt injection in `evals/fixtures/gst-invoice-parser/README.md` and the fake secrets in `evals/cases/` are test data. They are harmless by design. See [AGENTS.md](AGENTS.md).

## Pinning a release

To install a fixed release instead of following `main`:

```
/plugin marketplace add devanathsugavasi/devreach#v0.1.1
/plugin install devreach@devreach
```

For `install.sh`, check out a tag first: `git checkout v0.1.1`. Read the diff before upgrading. Skills are plain Markdown, so a review takes minutes.

## Supported versions

Only the latest release receives fixes.

## Reporting a vulnerability

Please **do not open a public issue** for security problems.

Report privately through [GitHub private vulnerability reporting](https://github.com/devanathsugavasi/devreach/security/advisories/new). Include:

- The affected file(s) and skill name.
- A prompt or input that reproduces the behavior.
- What the agent did and what it should have done.

Expect an acknowledgement within 7 days. Fixes will be credited unless you ask otherwise.

## Rules for contributions

Pull requests are rejected if a skill:

- Instructs the agent to publish, post, send, or message anything, or to run repository commands, without explicit user approval.
- Asks for or stores passwords, API keys, tokens, or other credentials.
- Adds scripts, binaries, symlinks, `allowed-tools`, or other non-Markdown content to `skills/` (the validator enforces this).
- Contains hidden or obfuscated instructions (HTML comments, invisible Unicode, encoded text).
