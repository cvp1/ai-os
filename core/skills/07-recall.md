---
name: recall
order: 7
tier: core
---
   - /recall — The unified "what do I know about X?" front door: ONE query that
     searches my maintained memory, my notes vault, AND the work product of my
     other commands in a single pass and returns one ranked answer. This is the
     everything-at-once recall surface; /wiki stays for vault-only precedent + graph
     enrichment. Build it READ-ONLY — it never writes any store. RANK FAIRLY (the one
     real risk): the sources score on different scales, so a naive merge lets one
     drown out the others — score each source's hits, NORMALIZE within each source to
     0–1, then guarantee a minimum quota per source (default 2 from each) before
     filling the rest of the pack (default 8 total) by overall rank, so a cross-cutting
     question always shows every side. THIRD SOURCE — WORK PRODUCT: my other commands
     produce durable knowledge that lives in their own working folders, not in memory
     or the vault — a tracked list or pipeline, a strategy/decisions doc, dated
     research, profiles. Index these as a third source so a question like "what am I
     tracking?" finds them. Declare WHICH files to surface in a small manifest (a
     command folder + the files/globs worth recalling, each with a one-line label),
     and READ THEM LIVE at query time — never copy them into memory or the vault. This
     matters: a copy is a second writable source that drifts and goes stale; reading
     the file live means recall always reflects current state, the file stays the
     single source of truth, and the taxonomy is unchanged (memory = durable facts,
     vault = synthesis) — only recall's reach widens. Curate the manifest for
     knowledge (lists, decisions, strategy, research, profiles), NOT ephemeral reports
     or raw machine state; strip HTML to text, skip oversized dumps, and if the
     manifest is missing just drop this source so recall still spans memory + vault.
     RELATIONAL CONTEXT: after picking the top memory hits, expand them by
     their links — follow any [[slug]] links in the body and the MEMORY.md index
     grouping (and any typed relations in the frontmatter, if I keep them) to pull in
     directly-related memories as a separate "related" block, shown as context, not
     re-ranked; this gives relational depth the flat vault notes can't. ANSWER
     CONTRACT: ground the answer only in what was recalled; cite per source — vault
     claims as path > heading, memory facts as [[slug]], work product as
     command-folder/file (and treat work-product hits as LIVE current state, not
     durable precedent) — and end with an honest one-line "Gaps:" footer naming
     uncovered terms or stale notes the answer leaned on. Plain keyword matching is
     the right engine at this scale; leave a clear seam to swap in an embedding-based
     reranker later, but DON'T build that now. Trigger on "/recall", "what do I know
     about X", "search everything / all of it", "what am I tracking", "have I decided
     or noted anything about…".
<!-- docs -->
## What it does
One question — *"what do I know about X?"* — answered across all your knowledge at once: your maintained memory, your notes vault, and the work your other commands produce and keep (a tracked list, a strategy doc, research). Ranked together, cited, and honest about where you have gaps.

## When to use it
Any time you're sure you decided or noted something but can't find it, or you want the full picture before a meeting or a decision. It's strictly read-only — it never writes to any store.

## Walkthrough
1. Ask it plainly — *"/recall what am I tracking on the website redesign"* or *"have I decided anything about pricing?"*.
2. It searches all three sources in one pass — memory, vault, and your commands' work product — and **ranks them fairly** so no single source drowns out the others (each is scored, normalized, and guaranteed a minimum showing).
3. It returns one ranked answer with citations, pulls in directly-related notes as context, and ends with an honest **Gaps:** line naming what it couldn't cover.

A recall looks about like this:

> **What you know about "website redesign"**
> **Decision** · Ship the field guide as a second page — *[[field-guide-second-page]]*
> **Note** · Compare table below the fold — *04 Projects/Redesign > Layout*
> **Tracking (live)** · 11 command docs remaining — *product-backlog/BACKLOG.md*
> **Related** · Connector-auth refresh, mobile-nav QA
> **Gaps:** nothing recent on the privacy-page copy; the layout note is 3 weeks old

## Power user
- **`/recall` vs `/wiki`.** `/recall` spans everything — memory, vault, and command work product. `/wiki` is the vault-only deep dive with heading-level citations and graph enrichment. Reach for `/recall` first; drop to `/wiki` when you specifically want precedent from your notes.
- **Trust the "Gaps:" line.** It's deliberate honesty — if `/recall` leaned on a stale note or couldn't cover a term, it says so. Treat work-product hits (a tracked list, a pipeline) as *current state*, not settled precedent.
- **Widen its reach.** `/recall` reads a small manifest of which command folders and files to surface. As you add commands that produce durable knowledge, adding them to that manifest lets recall find them — read live at query time, never copied, so nothing goes stale.
- **It never changes anything.** `/recall` is read-only by design. If it surfaced something wrong or missing, fix the underlying note and run `/improve`; recall reflects it next time because it reads sources live.