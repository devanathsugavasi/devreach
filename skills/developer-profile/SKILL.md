---
name: developer-profile
description: Rewrites a developer's LinkedIn headline and About section, GitHub profile README, or portfolio bio using only real experience and projects. Use when someone wants their profile to be clearer to recruiters, collaborators, or clients, or is changing roles and needs to reposition what they already have.
---

# Developer Profile

## Purpose

Most developer profiles are either a list of technologies or a vague statement ("passionate about building scalable solutions"). Neither tells a reader what the person is good at or what they want next. This skill rewrites profile copy so that a specific target reader can tell, in under ten seconds, what this developer does, what evidence backs it up, and what they're looking for.

## When to Use

- "Rewrite my LinkedIn headline and About section."
- "Make my GitHub profile README better."
- "I'm moving from backend to ML — how should my profile read?"
- "Write a short bio for my portfolio site."

Not for: resumes (different format and rules), cover letters, or writing posts (use `project-to-post`).

## Inputs

Required — ask if missing:

1. **Current profile text** (or "I have none").
2. **Target reader**: recruiters for a role type, open-source collaborators, freelance clients, conference organizers.
3. **What they want next**: job type, collaboration, clients, or just visibility.
4. **Evidence**: 2–5 real projects, roles, or contributions — with links if public.

Helpful: resume, GitHub username (to read pinned repos), location/remote preference, things they *don't* want to be hired for.

## Workflow

1. **Audit the current copy.** Score it against three questions: Can a stranger tell (a) what this person does, (b) what proof exists, (c) what they want? Quote the weakest line for each.
2. **Choose a positioning statement.** One sentence: "<Role/specialty> who <does what> for <whom>, with proof in <evidence>." Offer two alternatives if the user's direction is ambiguous (e.g. "full-stack" vs "frontend-leaning").
3. **Map evidence to claims.** For each skill or specialty the profile will claim, point to the project or role that proves it. Drop claims with no evidence, or mark them "learning" if the user wants to signal direction honestly.
4. **Write each requested surface** with its own constraints:
   - **LinkedIn headline** (≤ 220 chars): role + specialty + one proof point or focus. Three options.
   - **LinkedIn About** (150–300 words): first two lines carry the positioning (they show before "see more"); then 2–3 short evidence paragraphs; then what they're looking for and how to reach them.
   - **GitHub profile README**: one-line intro, "What I'm working on", 3–6 pinned-project lines (name — what it does — tech), how to reach them. No stat-card widgets unless asked.
   - **Portfolio bio**: 50-word and 120-word versions, third person unless the user prefers first.
5. **Check keyword fit** for recruiter-targeted profiles: list the 5–10 terms a recruiter would search for this role and confirm each appears naturally once — only if the user actually has that skill.
6. **Return with a change summary** explaining the biggest changes and why.

## Output Format

```
**Audit**
- What you do: <clear / unclear> — "<weakest quote>"
- Proof: <clear / unclear> — "<weakest quote>"
- What you want: <clear / unclear> — "<weakest quote>"

**Positioning:** <one sentence>

**Evidence map**
| Claim | Evidence |
| ----- | -------- |

**<Surface 1>**
<copy>

**<Surface 2>**
<copy>

**What changed and why**
- ...

**Gaps** (things that would make the profile stronger if true and added)
- ...
```

## Quality Checklist

- The first line of every surface says what the person does, not how they feel about it.
- Every listed skill has a project, role, or contribution behind it.
- No buzzwords: "passionate", "rockstar", "ninja", "results-driven", "team player", "guru".
- Seniority words (senior, lead, expert) are used only if the user's experience supports them.
- Each surface fits its platform's length limit.
- A reader knows what action to take (hire, collaborate, contact).

## Safety

- Do not inflate titles, years of experience, team size, or impact.
- Do not list employers, clients, or projects under NDA unless the user confirms they can be named.
- Do not include personal phone numbers or home addresses; suggest a professional email or contact link.
- Do not change the user's profile directly — return copy for them to paste.

## Example

**Input**

> LinkedIn headline right now: "CS Student | Python | Java | C++ | ML Enthusiast | Open to opportunities". Final-year CS student. Built a crop-disease classifier (PyTorch, ~92% accuracy on PlantVillage test split, deployed on Hugging Face Spaces). Did a 3-month internship at a fintech startup writing Django APIs. Contributed two merged PRs to scikit-learn docs. Want ML engineering internships or new-grad roles. Rewrite headline and About.

**Output (abbreviated)**

**Audit**
- What you do: unclear — "ML Enthusiast" says interest, not ability.
- Proof: missing — no projects or results in the headline.
- What you want: clear but generic — "Open to opportunities".

**Positioning:** Final-year CS student building and deploying ML models, with production API experience from a fintech internship.

**Headline options**
1. CS final-year · Building and deploying ML models (PyTorch, Hugging Face) · Ex-intern backend dev (Django) · Seeking ML engineering roles 2027
2. ML engineering new grad 2027 · Shipped a crop-disease classifier to Hugging Face · scikit-learn docs contributor
3. Final-year CS student who ships ML, not just notebooks · PyTorch · Django · Open to ML engineering roles

**About** (first two lines)
> I build machine learning models and the APIs around them. My latest is a crop-disease classifier trained in PyTorch that reaches about 92% accuracy on the PlantVillage test split and runs publicly on Hugging Face Spaces.

**Gaps**
- A link to the Space and the repo in the Featured section.
- If the classifier was tested on real field photos, say how it performed — PlantVillage test accuracy alone overstates real-world performance, and ML reviewers know it.
