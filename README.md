<div align="center">

# 🧭 AI OS for Claude Code

**Turn [Claude Code](https://claude.com/claude-code) into a chief-of-staff — the person who runs the day around you — that remembers your work, knows your calendar, and gets sharper every time you correct it.**

A persistent memory · a structured notes vault · a toolkit of slash-commands — wired to your **Google (Gmail + Calendar) or Microsoft 365**, and built around *you* in about five minutes.

### [▶︎ Open the walkthrough →](https://cvp1.github.io/ai-os/)

</div>

---

## Why this exists

AI-OS started as a favor. I kept building these setups by hand for people I know — a friend who'd never opened a terminal, then a couple of colleagues — and doing it one at a time made the point obvious: the hard part was never *building* it. The capability is already here, sitting inside tools people already pay for; it's just locked behind knowing how to wire it up. The barrier is **access, not capability.** So I compressed the whole thing into one prompt anyone can paste and run — **a personal AI that's genuinely yours, that anyone can stand up.** Plain files on your machine, free to fork, on your side by default. It should belong to *you* — not to a platform, and not just to people who can code.

## What this is

A single self-contained page (`index.html`) with an embedded, copy-paste **setup prompt**. You paste it into a fresh Claude Code session; it **interviews you** about your role, then builds a personal "AI operating system" shaped to how you actually work — and explains each piece in plain language as it goes.

No code. No config files to edit. If you can use email and a calendar, you can use this.

## Why you'd want it

- **It keeps your memory true.** Claude Code remembers across sessions — this keeps that memory honest: it re-checks what's gone stale, removes duplicates, resolves contradictions, and links related facts, so what it knows about your projects and people stays trustworthy instead of drifting.
- **It's wired to your real work.** Commands read from your live mail & calendar — Google (Gmail + Calendar) or Microsoft 365 — not a generic chatbot guess.
- **It's in your hands.** Read-only by default — it drafts and proposes; nothing is sent, posted, or accepted without your explicit OK, every time.
- **It gets more "you."** Correct it once, run `/improve`, and the lesson sticks.

## Yours, not rented

Most "AI second brain" tools are hosted apps — your notes live in their cloud, for as long as you keep paying. An AI-OS is the opposite: a free template you copy, run on tools you already use, and reshape to fit you.

| | AI-OS | Hosted second-brain apps (Saner / Mem / Tana / Notion) | Native LLM memory (ChatGPT / Claude) |
|---|---|---|---|
| Where it lives | Notes & memory are local files¹ | Their cloud | Their cloud, tied to your account |
| Your data's form | Plain markdown — the store *is* the data | Proprietary DB you export *from* | A cloud summary you can view/edit |
| Own & fork it | Free template — fork & reshape | Rented seat | Rented seat |
| On its own | Reads & drafts; every outward action waits for your per-action OK — on by default, no mode to switch on (on M365 the connector is read-only outright) | Varies (Notion's agents act autonomously by default) | n/a — it's memory, not actions |
| Cost | Free; runs on your existing Claude plan | Paid subscription | Bundled in your subscription |

¹ Your notes & memory are local files; the model and connectors are cloud services you already use.
Every tool here lets you *export* — the difference is yours is *already* plain files. Details
as-of July 2026; verify before relying on them.

## Quickstart — about 5 minutes

| # | Step |
|---|------|
| 1 | Install the **Claude desktop app** from [claude.com/download](https://claude.com/download) and sign in — no terminal, no code. *(It runs on a paid Claude plan — Pro is ~$20/mo. This template is free; the AI that powers it isn't.)* |
| 2 | Connect your mail & calendar: at [claude.ai](https://claude.ai) → Settings → Connectors, turn on **Google (Gmail + Calendar)** *or* **Microsoft 365** — the [walkthrough](https://cvp1.github.io/ai-os/) covers the fine print (personal Gmail works; M365 needs a work account). |
| 3 | In the app, open the **Code** tab and create or pick a home folder — e.g. a new folder called `ai-os`. Then **switch the session to Auto mode** (top-left, just above where you type; accept the one-time dialog) *before* you paste. |
| 4 | Open the [walkthrough](https://cvp1.github.io/ai-os/), copy the setup prompt, and paste it as your first message. |
| 5 | Answer the interview. Claude builds everything and hands you your first morning brief — your day, from your real mail and calendar. |

*Prefer a terminal? The [Claude Code CLI](https://claude.com/claude-code) is the same engine — every step above works there too.*

## What gets built

**🧠 A maintained memory** — a clean one-fact-per-file structure (`user` / `feedback` / `project` / `reference`) over Claude Code's built-in memory, that actively keeps itself healthy: re-verifies stale facts, de-dupes, resolves contradictions, and grows the sources you drop in into interlinked concept notes — legible, trustworthy, and yours to edit.

**📚 Notes vault** — an Obsidian-compatible PARA vault, plus an AI-owned `Synthesis/` zone that turns raw sources you drop in into maintained, linked concept pages.

**🛠️ A starter toolkit of commands:**

| Command | What it does |
|---------|--------------|
| `/brief` | Your morning brief — meetings, what's waiting on you, priorities, deadlines. |
| `/triage` | One pass over inbox + calendar → Needs Reply / FYI / Noise, conflicts flagged. |
| `/prep` | Preps you for one meeting — invite, thread, notes, decisions, likely questions. |
| `/status` | Drafts a status update — what progressed, what's blocked, decisions needed, next steps. |
| `/weekly` | Pre-builds your weekly review and a ready-to-edit status update. |
| `/wiki` | Precedent search over your own notes, answered with citations. |
| `/recall` | "What do I know about X?" — one search across **all** your knowledge: your memory, your notes vault, and the work your other commands produce and keep (a tracked list, a strategy doc, research) — ranked together, with related facts and an honest gaps note. |
| `/ingest` | Turns raw notes you drop in into maintained, linked concept pages. |
| `/improve` | The learning loop — captures your corrections into durable memory. |
| `/memory-prune` | Keeps memory healthy — verifies, de-dupes, proposes cleanups (never auto-deletes). |
| `/skill-center` | Build, edit, and audit your own commands as your needs grow. |
| `/board` | Run a decision past a panel of advisor profiles — distinct takes, dissents, a recommendation. |
| `/teach` | A stateful tutor — keeps a syllabus and your progress across sessions. |
| `/workflow-visualizer` | Turns a system you describe into one interactive HTML diagram. |
| `/backup` | Snapshots your whole system — memory, notes, **and** skills — to on-disk history plus an **encrypted** copy in your own cloud (3-2-1), no setup needed. |
| `/restore` | Brings it all back from a snapshot — newest by default, fully reversible, with a `--drill` that proves a backup works without touching your live system. |
| `/doctor` | A read-only checkup — are your connectors signed in, your memory and commands healthy, your last `/backup` recent? Reports what needs attention and points you at the fix; never changes anything. |

**Want more from each command?** The **[Field Guide](https://cvp1.github.io/ai-os/guide.html)** covers every one — what it does, when to reach for it, a walkthrough, and the power-user moves.

**⚡ Local-first by design** — caches your calendar and mail locally and refreshes only what changed (Graph delta / Gmail history), so it's instant to use and won't trip rate limits.

## Once it's running

Two opt-in "second acts" wait past your first win — each is one more paste on the [walkthrough](https://cvp1.github.io/ai-os/):

- **Put it on a schedule** — a morning brief drafted and waiting, run locally in Ask mode so nothing is ever sent while you're away. → [scheduler](https://cvp1.github.io/ai-os/#autopilot)
- **Hire a domain manager** — a standing chief-of-staff for one part of your life: **career** (drafts LinkedIn posts in your voice), **projects** (drafts the status update you actually send), **learning** (plans what to learn; `/teach` teaches). → [staff your bench](https://cvp1.github.io/ai-os/#domain)

## Your control & privacy

- **Read-only by default.** It drafts and shows you; you approve before anything goes outward. Approving one action is never standing approval for the next.
- **Local — and recoverable.** Your data lives on your own machine; confidential material is treated as never-leaves-without-your-say. The one thing that can leave is a backup *you* ask for — encrypted, to your own cloud — so a lost laptop never means a lost system.
- **Yours to shape.** The starter commands are a foundation — `/skill-center` adds and refines more as you go.

## The principles behind it

A few rules shape every command — the same ones, whatever you wire it to:

- **Propose, don't act.** It drafts and recommends; you approve. The safe, reversible direction can be automatic — anything outward-facing or hard to undo waits for your OK.
- **Earn trust, don't assume it.** It leads with what it's unsure of, checks the real source instead of a cached "looks fine," and tells you when something's stale.
- **Signal over noise.** It surfaces what changed and what needs you, and stays quiet when nothing does.
- **Remember, then improve.** Your context persists and compounds; a correction you make once becomes a durable rule, not a lesson you repeat.
- **Local-first, recoverable, yours to shape.** Your data stays on your machine, secrets stay out of the conversation, every piece is a small tool you can read, edit, or replace — and `/backup` keeps an encrypted copy in your own cloud so it all survives a lost machine.

## A note before you connect a work account

This is a **personal-productivity template**, not an official product of any employer. If you're wiring it to a work mailbox, confirm with your leadership / IT that Claude Code with the Microsoft 365 or Google Workspace connector is approved for your account first.

## Repo layout (for forkers)

`core/` is the source — one fragment per command, the landing shell, the prose sections, and the second-act prompts. `index.html` and `guide.html` are **generated** from it by `tools/build_installer.py`; don't hand-edit them — edit `core/`, rebuild, done. That's the escape hatch: fork it, reshape `core/`, and it's yours.

## License

[MIT](LICENSE) — free to use, copy, modify, and share, including commercially. Keep the copyright line; otherwise, make it yours.

---

<div align="center">
<sub>Built &amp; shared by Craig Vandeputte · adapt it freely.</sub>
</div>
