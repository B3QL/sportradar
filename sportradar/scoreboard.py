class ScoreBoard:
    def __init__(self):
        """Create in-memory storage"""
        self._matches = []

    @property
    def summary(self) -> list[None]:
        """Return summary of ongoing matches"""
        return self._matches

    def add(self, home_team: str, away_team: str):
        """Add new match to score board"""
        self._matches.append(None)
