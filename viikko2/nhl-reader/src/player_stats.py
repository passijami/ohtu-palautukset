"""Statistics and rankings for NHL players."""

class PlayerStats:
    """Provide statistics calculated from players returned by a reader."""

    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_by_nationality(self, nationality):
        """Return players of a nationality, ranked by points."""
        players = []

        for player in self.players:
            if player.nationality == nationality:
                players.append(player)

        players.sort(
            key=lambda player: player.goals + player.assists,
            reverse=True
        )

        return players

    def top_by_team(self, team):
        """Return players from a team, ranked by points."""
        players = []

        for player in self.players:
            if player.team == team:
                players.append(player)

        players.sort(
            key=lambda player: player.goals + player.assists,
            reverse=True
        )

        return players

    def top_goal_scorers(self, how_many):
        """Return up to how_many players, ranked by goals scored."""
        players = sorted(self.players, key=lambda player: player.goals, reverse=True)

        return players[:how_many]
