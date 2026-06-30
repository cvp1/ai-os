#!/usr/bin/env python3
"""Generate ai-os/index.html from the core/ source fragments.

index.html is a BUILD ARTIFACT — edit core/, never index.html. The build is
deterministic and idempotent: no source change -> byte-identical output (which is
what keeps the 3-copy ai_os_sync_check.sh meaningful).

Usage:
  build_installer.py            # write index.html from core/ (warns on coverage drift)
  build_installer.py --check    # exit 1 if index.html is stale OR a command is
                                # missing from a human-facing list (CI guard)

After a real build, propagate to the docsite/vault copies with:
  ../ai-os-pm/.. no -> tools/ai_os_sync_check.sh --sync   (run from ai-os-pm/tools)
Canonical source of truth for the prompt text is core/; for the served copies it
remains the public-repo index.html (see ai_os_sync_check.sh).

Stdlib only, /usr/bin/python3.
"""
import re, sys, glob, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent      # .../ai-os
CORE = ROOT / "core"
OUT = ROOT / "index.html"
JOIN = "\n\n"   # the exact separator that flanks/separates skill blocks

def read(p):
    return (CORE / p).read_text()

def read_version():
    m = re.search(r'^version:\s*"?([^"\n]+?)"?\s*(?:#.*)?$', read("meta.yml"), re.M)
    if not m:
        sys.exit("FATAL: meta.yml has no version")
    return m.group(1).strip()

def skill_body(text):
    """Strip the leading '---\\n...\\n---\\n' frontmatter; return the exact body."""
    m = re.match(r"---\n.*?\n---\n", text, re.S)
    if not m:
        sys.exit("FATAL: skill fragment missing frontmatter")
    return text[m.end():]

def skill_order(text):
    m = re.search(r"^order:\s*(\d+)\s*$", text, re.M)
    return int(m.group(1)) if m else 9999

def skill_commands():
    """Command names (without the slash) declared by core/skills/*.md frontmatter."""
    cmds = []
    for p in sorted(glob.glob(str(CORE / "skills/*.md"))):
        t = pathlib.Path(p).read_text()
        m = re.search(r"^name:\s*(\S+)\s*$", t, re.M)
        if not m:
            sys.exit("FATAL: %s has no name: in frontmatter" % pathlib.Path(p).name)
        cmds.append(m.group(1).strip())
    return cmds

def _section(html, sec_id):
    """Inner markup of <section id="sec_id"> ... </section>, or '' if absent."""
    m = re.search(r'<section id="%s".*?</section>' % re.escape(sec_id), html, re.S)
    return m.group(0) if m else ""

def check_command_coverage():
    """Every core/skills command must be named in BOTH human-facing surfaces — the
    README command table and the landing #commands section — not just in the pasted
    prompt (which the build always fills). This is the tripwire for the drift where a
    new skill ships in the prompt but is missing from the lists a person actually
    reads. Limits (by design, kept a simple tripwire): it does not police the reverse
    (a listed command with no skill), nor distinguish a dedicated row from an
    in-prose cross-reference. Returns a list of problem strings ([] = clean)."""
    problems = []
    readme = (ROOT / "README.md").read_text()
    commands_sec = _section(read("shell.html"), "commands")
    if not commands_sec:
        problems.append('shell.html has no <section id="commands"> to check')
    for name in skill_commands():
        n = re.escape(name)
        # A command counts as "listed" on the landing page if it appears either as a
        # contiguous /name (in a description or the "Try saying" column) OR in the grid's
        # command cell, where the slash is its own span: <span class="slash">/</span>name.
        # (The cell form couples this check to that template — fine; if the markup ever
        # changes the guard fails loudly and gets updated.)
        plain = re.compile(r"/%s(?![\w-])" % n)
        cell = re.compile(r'/</span>%s(?![\w-])' % n)
        if not plain.search(readme):
            problems.append("/%s missing from the README command list" % name)
        if commands_sec and not (plain.search(commands_sec) or cell.search(commands_sec)):
            problems.append("/%s missing from the landing #commands section" % name)
    return problems

def render():
    before = read("sections/before-skills.txt")
    after = read("sections/after-skills.txt")
    career = read("second-act/career.txt")
    scheduler = read("second-act/scheduler.txt")

    frags = [pathlib.Path(p).read_text() for p in glob.glob(str(CORE / "skills/*.md"))]
    frags.sort(key=skill_order)
    bodies = [skill_body(f) for f in frags]

    prompt = before + JOIN + JOIN.join(bodies) + JOIN + after

    shell = read("shell.html")
    if (shell.count("{{PROMPT}}") != 1 or shell.count("{{PROMPT2}}") != 1
            or shell.count("{{PROMPT3}}") != 1):
        sys.exit("FATAL: shell.html must contain exactly one each of "
                 "{{PROMPT}}, {{PROMPT2}}, {{PROMPT3}}")
    html = (shell.replace("{{PROMPT}}", prompt, 1)
                 .replace("{{PROMPT2}}", career, 1)
                 .replace("{{PROMPT3}}", scheduler, 1))
    html = html.replace("{{VERSION}}", read_version())   # global: stamps all build markers
    if "{{VERSION}}" in html:
        sys.exit("FATAL: unsubstituted {{VERSION}} remains")
    return html

def main():
    html = render()
    coverage = check_command_coverage()
    if "--check" in sys.argv[1:]:
        problems = list(coverage)
        current = OUT.read_text() if OUT.exists() else None
        if current != html:
            problems.append("index.html is stale vs a fresh build of core/ "
                            "(run build_installer.py to regenerate)")
        if problems:
            for p in problems:
                print("FAIL:", p, file=sys.stderr)
            return 1
        print("OK: index.html up to date with core/; all %d commands listed in "
              "README + landing" % len(skill_commands()))
        return 0
    if coverage:
        print("WARNING — command-coverage drift (fix before publishing):",
              file=sys.stderr)
        for p in coverage:
            print("  -", p, file=sys.stderr)
    OUT.write_text(html)
    print("wrote", OUT, "(%d bytes)" % len(html))
    return 0

if __name__ == "__main__":
    sys.exit(main())
