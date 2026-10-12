"""Report relative Markdown links that do not resolve. Exit 1 if any are found."""
import os, re, subprocess, sys
from urllib.parse import unquote

SKIP = ("prototype/backups/", "evidence-log/market-research/sources/", ".codegraph/", ".superpowers/", "docs/superpowers/")
LINK = re.compile(r"\]\(([^)\s#]+)(?:#[^)]*)?\)|^\[[^\]]+\]:\s*([^\s#]+)", re.M)

def broken():
    files = subprocess.run(["git", "ls-files", "-co", "--exclude-standard", "*.md"],
                           capture_output=True, text=True, check=True).stdout.split()
    for f in files:
        if f.startswith(SKIP) or not os.path.exists(f):
            continue
        for target in (a or b for a, b in LINK.findall(open(f, encoding="utf-8").read())):
            if target.startswith(("http:", "https:", "mailto:")):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), unquote(target)))):
                yield f, target

if __name__ == "__main__":
    bad = list(broken())
    for f, t in bad:
        print(f"{f} -> {t}")
    sys.exit(1 if bad else 0)
