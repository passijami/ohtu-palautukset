import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()

        print(type(response))
        print(response if isinstance(response, dict) else response[0])

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players
