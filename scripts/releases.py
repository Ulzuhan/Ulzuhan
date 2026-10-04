"""Rewrite the "Latest releases" block in README.md.

Takes the newest stable version tag of each project below, dates it by its
GitHub release (or by the tag when there is no release), and lists the most
recent ones between the releases:start / releases:end markers.

Needs GITHUB_TOKEN in the environment. Standard library only.
"""

import json
import os
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

OWNER = "Ulzuhan"
REPOS = [
    "reed",
    "reed-mcp",
    "private-ai-stack",
    "arveil",
    "docdrop",
    "secretdrop",
    "signdrop",
    "tabup",
    "qr-forge",
    "linkup",
    "pixelforge",
    "kaicorp-account",
]
SHOWN = 6
README = Path(__file__).resolve().parent.parent / "README.md"
START, END = "<!-- releases:start -->", "<!-- releases:end -->"
STABLE = re.compile(r"^v?\d+\.\d+\.\d+$")

FRAGMENT = """
fragment R on Repository {
  name
  url
  refs(refPrefix: "refs/tags/", first: 30, orderBy: {field: TAG_COMMIT_DATE, direction: DESC}) {
    nodes {
      name
      target {
        ... on Commit { committedDate }
        ... on Tag { tagger { date } target { ... on Commit { committedDate } } }
      }
    }
  }
  releases(first: 30, orderBy: {field: CREATED_AT, direction: DESC}) {
    nodes { tagName publishedAt isDraft }
  }
}
"""


def query(token):
    fields = "\n".join(
        f'  r{i}: repository(owner: "{OWNER}", name: "{name}") {{ ...R }}'
        for i, name in enumerate(REPOS)
    )
    body = json.dumps({"query": "query {\n" + fields + "\n}\n" + FRAGMENT}).encode()
    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    if payload.get("errors"):
        sys.exit(f"GraphQL errors: {payload['errors']}")
    return [repo for repo in payload["data"].values() if repo]


def parse(stamp):
    return datetime.fromisoformat(stamp.replace("Z", "+00:00"))


def tag_date(target):
    if not target:
        return None
    if target.get("tagger"):
        return target["tagger"]["date"]
    if target.get("committedDate"):
        return target["committedDate"]
    return (target.get("target") or {}).get("committedDate")


def latest(repo):
    published = {
        r["tagName"]: r["publishedAt"]
        for r in repo["releases"]["nodes"]
        if r["publishedAt"] and not r["isDraft"]
    }
    best = None
    for ref in repo["refs"]["nodes"]:
        if not STABLE.match(ref["name"]):
            continue
        stamp = published.get(ref["name"]) or tag_date(ref["target"])
        if not stamp:
            continue
        when = parse(stamp)
        if best is None or when > best[1]:
            best = (ref["name"], when)
    if best is None:
        return None
    tag, when = best
    return {
        "repo": repo["name"],
        "repo_url": repo["url"],
        "tag": tag,
        "tag_url": f"{repo['url']}/releases/tag/{tag}",
        "when": when,
    }


def render(entries):
    lines = [
        f"- **[{e['repo']}]({e['repo_url']})** [{e['tag']}]({e['tag_url']})"
        f" · {e['when']:%b} {e['when'].day}, {e['when']:%Y}"
        for e in entries
    ]
    return "\n".join(lines)


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN is not set")
    entries = [e for e in (latest(repo) for repo in query(token)) if e]
    entries.sort(key=lambda e: e["when"], reverse=True)
    block = render(entries[:SHOWN])

    text = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        sys.exit("Release markers not found in README.md")
    updated = pattern.sub(lambda _: f"{START}\n{block}\n{END}", text)
    if updated != text:
        README.write_text(updated, encoding="utf-8")
        print("README.md updated")
    else:
        print("No changes")


if __name__ == "__main__":
    main()
