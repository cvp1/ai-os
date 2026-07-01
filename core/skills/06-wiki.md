---
name: wiki
order: 6
tier: core
---
   - /wiki — Precedent search over my notes vault: "what did I decide / write about
     X?", answered with path > heading citations. Read-only recall.
<!-- docs -->
## What it does
A precedent search over your notes vault — *"what did I decide or write about X?"* — answered with citations down to the exact note and heading.

## When to use it
When you want the deep dive into your own notes specifically: the reasoning behind a past decision, what you wrote on a topic. Read-only recall — it never edits your notes.

## Walkthrough
1. Ask *"/wiki the data-migration decision"* or *"what did I write about pricing?"*.
2. It searches your vault and returns the relevant passages, each cited as note > heading so you can open the source.
3. Follow the citations into your notes, or ask a follow-up to narrow.

A wiki answer looks about like this:

> **"data-migration decision"**
> · Chose phased cutover over big-bang — *02 Projects/Migration > Decision*
> · Rollback: keep the old DB read-only for 30 days — *02 Projects/Migration > Risk*
> · Related: the vendor SLA thread — *03 Areas/Vendors/Acme > SLA*

## Power user
- **`/wiki` vs `/recall`.** `/wiki` is vault-only, with heading-level precision and graph enrichment. `/recall` casts wider — memory, vault, and command work product at once. Use `/recall` for "what do I know?", `/wiki` for "what did I write?".
- **It's only as deep as your vault.** The more you capture (with `/ingest`, `/status`, plain notes), the more precedent it finds.
- **Read-only.** `/wiki` never changes a note. To turn raw sources *into* linked notes, that's `/ingest`.