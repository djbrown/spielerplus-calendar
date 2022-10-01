import json
from pathlib import Path
from typing import NamedTuple


class Config(NamedTuple):
    identity: str
    team_name: str


def read_config(path="config.json") -> Config:
    return json.loads(
        Path(path).read_text(encoding="utf-8"),
        object_hook=lambda d: Config(**d),
    )
