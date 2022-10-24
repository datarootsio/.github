"""Recruitee helpers for jobs dynamic info."""
from dataclasses import dataclass
from textwrap import dedent
from typing import Any

import requests

URL_BASE = "https://careers.dataroots.io/o/"


@dataclass
class Offer:
    """'Brief' offer information (instead of 'default') from Recruitee API."""

    location: str
    id: int
    slug: str
    status: str
    position: str
    guid: str
    lang_code: str
    department_id: int
    kind: str
    title: str


def jobs(*, company_id: str, token: str) -> list[Offer]:
    """Retrieve active jobs from Recruitee."""
    response = requests.get(
        f"https://api.recruitee.com/c/{company_id}/offers?scope=active&view_mode=brief",
        headers={"accept": "application/json", "authorization": f"Bearer {token}"},
    )
    return [Offer(**offer) for offer in response.json().get("offers", [])]


def offer2str(offer: Offer, *, url_base: str = URL_BASE) -> str:
    """Get a formatted string for markdown profile from offer information."""
    return dedent(
        f"""\
- {offer.title}
    - 🏡 {offer.location}
    - [✍️ Apply!]({url_base + offer.slug})"""
    )


def jobs2str(offers: list[Offer], **offer2str_kwargs: Any) -> str:
    """Get a nice string with jobs from listing."""
    if not offers:
        raise ValueError(f"Expected list of offers, got {offers}.")
    offers = "\n".join(offer2str(offer, **offer2str_kwargs) for offer in offers)
    return dedent(
        f"""\
### Join our team! 🤝

{offers}"""
    )


def info(company_id: str, token: str, **offer2str_kwargs: Any) -> str:
    """Get jobs information string for markdown profile."""
    _jobs = jobs(company_id=company_id, token=token)
    return jobs2str(_jobs, **offer2str_kwargs)
