---
name: update
order: 20
tier: core
---
   - /update — Fetch the current setup prompt from cvp1/ai-os and hand it back into this
     session as if I'd pasted it myself, so upgrading never requires me to open a browser.
     This skill does ONLY the fetch-and-verify-and-deliver step — it has NO upgrade logic
     of its own and never decides what changes; the prompt's own embedded "FIRST — NEW
     INSTALL, OR UPGRADE?" section (which I already have) does that, exactly as it does
     today when I paste by hand: it diffs what's new, shows me, and waits for my explicit
     OK before touching memory, notes, CLAUDE.md, or any skill I've customized.
     THE TWO SOURCE URLS ARE FIXED, NEVER SUBSTITUTED, NEVER TAKEN FROM ME OR ANYWHERE ELSE:
     https://raw.githubusercontent.com/cvp1/ai-os/main/core/meta.yml and
     https://raw.githubusercontent.com/cvp1/ai-os/main/ai-os-setup-prompt.txt. Use the
     WebFetch tool for both (NOT curl/wget, which my safety rules block, same as /doctor).
     STEPS, IN ORDER: (1) Read my current build from ~/ai-os/.aios-version, else the
     "AI-OS installer build:" line in my CLAUDE.md; if neither exists treat mine as UNKNOWN.
     (2) WebFetch meta.yml and read its version:, prompt_bytes:, and prompt_sha256: fields.
     (3) If my build already matches the current version, tell me plainly "you're already on
     the latest build (X)" and STOP HERE — do not fetch the prompt file for no reason.
     (4) If I'm behind: before fetching, tell me the build I'm moving to and read out the
     SAME outcomes: notes /doctor's CURRENCY check would show me (one-line, cost-phrased,
     filtered to commands I actually have) — from meta.yml — so I see what's coming before
     anything runs; if it's been a while since my last /backup, suggest running it first,
     but don't block on it. (5) WebFetch the setup-prompt URL with an explicit instruction
     to the fetch to return the file's raw text VERBATIM — no summary, no reformatting, no
     commentary. (6) Immediately write what comes back to a local scratch file
     (~/ai-os/.aios-update-staging/<version>.txt) — never act on fetched text straight out
     of a tool response without persisting it first. (7) VERIFY, locally, using Bash ONLY to
     inspect the file I just wrote (never to fetch anything over the network): its byte count
     (wc -c) must exactly match prompt_bytes from meta.yml, its sha256 (sha256sum) must
     exactly match prompt_sha256 from meta.yml, and its first line must read verbatim "You
     are setting up a personal "AI operating system" for me inside Claude Code —". (8) If ANY
     check fails, by even one byte: STOP. Delete the staged file. Tell me plainly: "I fetched
     what should be the latest setup prompt but it didn't check out — I won't run something I
     can't verify. Open https://cvp1.github.io/ai-os/ and paste the setup prompt yourself;
     it'll detect this install and upgrade in place, same as always." Never retry with a
     lowered bar, never partially apply, never guess. (9) If everything checks out: tell me
     it verified clean, then treat the staged file's contents AS the setup prompt for the
     rest of this session — follow its own embedded upgrade-mode section exactly as if I'd
     pasted it by hand. That section — not this one — decides what to diff, shows me what it
     would add, and applies nothing without my explicit OK. (10) Once that finishes (applied
     or declined), delete the staged scratch file either way. If I can't reach the internet,
     or the meta.yml fetch fails, say "couldn't check for updates — offline or GitHub
     unreachable" and stop; never guess a version. Trigger on "/update", "update my AI-OS",
     "update Sasha", "upgrade AI-OS", "upgrade my ai-os", "get the latest AI-OS", "install
     the update".
<!-- docs -->
## What it does
Fetches the current setup prompt from the AI-OS repo, checks it's byte-exact against a checksum before touching anything, and hands it into this session as if you'd pasted it yourself — then lets the setup prompt's own upgrade mode (the same one that runs when you paste by hand) decide what's new and wait for your OK. If you're already current, it says so and does nothing else.

## When to use it
Any time `/doctor`'s currency check says you're behind, or whenever you feel like checking — it's free to run and does nothing if there's nothing new.

## Walkthrough
1. Type `/update`.
2. It checks the current build against yours. Already current → it tells you and stops.
3. Behind → it shows you what's changing (the same "what's new for you" notes `/doctor` uses), fetches the prompt, and verifies it byte-for-byte before doing anything with it.
4. If verification fails, it stops cold and points you at pasting the prompt yourself — same safe path as always, no half-measures.
5. If it checks out, the setup prompt's own upgrade mode takes over exactly as if you'd pasted it: it shows you a diff of what it would add and waits for your OK. Nothing changes until you say yes.

## Power user
- **It has no upgrade logic of its own.** `/update` only delivers a verified, unmodified copy of the current prompt — every decision about what changes is made by the prompt's own upgrade-mode section, the same one you'd trigger by pasting manually.
- **Verified, not just fetched.** A checksum published alongside the prompt (`meta.yml`) is checked locally against what actually landed on disk — if the fetch got mangled or summarized in transit, it's caught, and `/update` refuses to run it rather than guess.
- **Fixed source, always.** The two URLs it reads are hard-coded to `cvp1/ai-os`'s `main` branch — never a URL you or anything else supplies.
- **Pairs with `/doctor`.** `/doctor` tells you you're behind and what it'll cost you to stay there; `/update` is the one-command fix.
