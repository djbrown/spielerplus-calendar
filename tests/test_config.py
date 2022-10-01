from spielerplus_calendar import config


def test_filter_items():
    target = config.Config(
        identity=(
            'some:3:{d:2;o:5:"_identity";l:6;x:85:"'
            '[13245,"54qwe5wew8e7-687qweLq",23432,"65719",null]";}'
        ),
        team_name="HSG Blau-Weiß 22/23",
    )

    actual = config.from_file("tests/data/config.json")

    assert actual == target
