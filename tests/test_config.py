from spielerplus_calendar import config


def test_from_file():
    target = config.Config(
        server="http://localhost:50001",
        teams=[
            config.TeamConfig(
                identity=(
                    'some:3:{d:2;o:5:"_identity";l:6;x:85:"'
                    '[13245,"54qwe5wew8e7-687qweLq",23432,"65719",null]";}'
                ),
                name="HSG Blau-Weiß 22/23",
            ),
            config.TeamConfig(
                identity=(
                    'some:3:{d:2;o:5:"_identity";l:6;x:85:"'
                    '[67890,"564sasffds56-Gz72Jw57",23432,"65719",null]";}'
                ),
                name="Some Team Name",
            ),
        ],
    )

    actual = config.from_file("tests/data/config.json")

    assert actual == target
