from spielerplus_calendar import config


def test_filter_items():
    target = config.Config(
        server="http://localhost:50001",
        team_name="HSG Blau-Weiß 22/23",
    )

    actual = config.from_file("tests/data/config.json")

    assert actual == target
