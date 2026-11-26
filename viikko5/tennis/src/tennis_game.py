class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    DEUCE_SCORE = 3
    MINIMUM_SCORE_TO_WIN = 4
    SCORE_DIFFERENCE_TO_WIN = 2

    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self._is_tied():
            return self._get_tied_score()

        if self._is_advantage_or_win():
            return self._get_advantage_or_win_score()

        return self._get_regular_score()

    def _is_tied(self):
        return self.player1_score == self.player2_score

    def _get_tied_score(self):
        if self.player1_score < self.FORTY:
            return f"{self.SCORE_NAMES[self.player1_score]}-All"

        return "Deuce"

    def _is_advantage_or_win(self):
        return (
            self.player1_score >= self.MINIMUM_SCORE_TO_WIN
            or self.player2_score >= self.MINIMUM_SCORE_TO_WIN
        )

    def _get_advantage_or_win_score(self):
        score_difference = self.player1_score - self.player2_score

        if score_difference == 1:
            return f"Advantage {self.player1_name}"

        if score_difference == -1:
            return f"Advantage {self.player2_name}"

        if score_difference >= self.SCORE_DIFFERENCE_TO_WIN:
            return f"Win for {self.player1_name}"

        return f"Win for {self.player2_name}"

    def _get_regular_score(self):
        player1_score_name = self.SCORE_NAMES[self.player1_score]
        player2_score_name = self.SCORE_NAMES[self.player2_score]

        return f"{player1_score_name}-{player2_score_name}"

