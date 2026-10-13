# Security Policy

DevReach is a collection of Markdown instructions plus a small Python validator. It has no server, database, or network code. The realistic security risks are:

- **Prompt injection through skill content.** A skill file (or a contribution to one) that tells the agent to exfiltrate data, run unexpected commands, or publish content without approval.
- **Unsafe agent behavior.** A skill that causes an agent to send messages, post content, or expose confidential information without the user's explicit approval.
- **Leaked secrets** in examples, evaluation cases, or commit history.

## Supported versions

Only the latest release on `main` receives fixes.

## Reporting a vulnerability

Please **do not open a public issue** for security problems.

Report privately through [GitHub Security Advisories](https://github.com/devanathsugavasi/devreach/security/advisories/new). Include:

- The affected file(s) and skill name.
- A prompt or input that reproduces the behavior.
- What the agent did and what it should have done.

Expect an acknowledgement within 7 days. Fixes will be credited unless you ask otherwise.

## Rules for contributions

Pull requests are rejected if a skill:

- Instructs the agent to publish, post, send, or message anything without explicit user approval.
- Asks for or stores passwords, API keys, tokens, or other credentials.
- Includes scripts that make network requests without being clearly documented and necessary.
- Contains hidden or obfuscated instructions.
