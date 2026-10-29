import sys
import unittest
from pathlib import Path

# Lisätään src-hakemisto Pythonin hakupolkuun.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from statistics_service import StatisticsService
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
        player = self.stats.search("Unknown")
        self.assertIsNone(player)

    def test_team_returns_players_of_requested_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_team_returns_empty_list_when_team_not_found(self):
        players = self.stats.team("XXX")
        self.assertEqual(players, [])

    def test_top_returns_players_in_points_order(self):
        players = self.stats.top(3)
        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )
        self.assertEqual(
            [player.points for player in players],
            [124, 99, 98]
        )

    def test_top_zero_returns_empty_list(self):
        players = self.stats.top(0)
        self.assertEqual(players, [])


if __name__ == "__main__":
    unittest.main()
