"""Player model for NHL statistics."""

class Player:
    """Represent a player and their season statistics."""
    # This data model intentionally exposes attributes and a string representation.
    # pylint: disable=too-few-public-methods

    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.nationality = player_dict["nationality"]
        self.team = player_dict["team"]
        self.goals = player_dict["goals"]
        self.assists = player_dict["assists"]

    def __str__(self):
        """Return a readable summary of the player."""
        return (
            f"{self.name} team {self.team} "
            f"goals {self.goals} assists {self.assists}"
        )
