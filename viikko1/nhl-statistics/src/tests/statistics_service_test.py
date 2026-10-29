import sys
import unittest
from pathlib import Path

# Lisätään src-hakemisto Pythonin hakupolkuun.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Lemieux")
        self.assertEqual(player.name, "Lemieux")

    def test_search_returns_none_when_player_not_found(self):
        self.assertIsNone(self.stats.search("Unknown"))

    def test_team_returns_players_of_requested_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_team_returns_empty_list_when_team_not_found(self):
        self.assertEqual(self.stats.team("XXX"), [])

    def test_top_defaults_to_points(self):
        players = self.stats.top(3)
        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_top_by_points(self):
        players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_top_by_goals(self):
        players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman", "Kurri"]
        )

    def test_top_by_assists(self):
        players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Yzerman", "Lemieux"]
        )

    def test_top_zero_returns_empty_list(self):
        self.assertEqual(self.stats.top(0), [])


if __name__ == "__main__":
    unittest.main()
