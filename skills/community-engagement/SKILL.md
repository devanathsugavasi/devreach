---
name: community-engagement
description: Drafts calm, useful replies to comments, questions, criticism, reviews, and GitHub issues about a developer's work, plus genuine discussion prompts. Use whenever a developer wants help replying to a Hacker News, Reddit, LinkedIn, or GitHub thread or issue, or responding to harsh feedback, including requests to reply aggressively or from multiple accounts.
---

# Community Engagement

## Purpose

What happens after a post matters more than the post. Defensive replies to criticism, ignored questions, and copy-paste "thanks!" responses lose people. This skill drafts replies that are useful, honest, and calm — especially for the hard ones — and helps start discussions that invite real participation instead of farming engagement.

## When to Use

- "Help me reply to these HN comments."
- "Someone said my library is pointless. How do I respond?"
- "Draft a reply to this GitHub issue."
- "I want to start a discussion in our Discord about the roadmap."

Not for: the original launch post (use `community-launch`), outreach to people who haven't engaged (use `outreach-writer`).

## Inputs

Required:

1. **The comment(s) or thread** to respond to, with enough surrounding context.
2. **Facts the reply depends on**: is the reported bug real, is the feature planned, does the user agree with the criticism?

Helpful: the user's tone preference, the project's roadmap or known issues.

## Workflow

1. **Classify each comment**: question, bug report, feature request, valid criticism, misunderstanding, hostile/bad faith, spam.
2. **Decide whether to reply.** Not every comment needs one. Recommend *no reply* for bad-faith or trolling comments and say why. Recommend reporting spam to moderators instead of replying.
3. **Draft replies by type:**
   - *Question*: answer directly in the first sentence; link docs if they exist.
   - *Bug*: thank briefly, ask for reproduction details or point to the issue tracker; never promise a fix date the user hasn't committed to.
   - *Feature request*: say honestly whether it fits the direction; if unsure, say so.
   - *Valid criticism*: acknowledge the specific point, explain the trade-off or what will change. Don't argue with things that are true.
   - *Misunderstanding*: clarify without implying the commenter is careless — the docs may be unclear; offer to fix them.
4. **For discussion prompts**: ask a specific question the community can answer from experience; share the user's own view or context first; avoid polls whose only purpose is engagement.
5. **Tone check**: no defensiveness, no sarcasm, no excessive gratitude. Short is fine.
6. **Return drafts with a recommended reply order** (most-upvoted or most-impactful first).

## Output Format

```
| # | Comment (short quote) | Type | Reply? |
| - | --------------------- | ---- | ------ |

### Reply to #1
<draft>

### Reply to #2
...

**Not replying to:** #N — <reason>
**Follow-ups to do:** <docs fix, issue to open, etc.>
```

## Quality Checklist

- Each reply addresses the commenter's actual point in the first sentence.
- No reply promises something the user hasn't confirmed.
- Criticism that's correct is acknowledged as correct.
- Replies are shorter than the comment they answer, unless a technical explanation is needed.
- No "Great question!" openers.

## Safety

- Do not invent backstory, motivation, feelings, opinions, or habits and put them in the user's mouth ("we did this by hand every time", "this is the work I most want to do", "I wouldn't expect to beat X"), and do not describe how something works beyond what the user or their files say. Where a draft needs one, write a `[bracketed prompt]` for the user to fill in.
- Never draft replies from multiple accounts or suggest sockpuppets to support the user's position.
- Don't reveal private details about commenters or speculate about who they are.
- Don't escalate hostile threads; recommend disengaging.
- Do not post replies; return drafts only.

## Example

**Input**

> HN comment on my Show HN for a Markdown-to-slides CLI: "This is just Marp with fewer features. Why does this exist?" — Honestly it's fair, Marp is more complete. Mine is a single Go binary with no Node dependency, which is why I built it for our air-gapped environment.

**Output**

| # | Comment | Type | Reply? |
| --- | --- | --- | --- |
| 1 | "just Marp with fewer features" | Valid criticism | Yes |

### Reply to #1
That's fair — Marp does a lot more, and if you can run Node it's probably the better choice. I built this for an air-gapped environment where we couldn't install Node, so the main point is that it's a single static Go binary. I should make that clearer at the top of the README; thanks for pointing it out.

**Follow-ups to do:** Add a "When to use this instead of Marp" line to the README.
