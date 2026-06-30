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