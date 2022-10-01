import json
from datetime import datetime
from pathlib import Path

from spielerplus_calendar import logic


def test_filter_items():
    items = json.loads(
        Path("tests/data/event-calendar-items.json").read_text(encoding="utf-8")
    )
    target = json.loads(
        Path("tests/data/event-calendar-items-filtered.json").read_text(
            encoding="utf-8"
        )
    )

    actual = logic.filter_items(items)

    assert actual == target


def test_map_items():
    items = json.loads(
        Path("tests/data/event-calendar-items-filtered.json").read_text(
            encoding="utf-8"
        )
    )
    target = [
        logic.Appointment(
            id=12329600,
            title="Training",
            start=datetime(2022, 9, 5, 17, 55, 00),
            end=datetime(2022, 9, 5, 20, 00, 00),
            url="/training/view?id=12329600",
            color="#44AD34",
        ),
        logic.Appointment(
            id=12899706,
            title="Training+ Fototermin vorher",
            start=datetime(2022, 9, 12, 17, 50, 00),
            end=datetime(2022, 9, 12, 20, 00, 00),
            url="/training/view?id=12899706",
            color="#44AD34",
        ),
        logic.Appointment(
            id=12899707,
            title="Training",
            start=datetime(2022, 9, 19, 18, 25, 00),
            end=datetime(2022, 9, 19, 20, 00, 00),
            url="/training/view?id=12899707",
            color="#44AD34",
        ),
        logic.Appointment(
            id=54026552,
            title="Training",
            start=datetime(2022, 9, 2, 17, 55, 00),
            end=datetime(2022, 9, 2, 20, 00, 00),
            url="/training/view?id=54026552",
            color="#44AD34",
        ),
        logic.Appointment(
            id=654026553,
            title="Training",
            start=datetime(2022, 9, 9, 17, 55, 00),
            end=datetime(2022, 9, 9, 20, 00, 00),
            url="/training/view?id=654026553",
            color="#44AD34",
        ),
        logic.Appointment(
            id=54026552,
            title="Training",
            start=datetime(2022, 9, 16, 18, 40, 00),
            end=datetime(2022, 9, 16, 20, 30, 00),
            url="/training/view?id=54026552",
            color="#44AD34",
        ),
        logic.Appointment(
            id=65426555,
            title="Training",
            start=datetime(2022, 9, 23, 18, 55, 00),
            end=datetime(2022, 9, 23, 20, 30, 00),
            url="/training/view?id=65426555",
            color="#44AD34",
        ),
        logic.Appointment(
            id=65426556,
            title="Training",
            start=datetime(2022, 9, 30, 18, 55, 00),
            end=datetime(2022, 9, 30, 20, 30, 00),
            url="/training/view?id=65426556",
            color="#44AD34",
        ),
        logic.Appointment(
            id=5440992,
            title="Gegner W",
            start=datetime(2022, 4, 27, 16, 50, 00),
            end=datetime(2022, 4, 27, 18, 30, 00),
            url="/game/view?id=5440992",
            color="#34692D",
        ),
        logic.Appointment(
            id=5603407,
            title="Gegner A",
            start=datetime(2022, 7, 11, 18, 10, 00),
            end=datetime(2022, 7, 11, 20, 00, 00),
            url="/game/view?id=5603407",
            color="#34692D",
        ),
        logic.Appointment(
            id=1049518,
            title="Training + Spiel",
            start=datetime(2022, 4, 24, 11, 55, 00),
            end=datetime(2022, 4, 24, 15, 30, 00),
            url="/event/view?id=1049518",
            color="#34692D",
        ),
        logic.Appointment(
            id=1065779,
            title="Meisterfeier",
            start=datetime(2022, 5, 25, 18, 00, 00),
            end=datetime(2022, 5, 25, 23, 59, 59),
            url="/event/view?id=1065779",
            color="#34692D",
        ),
        logic.Appointment(
            id=679238,
            title="Quali",
            start=datetime(2022, 4, 30, 10, 00, 00),
            end=datetime(2022, 4, 30, 17, 00, 00),
            url="/tournament/view?id=679238",
            color="#34692D",
        ),
        logic.Appointment(
            id=710393,
            title="Turnier",
            start=datetime(2022, 7, 9, 12, 45, 00),
            end=datetime(2022, 7, 9, 23, 59, 59),
            url="/tournament/view?id=710393",
            color="#34692D",
        ),
    ]

    actual = [logic.to_appointment(item) for item in items]

    assert actual == target
