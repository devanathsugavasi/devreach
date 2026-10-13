---
name: outreach-writer
description: Drafts a short, personalized one-to-one message to a recruiter, hiring manager, open-source maintainer, potential collaborator, or founder, grounded in real shared context. Use when a developer wants to reach out to a specific person for a job, collaboration, contribution, or advice — not for bulk or templated outreach.
---

# Outreach Writer

## Purpose

Cold messages get ignored when they are long, generic, or ask for too much. They get answered when they show the sender did their homework, offer something relevant, and make a small, easy ask. This skill drafts one message to one person at a time, based on real context about both sides.

## When to Use

- "Help me message this recruiter about the backend role."
- "I want to ask the maintainer of X if they'd accept a PR for Y."
- "Write a LinkedIn note to a founder whose startup I like."
- "Follow up on a message I sent last week."

Not for: mass outreach, email campaigns, or "send this to 100 people" — this skill declines those (see Safety).

## Inputs

Required:

1. **Recipient**: who they are, role, and what the user knows about them (their post, project, talk, job listing — paste it).
2. **Sender's relevant context**: the 1–2 facts that make the user relevant to this person.
3. **The ask**: what the user wants (a call, a referral, feedback, permission to contribute).
4. **Channel**: LinkedIn connection note (≤ 300 chars), LinkedIn message, email, GitHub issue/discussion, X DM.

## Workflow

1. **Check the ask is proportionate.** A stranger can reasonably be asked for a short reply, a pointer, or permission — not a referral or an hour of their time. If the ask is too big, suggest a smaller first ask.
2. **Find the genuine connection.** One specific, true reason this person and not someone else: their post, a project, a shared community, the job listing. If nothing specific exists, tell the user to find it first.
3. **Draft** to the channel's length: why them (1 sentence) → who you are, relevant part only (1–2 sentences) → the ask (1 sentence, easy to say yes or no to) → close. No attachments requested in the first message.
4. **Write a follow-up** to send after 5–7 business days if there is no reply — shorter, adds one new piece of value, and makes it easy to decline. Never more than one follow-up.
5. **Return for review.**

## Output Format

```
**Channel:** <...> (<length limit>)
**Connection used:** <the specific reason>
**Ask:** <the ask, and whether it's proportionate>

**Message**
<draft>

**Follow-up (send after 5–7 business days if no reply)**
<draft>

**Before sending, check:** <facts to verify about the recipient>
```

## Quality Checklist

- The first sentence could only be written to this recipient.
- Message fits the channel limit.
- Exactly one ask, and it's small.
- No flattery that isn't specific ("I love your work" → which work, and why).
- No claims about the sender that aren't in their input.

## Safety

- Decline requests for mass or templated outreach, scraping contact details, or sending the same message to many people. Offer to help write one strong message instead.
- Do not guess or look up personal email addresses or phone numbers. Use channels the recipient has made public for professional contact.
- Do not impersonate anyone or imply a relationship that doesn't exist ("X suggested I contact you" unless true).
- Never send the message. The user sends it.

## Example

**Input**

> Recipient: maintainer of `fastapi-pagination`-style library (I'll call it `pagekit`). Their README says "cursor pagination for SQLAlchemy 2.0 is on the roadmap". I implemented cursor pagination for SQLAlchemy 2.0 in my company's internal fork last month (can share the approach, not the code). Ask: would they accept a PR? Channel: GitHub Discussion.

**Output**

**Channel:** GitHub Discussion (no hard limit; keep it under 150 words)
**Connection used:** Their roadmap item for SQLAlchemy 2.0 cursor pagination.
**Ask:** Whether a PR would be welcome and any design constraints — proportionate.

**Message**
Title: Interest in contributing SQLAlchemy 2.0 cursor pagination

Hi! The README lists cursor pagination for SQLAlchemy 2.0 as planned. I recently implemented this for an internal project (keyset pagination on `(created_at, id)` with opaque base64 cursors) and would like to contribute a clean implementation to pagekit.

Before I start: would you accept a PR for this, and are there design constraints I should follow — e.g. cursor format, or how it should fit with the existing `Page` class?

Happy to open a draft PR with just the interface first so you can comment early.

**Follow-up**
Not needed for a GitHub Discussion — maintainers see these on their schedule. If there's no response in a few weeks, check whether the repo is still active before starting the work.

**Before sending, check:** The roadmap item is still listed and no one has an open PR for it.
