---
name: doctor
order: 17
tier: core
---
   - /doctor — A quick READ-ONLY "is my AI-OS healthy?" check I can run any time: it
     inspects and reports, and must NEVER change, delete, or send anything. Cover the
     AI-OS-specific state that the platform's own checker can't see: (1) CONNECTORS —
     run /mcp and report which mail/calendar connector is signed in vs. needs a fresh
     sign-in; this is the thing most likely to be quietly broken, and /mcp shows the
     live auth, so if one needs sign-in point me to re-authorize it. (2) MEMORY —
     confirm ~/ai-os/memory/ exists, report its rough size and how many notes it holds,
     and flag if it's grown big enough that a /memory-prune is worth running. (3)
     TOOLKIT — count and list the skills installed under ~/.claude/skills/ so I can see
     my commands are all registered (if one I expect is missing, that's why it "does
     nothing" — start a fresh session to register newly-built ones). (4) PROTECTION —
     if ~/ai-os/backups/ exists, report the age of my most recent /backup so a stale or
     missing backup is visible; if there's no backup yet, say so and suggest running
     /backup. Then, for the deeper SYSTEM layer — install health, connector CONFIG
     validity, version currency, search/ripgrep, CLAUDE.md size — tell me to run Claude
     Code's own built-in /doctor (if it's available here); don't reinvent that plumbing,
     just point at it. Finish with a short green / needs-attention summary naming the
     one or two things worth doing next. Build it as a Claude Code skill, strictly
     READ-ONLY (inspect and report only). Pairs with /backup: /doctor tells me my
     safety net is current. Trigger on "/doctor", "is my AI-OS healthy / okay", "health
     check", "check my system / check my connectors".
