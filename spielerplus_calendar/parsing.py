import json
import re
import typing
from datetime import datetime, timedelta

from lxml import html


def parse_event_calendar(html_text: str) -> list:
    pattern = (
        r'^        },"locale":"de","firstDay":1,"events":(\[.*\]),'
        r'"allDayDefault":true,"eventRender":    \(function\(event, element\) {$'
    )
    result: re.Match[str] | None = re.search(pattern, html_text, re.MULTILINE)
    if result is None:
        raise Exception("Could not parse calendar html")
    data = result.group(1)
    return json.loads(data)


def parse_timestamp(timestamp: str) -> datetime:
    return datetime.fromisoformat(timestamp[:-1])  # stip trailing Z


def parse_event_list_items(html_text: str) -> list[dict]:
    dom = html.fromstring(html_text)
    item_xpath = (
        "//div[@class='list event'"
        " and .//button[@class='participation-button selected'"
        " and @title = 'Zugesagt']]"
    )
    items = typing.cast(html.HtmlElement, dom.xpath(item_xpath))

    return [_parse_event_list_item(item) for item in items]


def _parse_event_list_item(item: html.HtmlElement) -> dict:
    id_xpath = ".//div[@class='panel']"
    event_id: str = item.xpath(id_xpath)[0].attrib.get("id")

    title_xpath = ".//div[@class='panel-heading-text']/div[@class='panel-title']"
    title: str = item.xpath(title_xpath)[0].text

    subtitle_xpath = ".//div[@class='panel-heading-text']/div[@class='panel-subtitle']"
    subtitle = item.xpath(subtitle_xpath)
    if subtitle:
        title += " - " + subtitle[0].text

    begin = _parse_begin(item)
    end = _parse_end(item, begin)
    meet = _parse_meet(item, begin)

    url_xpath = ".//a[@class='event-header-border']"
    url: str = item.xpath(url_xpath)[0].attrib.get("href")

    return {"id": event_id, "title": title, "start": meet, "end": end, "url": url}


def _parse_begin(item: html.HtmlElement) -> datetime:
    begin_date_xpath = (
        ".//div[@class='panel-heading-info']/div[@class='panel-subtitle']"
    )
    begin_date_text: str = item.xpath(begin_date_xpath)[0].text
    (begin_day_text, begin_month_text) = begin_date_text.split(".")
    (begin_day, begin_month) = (int(begin_day_text), int(begin_month_text))

    begin_time_xpath = (
        ".//div[@class='event-time-item'"
        " and div[@class='event-time-label'"
        " and text()='Beginn']]"
        "/div[@class='event-time-value']"
    )
    begin_time_text: str = item.xpath(begin_time_xpath)[0].text
    (begin_hour_text, begin_minutes_text) = begin_time_text.split(":")
    (begin_hour, begin_minutes) = (int(begin_hour_text), int(begin_minutes_text))

    return datetime(
        datetime.today().year, begin_month, begin_day, begin_hour, begin_minutes
    )


def _parse_end(item: html.HtmlElement, begin: datetime) -> datetime:
    end_time_xpath = (
        ".//div[@class='event-time-item'"
        " and div[@class='event-time-label' and text()='Ende']]"
        "/div[@class='event-time-value']"
    )
    end_time_text: str = item.xpath(end_time_xpath)[0].text
    if end_time_text == "-:-":
        return begin + timedelta(minutes=90)

    (end_hour_text, end_minutes_text) = end_time_text.split(":")
    (end_hour, end_minutes) = (int(end_hour_text), int(end_minutes_text))
    return datetime(
        datetime.today().year, begin.month, begin.day, end_hour, end_minutes
    )


def _parse_meet(item: html.HtmlElement, begin: datetime) -> datetime:
    meet_time_xpath = (
        ".//div[@class='event-time-item'"
        " and div[@class='event-time-label' and text()='Treffen']]"
        "/div[@class='event-time-value']"
    )
    meet_time_text: str = item.xpath(meet_time_xpath)[0].text
    if meet_time_text == "-:-":
        return begin

    (meet_hour_text, meet_minutes_text) = meet_time_text.split(":")
    (meet_hour, meet_minutes) = (int(meet_hour_text), int(meet_minutes_text))
    return datetime(
        datetime.today().year, begin.month, begin.day, meet_hour, meet_minutes
    )


def parse_event_year(html_text: str) -> int:
    dom = html.fromstring(html_text)
    xpath = "//title"
    title: str = typing.cast(html.HtmlElement, dom.xpath(xpath))[0].text
    year = title[-4:]
    return int(year)
