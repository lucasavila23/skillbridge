"""Report relative Markdown links (and #anchors) that do not resolve. Exit 1 if any are found."""
import os, re, subprocess, sys
from urllib.parse import unquote

SKIP = ("prototype/backups/", "evidence-log/market-research/sources/", ".codegraph/", ".superpowers/", "docs/superpowers/")
LINK = re.compile(r"\]\(([^)\s]+)\)|^\[[^\]]+\]:\s*(\S+)", re.M)


def slug(heading):
    """GitHub-style heading anchor: lowercase, drop punctuation, spaces to hyphens."""
    heading = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return heading.replace(" ", "-")


def anchors(path, cache={}):
    if path not in cache:
        with open(path, encoding="utf-8") as fh:
            cache[path] = {slug(m.group(1)) for m in re.finditer(r"^#+\s+(.*)$", fh.read(), re.M)}
    return cache[path]


def broken():
    # -z keeps paths with spaces intact (several research notes have them).
    out = subprocess.run(["git", "ls-files", "-z", "-co", "--exclude-standard", "*.md"],
                         capture_output=True, text=True, check=True).stdout
    for f in filter(None, out.split("\0")):
        if f.startswith(SKIP) or not os.path.exists(f):
            continue
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        for a, b in LINK.findall(text):
            target = a or b
            if target.startswith(("http:", "https:", "mailto:")):
                continue
            path, _, frag = target.partition("#")
            resolved = os.path.normpath(os.path.join(os.path.dirname(f), unquote(path))) if path else f
            if not os.path.exists(resolved):
                yield f, target
            elif frag and resolved.endswith(".md") and slug(unquote(frag)) not in anchors(resolved):
                yield f, target + "  (anchor not found)"


if __name__ == "__main__":
    bad = list(broken())
    for f, t in bad:
        print(f"{f} -> {t}")
    sys.exit(1 if bad else 0)
