---
name: multi-platform-content
description: Adapts one source idea, article, or announcement into distinct drafts for LinkedIn, X/Twitter threads, Reddit, Bluesky, Mastodon, and short-form video scripts, each fitting that platform. Use whenever someone wants to repurpose or cross-post existing content, turn an article into a thread or video script, or post the same thing to several platforms or subreddits.
---

# Multi-Platform Content

## Purpose

Copy-pasting one post everywhere performs badly: a LinkedIn post reads as spam on Reddit, and a Reddit post is too long for X. This skill takes one source and rewrites it for each platform's format, length, culture, and reader expectations — keeping the facts identical and the framing different.

## When to Use

- "Turn this blog post into a LinkedIn post and an X thread."
- "Adapt this announcement for Reddit and Mastodon."
- "Write a 60-second video script from this article."

Not for: creating the original idea from a project (use `project-to-post`), or deciding which communities to target (use `community-launch`).

## Inputs

Required:

1. **Source**: the article, notes, post, or idea.
2. **Target platforms** (ask which, if not stated; default suggestion: the two where the user is most active).

Helpful: the user's handle and voice samples per platform, links to include, the specific subreddit if Reddit.

## Workflow

1. **Extract the core.** From the source, write: the one-sentence point, 3–5 supporting facts, and the call to action. All drafts must stay within these facts.
2. **Apply the platform rules** from the table below.
3. **Draft each version independently.** Change the opening, structure, and tone — not just the length. Never start two drafts with the same sentence.
4. **Check consistency.** Facts, numbers, and links must match across every draft.
5. **Return all drafts together** for review.

| Platform | Length | What works | What to avoid |
| -------- | ------ | ---------- | ------------- |
| LinkedIn | 120–250 words | Personal story, lesson, line breaks | Hashtag walls, "Agree?" |
| X / Twitter | 1 post ≤ 280 chars, or thread of 3–7 | Specific claim first, one idea per post, code screenshot alt text | Thread numbering spam (🧵1/27), hooks with no payoff |
| Reddit | Varies by sub | Plain text, technical depth, honest limitations, answering "why should I care" | Marketing tone, emojis, link-only posts |
| Bluesky / Mastodon | ≤ 300 / ≤ 500 chars | Conversational, relevant hashtags on Mastodon (discovery depends on them) | Cross-posted X formatting |
| Short video (60 s) | ~140–160 spoken words | Show the thing in the first 3 seconds, one idea, on-screen captions | Long intros, reading a blog aloud |

## Output Format

```
**Core point:** <one sentence>
**Facts used:** <bulleted list>

### LinkedIn
<draft>

### X
<single post or numbered thread>

### Reddit (r/<sub>)
Title: ...
Body: ...

### <other platform>
...

### Video script (if requested)
| Time | Visual | Voiceover |
```

## Quality Checklist

- Every draft uses only the listed facts.
- Each draft fits its platform's length.
- No two drafts share an opening sentence.
- Reddit draft has no marketing language and states limitations.
- Links and numbers are identical across drafts.

## Safety

- Do not invent backstory, motivation, feelings, opinions, or habits and put them in the user's mouth ("we did this by hand every time", "this is the work I most want to do", "I wouldn't expect to beat X"), and do not describe how something works beyond what the user or their files say. Where a draft needs one, write a `[bracketed prompt]` for the user to fill in.
- Do not add claims that weren't in the source to make a platform version "punchier".
- Do not suggest posting identical content to multiple subreddits or using multiple accounts.
- Return drafts only; do not post or schedule.

## Example

**Input**

> Source: my blog post "I replaced Redis with SQLite for my side project's job queue" — key points: 1 user-facing app, ~2k jobs/day, removed one Docker service, used `BEGIN IMMEDIATE` transactions for locking, works fine for my scale, wouldn't do it past one server. Platforms: X, Reddit (r/selfhosted), LinkedIn.

**Output (abbreviated)**

**Core point:** For a single-server side project, SQLite handled a ~2k jobs/day queue and removed a Redis service.

### X
I replaced Redis with SQLite for my side project's job queue.

~2k jobs/day, one server, one less Docker container. Locking is a `BEGIN IMMEDIATE` transaction.

Would I do it with multiple servers? No. Write-up: <link>

### Reddit (r/selfhosted)
Title: Dropped Redis from my stack and used SQLite as a job queue — notes on where it works and where it won't
Body: Leads with the setup (single server, ~2k jobs/day), explains the locking approach, and spends a full paragraph on limits (single writer, no multi-node). Ends: "If you've run SQLite queues at higher volume, where did it break?"

### LinkedIn
Opens with the decision ("I removed a service from my stack this month"), frames it as a lesson about matching tools to scale, and closes by asking what others have simplified.
