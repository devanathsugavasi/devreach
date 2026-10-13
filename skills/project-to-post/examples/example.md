# Example: project-to-post

> This is an illustrative example with a fictional project. Names and numbers are made up for demonstration.

## Input

> Write a LinkedIn post about my project. It's called **ClassNotes AI** — a Chrome extension that takes a YouTube lecture and builds a timestamped study guide. Built it with a friend (Priya — she's fine being tagged) over 3 weekends. Uses the YouTube transcript API, chunks the transcript, and sends it to Claude to make section summaries with timestamps. Biggest problem: lectures over 2 hours blew past context, and summaries of chunks lost the thread. We fixed it by doing a first pass that builds an outline, then summarizing each chunk with the outline included. About 60 classmates installed it from our college group. Goal: get feedback and maybe some people outside my college to try it. Audience: students and devs.

## Clarifying questions

None needed — goal, audience, facts, and teammate consent are all supplied.

## Output

**Angle:** The decision — outline-first summarization. It's the most interesting technical choice and peers can learn from it.

**Hooks**
1. Summarizing a 2-hour lecture in chunks gave us a pile of accurate paragraphs and no idea what the lecture was about.
2. The fix for our AI study-guide extension wasn't a bigger context window. It was writing the outline first.
3. Three weekends, one Chrome extension, and a lesson about why chunked summaries lose the plot.

**Draft post**

Summarizing a 2-hour lecture in chunks gave us a pile of accurate paragraphs and no idea what the lecture was about.

Priya and I spent three weekends building ClassNotes AI, a Chrome extension that turns a YouTube lecture into a timestamped study guide.

The first version split the transcript into chunks and summarized each one. Short lectures were fine. Long ones fell apart: each summary was accurate on its own, but the guide had no structure and repeated itself.

What worked was a two-pass approach. First, we ask the model for an outline of the whole lecture. Then each chunk is summarized *with that outline included*, so the model knows where it is in the lecture and what's already been covered.

About 60 classmates installed it from our college group.

Next we want to test it on lectures outside our college's courses. If you watch long technical lectures on YouTube, I'd love for you to try it and tell me where the outline gets it wrong.

Link in the comments.

**Suggested call to action:** Ask readers who watch long lectures to try it and report where the outline is wrong.

**Claims to verify before posting**
- "About 60 classmates installed it" — confirm the number is current before posting.
- "Link in the comments" — add the Chrome Web Store or GitHub link in the first comment.
- Tag Priya using her LinkedIn profile so she gets credit.

**Optional:** Hashtags: #ChromeExtension #LLM #BuildInPublic
