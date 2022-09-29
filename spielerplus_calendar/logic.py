from datetime import datetime, timedelta
from typing import TypedDict

from spielerplus_calendar import parsing


def filter_items(items: list) -> list:
    filtered = []
    for item in items:
        if str(item["id"]).startswith("absence."):
            continue
        if item.get("className") == "fc-event-birthday":
            continue
        filtered.append(item)
    return filtered


Appointment = TypedDict(
    "Appointment",
    {
        "id": int,
        "title": str,
        "start": datetime,
        "end": datetime,
        "url": str,
        "color": str,
    },
)


def to_appointment(item) -> Appointment:
    return Appointment(
        id=item["id"],
        title=item["title"],
        start=parsing.parse_timestamp(item["start"]),
        end=parsing.parse_timestamp(item["end"]) - timedelta(days=1),
        url=item["url"],
        color=item["color"],
    )