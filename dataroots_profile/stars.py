"""Eventbrite helpers for events dynamic info."""
from dataclasses import dataclass
from enum import Enum
from typing import Any

import requests

Status = Enum("Status", ["draft", "live", "completed"])


@dataclass
class Repo:
    """GitHub repository."""

    id: int
    name: str
    full_name: str
    private: bool
    html_url: str
    stargazers_count: int
    language: str
    forks_count: int
    open_issues_count: int
    ...


def repos(
    org_name: str = "datarootsio",
) -> list[Repo]:
    """Retrieve all repos from GitHub."""
    response = requests.get(
        f"https://api.github.com/orgs/{org_name}/repos",
    )
    return [
        Repo(**{k: v for k, v in repo.items() if k in Repo.__annotations__.keys()})
        for repo in response.json()
    ]


def repos2stars(repos: list[Repo]) -> int:
    """Get the sum of stars in all the repos in the list."""
    return sum(repo.stargazers_count for repo in repos)


def stars2shield(
    stars: int, *, description: str = "GitHub_Stars", color: str = "38b580"
) -> str:
    """
    Generate a shield with the number of stars from `shields.io`.

    The `description` string will have underscores replaced by spaces.
    The `color` can be `hex`, `rgb`, `rgba`, `hsl`, `hsla` and `css` named colors.
    More info on `https://shields.io/badges`.
    """
    return f"https://img.shields.io/badge/{stars}_⭐️_-{description}-{color}"


def shield(
    org_name: str = "datarootsio",
    **shield_kwargs: Any,
) -> str:
    """Get a markdown string with the number of stars."""
    return (
        f"[![stars]({stars2shield(repos2stars(repos('datarootsio')),**shield_kwargs)})]"
        f"(https://github.com/orgs/{org_name}/repositories)"
    )
