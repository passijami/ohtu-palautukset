"""Read NHL player data from a remote JSON endpoint."""

import requests
from player import Player

class PlayerReader:
    """Fetch and convert player data from a URL."""
    # This class intentionally has a single operation for reading players.
    # pylint: disable=too-few-public-methods

    def __init__(self, url):
        self.url = url

    def get_players(self):
        """Return the players provided by the configured endpoint."""
        response = requests.get(self.url, timeout=10).json()

        print(type(response))
        print(response if isinstance(response, dict) else response[0])

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players
