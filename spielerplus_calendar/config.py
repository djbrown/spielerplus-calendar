import json
from pathlib import Path
from typing import NamedTuple


class TeamConfig(NamedTuple):
    name: str
    identity: str


class Config(NamedTuple):
    server: str
    teams: list[TeamConfig]


def parse_config(data):
    if "name" in data.keys():
        return TeamConfig(**data)
    if "server" in data.keys():
        return Config(**data)
    return data


def from_file(path="config.json") -> Config:
    return json.loads(Path(path).read_text("utf-8"), object_hook=parse_config)
