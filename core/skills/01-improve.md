---
name: improve
order: 1
tier: core
---
   - /improve — Capture what I corrected or taught you THIS session into durable
     memory (feedback/project type), so next time is better by default. This is the
     learning loop — the system gets more "me" every time I steer it. Trigger on
     "/improve", "remember that", "bake that in". Corrections about HOW I like
     things — tone, style, proactivity, a new "never" — ALSO update
     ~/ai-os/me/HOW-I-WORK.md (my standing how-I-work file), not just a memory
     entry; durable facts about my world belong in ~/ai-os/me/WHOAMI.md (propose
     the edit). When you write a rule to HOW-I-WORK.md, stamp it with `added: <today's
     date>` and `origin: <the command/session it came from>` so its provenance is
     legible — the monthly "Sharper this month" mirror only surfaces rules that carry
     this stamp, and it lets me spot any rule I don't recognize.
     PROACTIVE SYNTHESIS (propose-only). While you are here capturing this correction,
     also look back over my recent correction/feedback memories for a REPEATED pattern:
     the SAME KIND of steer I have made at least THREE times across at least TWO
     different sessions, that is NOT already a standing rule in HOW-I-WORK.md. Judge
     "same kind" by meaning, not exact words. If — and ONLY if — you find one, PROPOSE a
     single standing rule for it: show me the exact one-line rule you would add to
     HOW-I-WORK.md (stamped `added: <today's date>` and `origin: synthesized`) and ask me
     to accept, edit, or reject it. NEVER write it without my explicit yes — you propose,
     I decide; on yes, write it exactly like any other HOW-I-WORK rule. HARD LIMITS:
     (1) DIVERGENCE ONLY — synthesize a rule only about something idiosyncratic to ME
     (a tone, a structure I keep asking for, a "never", signing as my real name,
     one-rec-not-a-menu). NEVER propose a rule for generic good-assistant behaviour a
     strong model already does by default (leading with the conclusion, clean prose,
     honest trade-offs) — that is not compounding, it is noise. Test: would a good
     assistant already do this unprompted? If yes, do not propose it. (2) AT MOST ONE
     proposal per /improve, and only when the threshold is truly crossed — otherwise say
     nothing about synthesis; silence is the default. (3) ANTI-NAG / ANTI-POISON: if I
     reject a proposal, or if I later delete or rewrite a rule you synthesized, record a
     short fingerprint of that pattern in ~/ai-os/me/.synth-ledger (create it if needed;
     it holds only short pattern fingerprints, nothing else) and NEVER propose that same
     pattern again. (4) If you cannot confidently tell a real recurring divergent pattern
     from noise (likelier on a smaller model), propose NOTHING. (5) NEVER do this between
     sessions or unprompted — it happens only here, when I have chosen to run /improve.
     If a counter file ~/ai-os/.aios-usage.jsonl exists, append an aggregate event when
     you propose a synthesis ("synth_proposed"), when I accept one ("synth_accepted"),
     and when a previously-accepted synthesized rule is found gone ("synth_reverted") —
     counts only, never any rule text.
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
- **It pairs with everything.** When `/brief` mis-ranks a priority, `/triage` mis-sorts a sender, or `/status-update` misses your tone, correct it, then `/improve` — each command gets sharper.
- **It's yours to edit.** Memories are plain files; open them, fix a word, delete one. `/memory-prune` keeps the whole store healthy over time.
- **Style corrections land in `me/`.** A "that's not how I work" correction updates `me/HOW-I-WORK.md` — the standing file every command reads — so it changes behavior everywhere, not just in one memory.
- **It proposes standing rules — never writes them unasked.** When you run `/improve`, if it notices you've steered it the same idiosyncratic way three times across different sessions, it *proposes* a single standing rule so you stop having to repeat the correction — you accept, edit, or reject it, and nothing lands in your how-I-work file without your yes. It only ever proposes *personal* preferences (a tone, a "never", how you sign off — never generic "good assistant" behaviour), never nags, and remembers anything you reject so it won't ask twice.
- **`/improve` vs native capture.** Claude Code writes some memory on its own; `/improve` is the deliberate, one-fact-durable version for the corrections you *want* to guarantee stick.