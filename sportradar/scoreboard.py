from uuid import uuid4, UUID
from dataclasses import dataclass, field

@dataclass
class Match:
    """Data related to single match"""
    mid: UUID = field(default_factory=uuid4)
    score: tuple[int, int] = (0, 0)


class ScoreBoard:
    def __init__(self):
        """Create in-memory storage"""
        self._matches = {}

    @property
    def summary(self) -> list[Match]:
        """Return summary of ongoing matches"""
        return list(self._matches.values())

    def add(self, home_team: str, away_team: str) -> UUID:
        """Add new match to score board"""
        new_match = Match()
        self._matches[new_match.mid] = new_match
        return new_match.mid

    def update_score(self, match_id: UUID, home_score: int, away_score: int):
        """Update score of specific match"""
        self._matches[match_id].score = (home_score, away_score)
