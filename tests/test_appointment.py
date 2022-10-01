import json
from pathlib import Path

from spielerplus_calendar import appointment
from tests import fixtures


def test_filter_items():
    items = json.loads(Path("tests/data/event-calendar-items.json").read_text("utf-8"))
    target = json.loads(
        Path("tests/data/event-calendar-items-filtered.json").read_text("utf-8")
    )

    actual = appointment.filter_items(items)

    assert actual == target


def test_map_items():
    items = json.loads(
        Path("tests/data/event-calendar-items-filtered.json").read_text("utf-8")
    )
    target = fixtures.filtered_appointments()

    actual = [appointment.to_appointment(item) for item in items]

    assert actual == target
