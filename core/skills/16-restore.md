---
name: restore
order: 16
tier: core
---
   - /restore — Bring this AI-OS back from a snapshot — after a new laptop, a bad
     edit, or a lost folder. Lists the snapshots it can find (local and the cloud
     folder), defaults to the newest, and lays everything back into place — my memory,
     notes, and skills. It is REVERSIBLE: anything it would overwrite is moved aside
     first, so a restore can itself be undone. Use --dry-run to see exactly what it
     would change, and --drill to prove a backup actually restores (into a throwaway
     copy, never touching my live system) — because a backup I've never restored is
     only a hope. Build it per the BACKUP & RECOVERY section below. Trigger on
     "/restore", "restore my AI-OS", "recover my system".