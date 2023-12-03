import json
from datetime import datetime
from pathlib import Path

from spielerplus_calendar import parsing


def test_parse_event_calendar():
    html = Path("tests/data/event-calendar.html").read_text("utf-8")
    target = json.loads(Path("tests/data/event-calendar-items.json").read_text("utf-8"))

    actual = parsing.parse_event_calendar(html)

    assert actual == target


def test_parse_datetime():
    timestamp = "2022-12-14T17:25:00Z"
    target = datetime(2022, 12, 14, 17, 25)

    actual = parsing.parse_timestamp(timestamp)

    assert actual == target


def test_parse_event_list_old():
    html = Path("tests/data/event-list-old-0.html").read_text("utf-8")
    target = [
        {
            "id": "event-training-55555",
            "title": "Training",
            "start": datetime(datetime.today().year, 9, 30, 18, 55),
            "end": datetime(datetime.today().year, 9, 30, 20, 30),
            "url": "/training/view?id=55555",
        },
        {
            "id": "event-training-66666",
            "title": "Training",
            "start": datetime(datetime.today().year, 10, 3, 17, 55),
            "end": datetime(datetime.today().year, 10, 3, 20, 0),
            "url": "/training/view?id=66666",
        },
    ]

    actual = parsing.parse_event_list_items(html)

    assert actual == target


def test_parse_event_list_old_3():
    html = Path("tests/data/event-list-old-3.html").read_text("utf-8")
    target = [
        {
            "id": "event-training-11111",
            "title": "Training",
            "start": datetime(datetime.today().year, 9, 23, 18, 55),
            "end": datetime(datetime.today().year, 9, 23, 20, 30),
            "url": "/training/view?id=11111",
        },
    ]

    actual = parsing.parse_event_list_items(html)

    assert actual == target


def test_parse_event_list_today():
    html = Path("tests/data/events.html").read_text("utf-8")
    target = [
        {
            "id": "event-event-11120",
            "title": "test heute",
            "start": datetime(datetime.today().year, 11, 26, 10, 0),
            "end": datetime(datetime.today().year, 11, 26, 11, 30),
            "url": "/event/view?id=11120",
        },
        {
            "id": "event-training-11122",
            "title": "Training",
            "start": datetime(datetime.today().year, 11, 28, 18, 25),
            "end": datetime(datetime.today().year, 11, 28, 20, 0),
            "url": "/training/view?id=11122",
        },
        {
            "id": "event-training-11124",
            "title": "Training",
            "start": datetime(datetime.today().year, 12, 2, 18, 55),
            "end": datetime(datetime.today().year, 12, 2, 20, 30),
            "url": "/training/view?id=11124",
        },
    ]

    actual = parsing.parse_event_list_items(html)

    assert actual == target


def test_parse_event_list_item_subtitle():
    html = Path("tests/data/event-list-item-subtitle.html").read_text("utf-8")
    target = [
        {
            "id": "event-event-11125",
            "title": "Training + Spiel - SG Gegner",
            "start": datetime(datetime.today().year, 9, 23, 18, 55),
            "end": datetime(datetime.today().year, 9, 23, 20, 30),
            "url": "/event/view?id=11125",
        },
    ]

    actual = parsing.parse_event_list_items(html)

    assert actual == target


def test_parse_canceled_event_list_item():
    html = Path("tests/data/event-list-item-canceled.html").read_text("utf-8")

    actual = parsing.parse_event_list_items(html)

    assert not actual


def test_parse_end_from_multiday_event_list_item():
    html = Path("tests/data/event-list-item-multiday.html").read_text("utf-8")

    begin = parsing.parse_begin(html)
    actual = parsing.parse_end(html, begin)

    assert actual == datetime(datetime.today().year, 6, 18, 11, 0)


def test_parse_event_year():
    html = Path("tests/data/event.html").read_text("utf-8")

    actual = parsing.parse_event_year(html)

    assert actual == 2022


def test_parse_year_from_multiday_event():
    html = Path("tests/data/event-multiday.html").read_text("utf-8")

    actual = parsing.parse_event_year(html)

    assert actual == 2023


def test_parse_description():
    html = Path("tests/data/game.html").read_text("utf-8")

    actual = parsing.parse_description(html)

    assert actual == "Some description"


def test_parse_long_description():
    html = Path("tests/data/game-long-desc.html").read_text("utf-8")

    actual = parsing.parse_description(html)
    target = "This is the first line\nanother line & special char\nsome time 12:00 end"
    assert actual == target


def test_parse_no_description():
    html = Path("tests/data/event.html").read_text("utf-8")

    actual = parsing.parse_description(html)

    assert actual == ""


def test_parse_address():
    html = Path("tests/data/game.html").read_text("utf-8")

    actual = parsing.parse_address(html)

    assert actual == "Some address"


def test_parse_no_address():
    html = Path("tests/data/event-no-address.html").read_text("utf-8")

    actual = parsing.parse_address(html)

    assert actual == ""
