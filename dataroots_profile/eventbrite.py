"""Eventbrite helpers for events dynamic info."""
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from textwrap import dedent
from typing import Any

import requests

Status = Enum("Status", ["draft", "live", "completed"])


@dataclass
class Name:
    """Event name property."""

    html: str
    text: str


@dataclass
class Date:
    """Event date property."""

    local: datetime
    timezone: str
    utc: str


@dataclass
class Event:
    """Partial model for Eventbrite's events response."""

    url: str
    name: Name
    start: Date
    status: Status
    ...


def events(
    key: str, filter_status: Status = Status.live, org_id: int = 813260157363
) -> list[Event]:
    """Retrieve events from Eventbrite."""
    response = requests.get(
        f"https://www.eventbriteapi.com/v3/organizations/{org_id}/events/",
        headers={"accept": "application/json", "authorization": f"Bearer {key}"},
    )
    return [
        Event(
            url=event["url"],
            name=Name(**event["name"]),
            start=Date(
                local=datetime.strptime(event["start"]["local"], "%Y-%m-%dT%H:%M:%S"),
                timezone=event["start"]["timezone"],
                utc=event["start"]["utc"],
            ),
            status=Status[event["status"]],
        )
        for event in response.json().get("events", [])
        if Status[event["status"]] == filter_status
    ]


def event2str(event: Event) -> str:
    """Get a formatted string for markdown profile from posts information."""
    return f"- [{event.start.local.strftime('%x')} - {event.name.text}]({event.url})"


def calendar2str(events: list[Event], n_events: int = 5) -> str:
    """Get a nice string with upcoming events for listing."""
    if not events:
        raise ValueError(f"Expected list of posts, got {events}.")
    _events = "\n".join(
        event2str(post)
        for post in sorted(events[-n_events:], key=lambda e: e.start.local)
    )
    _upcoming = f"\nUpcoming:\n\n{_events}\n" if _events else ""

    return dedent(
        f"""\
## Our events 🍻
{_upcoming}
Check out all our events at [dataroots.io/events/](https://dataroots.io/events/)\
 or sign up to our [weekly digest](http://eepurl.com/gzXeR5) 👈"""
    )


def info(n_events: int = 5, **events_kwargs: Any) -> str:
    """Get content information string for markdown profile."""
    return calendar2str(events(**events_kwargs), n_events=n_events)
