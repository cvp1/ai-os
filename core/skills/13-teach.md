---
name: teach
order: 13
tier: core
---
   - /teach — A stateful tutor for learning a topic across many sessions. Keep a
     per-topic workspace in the vault (04 Resources/Learning/<topic>/) holding a
     syllabus, what we've covered, and where I struggled; each session resumes where
     the last ended, teaches the next piece, checks my understanding, and updates the
     progress file. Adapt depth to my level. Trigger on "/teach", "teach me X",
     "continue my <topic> lessons".
<!-- docs -->
## What it does
A stateful tutor for learning a topic over many sessions — it keeps a syllabus and your progress, and picks up each time exactly where you left off.

## When to use it
When you're learning something bigger than one sitting — a system, a skill, a subject — and want a course that remembers you rather than starting over each time.

## Walkthrough
1. Say *"/teach me system design"* (or *"continue my system-design lessons"*).
2. First time, it builds a syllabus and a per-topic workspace in your vault; after that it resumes where you left off, teaches the next piece, and checks your understanding.
3. It updates a progress file each session — what you've covered, where you struggled — and adapts the depth to your level.

A session looks about like this:

> **System design · session 4**
> Last time: caching, load balancing (you were shaky on cache invalidation)
> Today: consistent hashing → a quick check → then sharding
> Progress saved to 04 Resources/Learning/system-design/

## Power user
- **It remembers your struggles, not just your progress.** The progress file tracks where you wobbled, so it circles back instead of marching on.
- **Everything's a plain file.** The syllabus and progress live in your vault — edit the plan, or read back what you've learned, anytime.
- **Pairs with `/ingest` and `/recall`.** Turn course material into concept pages with `/ingest`; recall what you learned later with `/recall` or `/wiki`.