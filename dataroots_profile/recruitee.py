"""Recruitee helpers for jobs dynamic info."""
from dataclasses import dataclass
from pprint import pprint
from textwrap import dedent
from typing import Any

import requests

URL_BASE = "https://careers.dataroots.io/o/"


@dataclass
class Offer:
    """'Brief' offer information (instead of 'default') from Recruitee API."""

    careers_url: int
    title: str


def jobs() -> list[Offer]:
    """Retrieve active jobs from Recruitee."""
    response = requests.get(
        "https://dataroots.recruitee.com/api/offers",
        headers={"accept": "application/json"},
    )
    return [Offer(careers_url=offer["careers_url"], title=offer["title"]) for offer in response.json().get("offers", [])]


def offer2str(offer: Offer, *, url_base: str = URL_BASE) -> str:
    """Get a formatted string for markdown profile from offer information."""
    return f"- [{offer.title}]({offer.careers_url})"


def jobs2str(offers: list[Offer], **offer2str_kwargs: Any) -> str:
    """Get a nice string with jobs from listing."""
    if not offers:
        raise ValueError(f"Expected list of offers, got {offers}.")
    offers = "\n".join(offer2str(offer, **offer2str_kwargs) for offer in offers)
    return dedent(
        f"""\
## Join our team! ❤️

Our open positions:

{offers}

For more info check out [dataroots.io/careers](https://dataroots.io/careers) 👈"""
    )


def info(**offer2str_kwargs: Any) -> str:
    """Get jobs information string for markdown profile."""
    _jobs = jobs()
    return jobs2str(_jobs, **offer2str_kwargs)
