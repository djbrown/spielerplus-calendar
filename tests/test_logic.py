import json
from pathlib import Path

from spielerplus_calendar import logic


def test_filter_items():
    items = json.loads(Path("tests/data/event-calendar-items.json").read_text())
    target = json.loads(Path("tests/data/event-calendar-items-filtered.json").read_text())

    actual = logic.filter_items(items)

    assert actual == target
