<div align="center">

# 🧭 AI OS for Claude Code

**Turn [Claude Code](https://claude.com/claude-code) into a chief-of-staff that remembers your work, knows your calendar, and gets sharper every time you correct it.**

A persistent memory · a structured notes vault · a toolkit of slash-commands — all wired to your Microsoft 365, and built around *you* in about five minutes.

### [▶︎ Open the walkthrough →](https://cvp1.github.io/ai-os/)

</div>

---

## What this is

A single self-contained page (`index.html`) with an embedded, copy-paste **setup prompt**. You paste it into a fresh Claude Code session; it **interviews you** about your role, then builds a personal "AI operating system" shaped to how you actually work — and explains each piece in plain language as it goes.

No code. No config files to edit. If you can use Outlook, you can use this.

## Why you'd want it

- **It remembers.** Stop re-explaining your context every session — your engagements, stakeholders, and preferences persist and compound over time.
- **It's wired to your real work.** Commands read from your live Microsoft 365 (Outlook, calendar, Teams, SharePoint), not a generic chatbot guess.
- **It's in your hands.** Read-only by default — it drafts and proposes; nothing is sent, posted, or accepted without your explicit OK, every time.
- **It gets more "you."** Correct it once, run `/improve`, and the lesson sticks.

## Quickstart — about 5 minutes

| # | Step |
|---|------|
| 1 | Install **Claude Code** and sign in. |
| 2 | Connect the **Microsoft 365** connector in settings (the prompt can walk you through it). |
| 3 | Open a Claude Code session in a folder you want as your home — e.g. `~/ai-os`. |
| 4 | Open the [walkthrough](https://cvp1.github.io/ai-os/), copy the setup prompt, and paste it as your first message. |
| 5 | Answer the interview. Claude builds everything and tells you what to try first. |

## What gets built

**🧠 Persistent memory** — one-fact-per-file notes (`user` / `feedback` / `project` / `reference`) with an index that loads every session, interlinked and self-maintaining.

**📚 Notes vault** — an Obsidian-compatible PARA vault, plus an AI-owned `Synthesis/` zone that turns raw sources you drop in into maintained, linked concept pages.

**🛠️ A starter toolkit of commands:**

| Command | What it does |
|---------|--------------|
| `/brief` | Your morning brief — meetings, what's waiting on you, priorities, deadlines. |
| `/triage` | One pass over inbox + calendar → Needs Reply / FYI / Noise, conflicts flagged. |
| `/prep` | Preps you for one meeting — invite, thread, notes, decisions, likely questions. |
| `/status` | Drafts a status report — progress, RAG by workstream, risks, decisions needed. |
| `/raid` | Keeps a Risks / Assumptions / Issues / Decisions log current per engagement. |
| `/weekly` | Pre-builds your weekly review and a ready-to-edit status update. |
| `/wiki` | Precedent search over your own notes, answered with citations. |
| `/ingest` | Turns raw notes you drop in into maintained, linked concept pages. |
| `/improve` | The learning loop — captures your corrections into durable memory. |
| `/memory-prune` | Keeps memory healthy — verifies, de-dupes, proposes cleanups (never auto-deletes). |
| `/skill-center` | Build, edit, and audit your own commands as your needs grow. |

**⚡ Local-first Microsoft 365** — caches your calendar and mail locally and refreshes only when stale, so it's instant to use and won't trip Microsoft Graph throttling.

## Your control & privacy

- **Read-only by default.** It drafts and shows you; you approve before anything goes outward. Approving one action is never standing approval for the next.
- **Your data stays local.** Cached on your own machine; confidential material is treated as never-leaves-without-your-say.
- **Yours to shape.** The starter commands are a foundation — `/skill-center` adds and refines more as you go.

## A note before you connect a work account

This is a **personal-productivity template**, not an official product of any employer. If you're wiring it to a work mailbox, confirm with your leadership / IT that Claude Code with the Microsoft 365 connector is approved for your account first.

---

<div align="center">
<sub>Built &amp; shared by Craig Vandeputte · adapt it freely.</sub>
</div>
