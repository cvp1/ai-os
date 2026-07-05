---
name: capture
order: 18
tier: core
---
   - /capture — At the END of a session that mattered, distill what was DECIDED and
     LEARNED and route each piece to the right brain: durable rules and preferences →
     my memory (the /improve loop), durable decisions and knowledge → my notes vault.
     PROPOSE the vault note before writing it (show me the distilled decision, apply on
     my OK); memory rules follow the /improve contract. This is the write-back loop that
     keeps a working session from evaporating. Distinct from /improve (memory-only
     corrections) and /ingest (raw notes I drop in) — /capture is the both-brains
     session close. Trigger on "/capture", "capture this session", "write that back",
     "log this decision".
<!-- docs -->
## What it does
Turns the reasoning of a session you just finished into durable, routed knowledge — the rules and preferences into your memory, the decisions and what-you-learned into your notes vault — so a session that mattered doesn't evaporate when you close it.

## When to use it
At the end of a session where real thinking happened — a decision got made, an approach got chosen, you learned something worth keeping. `/improve` captures a correction into memory; `/ingest` files raw notes you drop in; `/capture` is the one that closes a whole working session across both brains. Everything stays in plain files you own; nothing leaves your machine.

## Walkthrough
1. When you finish a session worth keeping, type `/capture` (or say *"write that back"*).
2. It distills what was decided and learned, and sorts each piece: memory rules vs a vault decision note.
3. It *proposes* the vault note for your OK before writing it; memory rules follow the `/improve` contract. Both stores stay yours to edit.

## Power user
- **`/capture` vs `/improve`.** `/improve` is the fast, memory-only "bake that in" for a single correction. `/capture` is the both-brains session close — use it when a session produced a decision worth a durable note, not just a preference.
- **Propose-first on the vault.** It never silently writes a decision note — you see the distilled version and approve it. Your vault stays yours.
- **It pairs with `/recall`.** What `/capture` files, `/recall` finds later — the write-back and read-back ends of the same knowledge loop.
