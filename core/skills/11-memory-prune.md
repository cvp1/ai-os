---
name: memory-prune
order: 11
tier: core
---
   - /memory-prune — Keep memory healthy on demand: verify each memory is still true,
     fix drift, convert relative dates to absolute, rebuild MEMORY.md from the files
     (grouped, one line each), flag orphans and dangling [[links]], and PROPOSE
     deletions for my OK — never auto-delete. Keep a small ledger so it doesn't
     re-flag the same ones.
<!-- docs -->
## What it does
An on-demand health check for your memory — it verifies each memory is still true, fixes drift, rebuilds the index, and flags what's stale or orphaned, proposing deletions for your OK. It never auto-deletes.

## When to use it
Every so often as your memory grows, or when answers start feeling out of date. This is the maintenance half of the memory lifecycle — what keeps a long-lived memory *true* rather than just large.

## Walkthrough
1. Type `/memory-prune`.
2. It walks your memories: verifies each is still accurate, converts relative dates ("last week") to absolute, rebuilds the `MEMORY.md` index (grouped, one line each), and flags orphans and dangling `[[links]]`.
3. It **proposes** deletions for your approval — nothing is removed without your OK. A small ledger means it won't re-flag the same items next time.

A run looks about like this:

> **Memory check** · 84 memories
> · Fixed 6 relative dates → absolute · Rebuilt MEMORY.md index
> · 2 dangling links, 1 orphan flagged
> · Proposed for deletion (your OK): "trial ends Friday" (expired) · duplicate of [[acme-contact]]

## Power user
- **Propose-only, always.** `/memory-prune` never deletes on its own — you approve every removal. That's the deliberate trust posture.
- **`/improve` grows it, `/memory-prune` keeps it true.** One captures new rules; the other re-verifies, de-dupes, and fixes drift — the maintenance native memory doesn't do.
- **`/doctor` tells you when.** `/doctor` flags when your store has grown big enough that a prune is worth running.