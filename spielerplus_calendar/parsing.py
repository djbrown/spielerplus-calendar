import json
import re
from datetime import datetime, timedelta

from lxml import html


def parse_event_calendar(html: str) -> list:
    pattern = (
        r'^        },"locale":"de","firstDay":1,"events":(\[.*\]),'
        r'"allDayDefault":true,"eventRender":    \(function\(event, element\) {$'
    )
    result: re.Match[str] | None = re.search(pattern, html, re.MULTILINE)
    if result is None:
        raise Exception("Could not parse calendar html")
    data = result.group(1)
    return json.loads(data)


def parse_timestamp(timestamp: str) -> datetime:
    return datetime.fromisoformat(timestamp[:-1])  # stip trailing Z


def parse_event_list_items(html_text: str) -> list[dict]:

    dom = html.fromstring(html_text)
    items: list[html.HtmlElement] = dom.xpath(
        "//div[@class='list event' and .//button[@class='participation-button selected' and @title = 'Zugesagt']]"
    )

    return [_parse_event_list_item(item) for item in items]


def _parse_event_list_item(item: html.HtmlElement) -> dict:
    id_xpath = ".//div[@class='panel']"
    id: str = item.xpath(id_xpath)[0].attrib.get("id")

    title_xpath = ".//div[@class='panel-heading-text']/div[@class='panel-title']"
    title: str = item.xpath(title_xpath)[0].text

    (start, end) = _parse_datetimes(item)

    url_xpath = ".//a[@class='event-header-border']"
    url: str = item.xpath(url_xpath)[0].attrib.get("href")

    return {"id": id, "title": title, "start": start, "end": end, "url": url}


def _parse_datetimes(item: html.HtmlElement) -> tuple[datetime, datetime]:
    begin_date_xpath = (
        ".//div[@class='panel-heading-info']/div[@class='panel-subtitle']"
    )
    begin_date_text: str = item.xpath(begin_date_xpath)[0].text
    (begin_day, begin_month) = begin_date_text.split(".")
    (begin_day, begin_month) = (int(begin_day), int(begin_month))

    begin_time_xpath = ".//div[@class='event-time-item' and div[@class='event-time-label' and text()='Beginn']]/div[@class='event-time-value']"
    begin_time_text: str = item.xpath(begin_time_xpath)[0].text
    (begin_hour, begin_minutes) = begin_time_text.split(":")
    (begin_hour, begin_minutes) = (int(begin_hour), int(begin_minutes))

    begin: datetime = datetime(
        datetime.today().year, begin_month, begin_day, begin_hour, begin_minutes
    )

    end_time_xpath = ".//div[@class='event-time-item' and div[@class='event-time-label' and text()='Ende']]/div[@class='event-time-value']"
    end_time_text: str = item.xpath(end_time_xpath)[0].text
    if end_time_text == "-:-":
        end = begin + timedelta(minutes=90)
    else:
        (end_hour, end_minutes) = end_time_text.split(":")
        (end_hour, end_minutes) = (int(end_hour), int(end_minutes))
        end: datetime = datetime(
            datetime.today().year, begin_month, begin_day, end_hour, end_minutes
        )

    meet_time_xpath = ".//div[@class='event-time-item' and div[@class='event-time-label' and text()='Treffen']]/div[@class='event-time-value']"
    meet_time_text: str = item.xpath(meet_time_xpath)[0].text
    if meet_time_text == "-:-":
        start = begin
    else:
        (meet_hour, meet_minutes) = meet_time_text.split(":")
        (meet_hour, meet_minutes) = (int(meet_hour), int(meet_minutes))
        start: datetime = datetime(
            datetime.today().year, begin_month, begin_day, meet_hour, meet_minutes
        )

    return (start, end)
