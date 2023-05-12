"""Ghost helpers for jobs dynamic info."""
from dataclasses import dataclass
from datetime import datetime
from textwrap import dedent
from typing import Any

import requests


@dataclass
class Post:
    """Partial model for Ghosts' posts response."""

    title: str
    slug: str
    published_at: datetime
    ...


def posts(key: str, admin_domain: str = "dataroots.ghost.io") -> list[Post]:
    """Retrieve posts from Ghost CMS."""
    response = requests.get(
        f"https://{admin_domain}/ghost/api/content/posts/?key={key}",
        headers={"accept": "application/json"},
    )
    return [
        Post(
            title=post["title"],
            slug=post["slug"],
            published_at=datetime.strptime(
                post["published_at"],
                "%Y-%m-%dT%H:%M:%S.%f+00:00",
            ),
        )
        for post in response.json().get("posts", [])
    ]


def post2str(
    post: Post,
    *,
    base_url: str = "https://dataroots.io/research/contributions",
) -> str:
    """Get a formatted string for markdown profile from posts information."""
    base_url = base_url.rstrip("/", 1)[0] if base_url.endswith("/") else base_url
    return (
        f"- [{post.title} ({post.published_at.strftime('%d/%m/%Y')})]"
        f"({base_url}/{post.slug})"
    )


def content2str(posts: list[Post], n_posts: int = 5) -> str:
    """Get a nice string with blog contents from listing."""
    if not posts:
        raise ValueError(f"Expected list of posts, got {posts}.")
    _posts = "\n".join(
        post2str(post)
        for post in sorted(posts[:n_posts], key=lambda p: p.published_at, reverse=True)
    )
    return dedent(
        f"""\
## Our blog ✍️

Our latest posts:

{_posts}

Check out all our posts at [dataroots.io/research/contributions/]\
(https://dataroots.io/research/contributions/) 👈""",
    )


def info(n_posts: int = 5, **posts_kwargs: Any) -> str:
    """Get content information string for markdown profile."""
    return content2str(posts(**posts_kwargs), n_posts=n_posts)
