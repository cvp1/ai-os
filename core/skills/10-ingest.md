---
name: ingest
order: 10
tier: core
---
   - /ingest — Turn raw sources I drop into _inbox/ (clippings, transcripts,
     meeting/Teams exports, reading) into maintained, interlinked CONCEPT PAGES under
     04 Resources/Synthesis/ — synthesize once and navigate later instead of
     re-summarizing the same sources every time I ask. For each source: read it, then
     for each distinct concept create or UPDATE a short, cited Synthesis/<slug>.md
     (one idea per page) with [[wikilinks]] to sibling pages, rebuild the Synthesis
     index.md, and archive the raw source to _inbox/processed/. SAFETY FENCE: you
     write end-to-end ONLY inside 04 Resources/Synthesis/; everywhere else in the
     vault is propose-only — a link from one of my hand-authored notes into a concept
     page is a SUGGESTION you collect for my review, never an edit to my note.
<!-- docs -->
## What it does
Turns raw sources you drop in — clippings, transcripts, meeting or Teams exports, reading — into maintained, interlinked concept pages, so you synthesize once and navigate later instead of re-summarizing the same material every time.

## When to use it
When you've collected material you'll want to reuse — research, meeting exports, articles — and don't want a growing pile of unprocessed files. Safety fence: it writes end-to-end *only* inside your Synthesis folder; everywhere else in your vault it's propose-only (a link into one of your own notes is a suggestion for your review, never a silent edit).

## Walkthrough
1. Drop raw sources into your `_inbox/` folder.
2. Run `/ingest`. For each source it reads it, then for each distinct idea creates or updates a short, cited concept page (one idea per page) with `[[wikilinks]]` to sibling pages.
3. It rebuilds the Synthesis index and archives the raw source to `_inbox/processed/` — so your inbox stays clean and your knowledge stays linked.

A run looks about like this:

> **Ingested 3 sources → 5 concept pages**
> · New: *Synthesis/context-windows.md*, *Synthesis/rag-vs-finetune.md*
> · Updated: *Synthesis/agent-harness.md* (+2 links)
> · Archived raws → _inbox/processed/ · Rebuilt Synthesis/index.md
> Suggested 2 links into your hand-authored notes — review before applying.

## Power user
- **The safety fence is the point.** `/ingest` owns the Synthesis folder end-to-end but treats the rest of your vault as propose-only — your hand-written notes are never silently edited.
- **One idea per page.** Concept pages stay short and single-topic so they interlink cleanly and stay reusable — the opposite of a giant summary doc.
- **Feeds `/wiki` and `/recall`.** Everything `/ingest` builds becomes searchable precedent; the more you ingest, the richer those answers.