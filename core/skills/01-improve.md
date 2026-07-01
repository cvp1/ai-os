---
name: improve
order: 1
tier: core
---
   - /improve — Capture what I corrected or taught you THIS session into durable
     memory (feedback/project type), so next time is better by default. This is the
     learning loop — the system gets more "me" every time I steer it. Trigger on
     "/improve", "remember that", "bake that in".
<!-- docs -->
## What it does
Turns a correction you just made into a durable rule, so the system doesn't repeat the same miss — the learning loop that makes it more "you" over time.

## When to use it
Right after you fix something — its tone, a wrong assumption, a formatting preference. Claude already jots down some corrections on its own; `/improve` is how you make the ones that matter stick deliberately. It writes to your own local memory (a plain file you own); nothing leaves your machine.

## Walkthrough
1. After you've corrected it in the conversation, type `/improve` (or say *"remember that"* / *"bake that in"*).
2. It captures what changed this session as a durable memory — a one-fact rule, tagged as a preference or a project fact.
3. Next time, that rule is in play by default. You can see and edit it — it's a plain file in your memory folder.

A capture looks about like this:

> **Learned this session**
> · Status updates: lead with the decision, not the backstory — *[[status-lead-with-decision]]*
> · "Acme" = Acme Robotics, not Acme Foods
> Saved to memory. These apply from your next session on.

## Power user
- **One fact per rule.** Small, specific rules beat big ones — easier to recall and to correct later.
- **It pairs with everything.** When `/brief` mis-ranks a priority, `/triage` mis-sorts a sender, or `/status` misses your tone, correct it, then `/improve` — each command gets sharper.
- **It's yours to edit.** Memories are plain files; open them, fix a word, delete one. `/memory-prune` keeps the whole store healthy over time.
- **`/improve` vs native capture.** Claude Code writes some memory on its own; `/improve` is the deliberate, one-fact-durable version for the corrections you *want* to guarantee stick.