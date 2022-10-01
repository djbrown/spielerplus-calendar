import json
from pathlib import Path
from typing import NamedTuple


class Config(NamedTuple):
    server: str
    team_name: str


def from_file(path="config.json") -> Config:
    return json.loads(
        Path(path).read_text("utf-8"),
        object_hook=lambda d: Config(**d),
    )
