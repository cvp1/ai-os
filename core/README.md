# `core/` — the AI-OS installer source

**`../index.html` is a build artifact. Edit `core/`, never `index.html`.**

The single copy-paste installer that ships in `index.html` is *generated* from the
fragments here by `../tools/build_installer.py`. This keeps the novice-facing
single-paste delivery (no terminal, no network, safe) while making authoring modular:
adding/updating a skill is a one-file edit, not surgery on a 600-line monolith.

## Layout

```
core/
  meta.yml                  build manifest (version, paths, join separator)
  shell.html                landing page + {{PROMPT}} / {{PROMPT2}} slots
  sections/
    before-skills.txt       PROMPT up to "…/name. Build:"
    after-skills.txt        PROMPT from "   Keep every skill…" to end
  skills/NN-name.md         ONE fragment per skill: frontmatter + the exact prose
                            that lands in the PHASE 1 SKILLS list (ordered by `order:`)
  second-act/career.txt     the promptSource2 block (career manager)
```

`PROMPT = before + "\n\n".join(skill bodies, by order, flanked by "\n\n") + after`,
then `shell.html` gets `{{PROMPT}}`/`{{PROMPT2}}` substituted. That join exactly
mirrors how the original prompt was structured, so the build is byte-deterministic.

## Build

```bash
python3 ../tools/build_installer.py            # regenerate index.html
python3 ../tools/build_installer.py --check    # CI guard: exit 1 if index.html is stale
```

After a real build, propagate to the docsite/vault copies with the existing guard:
```bash
~/Github/CC/ai-os-pm/tools/ai_os_sync_check.sh --sync
```

## Capture / extend / update flow

1. A skill matures in the proving ground → add/edit `core/skills/NN-name.md`.
2. `build_installer.py` → regenerate `index.html`.
3. `ai_os_sync_check.sh --sync` → propagate to docsite (prints the vault command).
4. Review `git diff` → commit + push.

## Notes

- **Frontmatter is `name`/`order`/`tier` only** for now. `trigger`/`mirrors` (a
  dev-time pointer to the tested skill) are deferred — open decisions in the proposal.
- **Version is NOT yet stamped into the output.** Stamping a build version into the
  UPGRADE-MODE header is the first *intended* edit now that parity is proven — it was
  held back so this migration produced a byte-identical `index.html` (the safety gate).
- Finer splitting of `after-skills.txt` into the per-section files from the proposal
  (`memory-system`, `wiring`, `backup`, `principles`…) is a safe follow-up; the
  skills fan-out — the part that grows — is already isolated.
