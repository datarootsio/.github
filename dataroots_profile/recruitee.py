"""Recruitee helpers for jobs dynamic info."""
from dataclasses import dataclass
from textwrap import dedent

import requests


@dataclass
class Offer:
    """Partial offer response from Recruitee API."""

    careers_url: int
    title: str
    ...


def jobs() -> list[Offer]:
    """Retrieve active jobs from Recruitee."""
    response = requests.get(
        "https://dataroots.recruitee.com/api/offers",
        headers={"accept": "application/json"},
    )
    return [
        Offer(careers_url=offer["careers_url"], title=offer["title"])
        for offer in response.json().get("offers", [])
    ]


def offer2str(offer: Offer) -> str:
    """Get a formatted string for markdown profile from offer information."""
    return f"- [{offer.title}]({offer.careers_url})"


def jobs2str(offers: list[Offer]) -> str:
    """Get a nice string with jobs from listing."""
    if not offers:
        raise ValueError(f"Expected list of offers, got {offers}.")
    _offers = "\n".join(offer2str(offer) for offer in offers)
    return dedent(
        f"""\
## Join our team! ❤️

Our open positions:

{_offers}

For more info check out [dataroots.io/careers](https://dataroots.io/careers) 👈""",
    )


def info() -> str:
    """Get jobs information string for markdown profile."""
    return jobs2str(jobs())
