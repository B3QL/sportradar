from dataclasses import dataclass

@dataclass
class Match:
    """Data related to single match"""
    score: tuple[int, int] = (0, 0)


class ScoreBoard:
    def __init__(self):
        """Create in-memory storage"""
        self._matches = []

    @property
    def summary(self) -> list[Match]:
        """Return summary of ongoing matches"""
        return self._matches

    def add(self, home_team: str, away_team: str):
        """Add new match to score board"""
        new_match = Match()
        self._matches.append(new_match)
