#!/usr/bin/env python3
"""Generate ai-os/index.html from the core/ source fragments.

index.html is a BUILD ARTIFACT — edit core/, never index.html. The build is
deterministic and idempotent: no source change -> byte-identical output (which is
what keeps the 3-copy ai_os_sync_check.sh meaningful).

Usage:
  build_installer.py            # write index.html from core/
  build_installer.py --check    # exit 1 if index.html is stale vs core/ (CI guard)

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

def render():
    before = read("sections/before-skills.txt")
    after = read("sections/after-skills.txt")
    career = read("second-act/career.txt")

    frags = [pathlib.Path(p).read_text() for p in glob.glob(str(CORE / "skills/*.md"))]
    frags.sort(key=skill_order)
    bodies = [skill_body(f) for f in frags]

    prompt = before + JOIN + JOIN.join(bodies) + JOIN + after

    shell = read("shell.html")
    if shell.count("{{PROMPT}}") != 1 or shell.count("{{PROMPT2}}") != 1:
        sys.exit("FATAL: shell.html must contain exactly one {{PROMPT}} and one {{PROMPT2}}")
    html = shell.replace("{{PROMPT}}", prompt, 1).replace("{{PROMPT2}}", career, 1)
    html = html.replace("{{VERSION}}", read_version())   # global: stamps all build markers
    if "{{VERSION}}" in html:
        sys.exit("FATAL: unsubstituted {{VERSION}} remains")
    return html

def main():
    html = render()
    if "--check" in sys.argv[1:]:
        current = OUT.read_text() if OUT.exists() else None
        if current == html:
            print("OK: index.html is up to date with core/")
            return 0
        print("STALE: index.html differs from a fresh build of core/ "
              "(run build_installer.py to regenerate)", file=sys.stderr)
        return 1
    OUT.write_text(html)
    print("wrote", OUT, "(%d bytes)" % len(html))
    return 0

if __name__ == "__main__":
    sys.exit(main())
