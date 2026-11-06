"""Unit tests for PlayerStats using an offline player-reader stub."""

import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    """Return a fixed set of players without making network requests."""
    # The stub intentionally exposes only the reader method used by PlayerStats.
    # pylint: disable=too-few-public-methods

    def get_players(self):
        """Return the players used by these tests."""
        return [
            Player({
                "name": "Semenko",
                "nationality": "CAN",
                "team": "EDM",
                "goals": 4,
                "assists": 12
            }),
            Player({
                "name": "Lemieux",
                "nationality": "CAN",
                "team": "PIT",
                "goals": 45,
                "assists": 54
            }),
            Player({
                "name": "Kurri",
                "nationality": "FIN",
                "team": "EDM",
                "goals": 37,
                "assists": 53
            }),
            Player({
                "name": "Yzerman",
                "nationality": "CAN",
                "team": "DET",
                "goals": 42,
                "assists": 56
            }),
            Player({
                "name": "Gretzky",
                "nationality": "CAN",
                "team": "EDM",
                "goals": 35,
                "assists": 89
            })
        ]


class TestPlayerStats(unittest.TestCase):
    """Test player filtering and ranking using local fixture data."""

    def setUp(self):
        """Create PlayerStats with the offline stub reader."""
        self.stats = PlayerStats(PlayerReaderStub())

    def test_top_by_nationality_filters_and_sorts_by_points(self):
        """Filter by nationality and rank matching players by points."""
        players = self.stats.top_by_nationality("CAN")

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman", "Semenko"]
        )

    def test_top_by_team_filters_and_sorts_by_points(self):
        """Filter by team and rank matching players by points."""
        players = self.stats.top_by_team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Kurri", "Semenko"]
        )

    def test_top_goal_scorers_limits_and_sorts_by_goals(self):
        """Limit the results and rank players by goals scored."""
        players = self.stats.top_goal_scorers(3)

        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman", "Kurri"]
        )

    def test_top_goal_scorers_returns_all_available_if_limit_is_larger(self):
        """Return all available players when the limit exceeds the count."""
        players = self.stats.top_goal_scorers(10)

        self.assertEqual(len(players), 5)
        self.assertEqual(players[0].name, "Lemieux")


if __name__ == "__main__":
    unittest.main()
