---
name: skill-center
order: 9
tier: core
---
   - /skill-center — Meta-skill to find, create, and audit my skills as my needs
     grow, following Anthropic's skill-authoring best practices.
<!-- docs -->
## What it does
The workshop for your toolkit — find, create, and audit your own commands as your needs grow, following Anthropic's skill-authoring best practices.

## When to use it
When the built-in commands don't quite cover something you do repeatedly, or you want to check an existing skill is well-formed. This is the expert on-ramp — how AI-OS grows *with* you instead of boxing you in.

## Walkthrough
1. Type `/skill-center` and say what you want — *"create a command that drafts my expense report"* or *"audit my /triage skill"*.
2. To create: it scaffolds a new skill to best practices, then you refine it.
3. To find or audit: it lists your skills and flags ones that could be tightened.

A session looks about like this:

> **Skill Center**
> · Installed: 17 commands · 1 flagged (missing a clear trigger)
> · Created: `/expenses` — drafts a monthly report from your receipts folder
> Start a fresh session to register the new command.

## Power user
- **New skills need a fresh session.** A newly-built command registers when you reopen the folder / restart — that's why a brand-new `/command` can "do nothing" until then (`/doctor` confirms what's registered).
- **Keep skills small and single-purpose.** The best commands do one thing with a clear trigger — the same discipline the built-in toolkit follows.
- **It's how AI-OS stays yours.** Everything is plain files you can read, edit, and share; `/skill-center` just makes authoring them follow the good patterns.