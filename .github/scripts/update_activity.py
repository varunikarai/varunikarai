"""Rewrite the activity block in README.md from public GitHub data.

Only public repositories are counted. Owners in DENY never appear.
Her own repos are left out of the 30-day line, so nothing in progress shows.
The block carries today's IST date, so it changes once per day.
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

USER = "varunikarai"
DENY = {"varunikarai/varunikarai"}
DENY_OWNERS = {"kaya-ai", "aeshvarya"}
IST = timezone(timedelta(hours=5, minutes=30))
START = "<!-- ACTIVITY:START -->"
END = "<!-- ACTIVITY:END -->"
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def call(url, body=None):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-readme"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def allowed(name, private=False, own_ok=True):
    owner = name.split("/")[0].lower()
    if not own_ok and owner == USER:
        return False
    return not private and name not in DENY and owner not in DENY_OWNERS


def ist_date(stamp):
    return datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=timezone.utc).astimezone(IST).strftime("%Y-%m-%d")


def merged_prs():
    q = f"is:pr is:public is:merged author:{USER} -user:{USER}"
    url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
        {"q": q, "sort": "created", "order": "desc", "per_page": 100})
    out = []
    for it in call(url)["items"]:
        repo = it["repository_url"].split("/repos/")[1]
        if not allowed(repo):
            continue
        out.append({"repo": repo, "number": it["number"], "title": it["title"],
                    "url": it["html_url"], "merged": ist_date(it["pull_request"]["merged_at"])})
    out.sort(key=lambda p: p["merged"], reverse=True)
    return out


def last_30_days():
    now = datetime.now(timezone.utc)
    frm = (now - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
    to = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    kinds = ["commitContributionsByRepository", "pullRequestContributionsByRepository",
             "issueContributionsByRepository", "pullRequestReviewContributionsByRepository"]
    fields = " ".join(
        f"{k}(maxRepositories: 100) {{ repository {{ nameWithOwner isPrivate }} contributions {{ totalCount }} }}"
        for k in kinds)
    query = f'query {{ user(login: "{USER}") {{ contributionsCollection(from: "{frm}", to: "{to}") {{ {fields} }} }} }}'
    data = call("https://api.github.com/graphql", {"query": query})
    if "errors" in data:
        raise SystemExit(f"GraphQL error: {data['errors']}")
    cc = data["data"]["user"]["contributionsCollection"]
    totals, repos = {}, set()
    for k in kinds:
        n = 0
        for row in cc[k]:
            r = row["repository"]
            if allowed(r["nameWithOwner"], r["isPrivate"], own_ok=False):
                n += row["contributions"]["totalCount"]
                repos.add(r["nameWithOwner"])
        totals[k] = n
    return totals, sorted(repos)


def plural(n, word):
    return f"{n} {word}" + ("" if n == 1 else "s")


def build(today):
    prs = merged_prs()
    lines = [START, "", f"_Updated automatically on {today} (IST) from public GitHub activity._", ""]
    if prs:
        projects = sorted({p["repo"].split("/")[1] for p in prs})
        lines.append(f"**Merged pull requests:** {len(prs)}, across {', '.join(projects)}.")
        lines.append("")
        for p in prs[:5]:
            lines.append(f"- {p['merged']} · [{p['repo']} #{p['number']}]({p['url']}): {p['title']}")
        lines.append("")
    if TOKEN:
        t, repos = last_30_days()
        parts = [plural(t["commitContributionsByRepository"], "commit"),
                 plural(t["pullRequestContributionsByRepository"], "pull request"),
                 plural(t["issueContributionsByRepository"], "issue"),
                 plural(t["pullRequestReviewContributionsByRepository"], "review")]
        if repos:
            links = ", ".join(f"[{r}](https://github.com/{r})" for r in repos)
            lines.append(f"**Last 30 days:** {' · '.join(parts)}, in {links}.")
            lines.append("")
    lines.append(END)
    return "\n".join(lines)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    text = open(path, encoding="utf-8").read()
    if START not in text or END not in text:
        raise SystemExit("activity markers missing from README")
    today = datetime.now(IST).strftime("%Y-%m-%d")
    block = build(today)
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    if new != text:
        open(path, "w", encoding="utf-8").write(new)
        print("README updated")
    else:
        print("no change")


if __name__ == "__main__":
    main()
