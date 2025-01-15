"Fetch github releases and process the json"

import subprocess as sp
import os

import json

import datetime as dt


def fetch_repo(repo: str) -> list[dict]:
    # cmd = ["gh", "auth", "login"]
    # process = sp.run(cmd, stderr=sp.STDOUT)
    cmd = ["gh", "api", "-H", "Accept: application/vnd.github+json", f"repos/{repo}/releases"]
    process = sp.run(cmd, stderr=sp.STDOUT, stdout=sp.PIPE)
    return json.loads(process.stdout)


def generate_blog_entry(repo: str, release_tag: str, date: str, topic_tags: list[str]) -> str:
    owner_name, repo_name = repo.split("/")
    tag_no_v = release_tag.replace("v", "")
    # d = dt.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    d = dt.datetime.fromisoformat(date.replace("Z", ""))
    topics_list = ", ".join(topic_tags)

    return (
        f"""---
title: {repo_name} v{tag_no_v} Released!
date: {d.strftime("%Y-%m-%d %H:%M:%S")} -0000
categories: [releases, {repo_name}]
tags: [{topics_list}]

p_name: "{repo_name}"
p_vers: "{tag_no_v}"
p_owner: "{owner_name}"
---

"""
        "{% include template_release_github.md p_name=page.p_name p_vers=page.p_vers p_owner=page.p_owner %}\n"
    )


def write_blog_entry(repo_slug: str, release_tag: str, date: str, content: str, base_dir: str = "_posts") -> None:
    d = dt.datetime.fromisoformat(date.replace("Z", ""))
    tag_no_v = release_tag.replace("v", "")
    filename = os.path.join(base_dir, f"{d.strftime('%Y-%m-%d')}-Release-{repo_slug}-v{tag_no_v}.md")

    with open(filename, "w") as f:
        f.write(content)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
