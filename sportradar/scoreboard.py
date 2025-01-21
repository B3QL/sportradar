from uuid import uuid4, UUID
from dataclasses import dataclass, field

@dataclass
class Match:
    """Data related to single match"""
    mid: UUID = field(default_factory=uuid4)
    score: tuple[int, int] = (0, 0)

    def __lt__(self, other: 'Match') -> bool:
        """Compare matches"""
        return sum(self.score) < sum(other.score)

class ScoreBoard:
    def __init__(self):
        """Create in-memory storage"""
        self._matches = {}

    @property
    def summary(self) -> list[Match]:
        """
        Return summary of ongoing matches

        ..note: The insertion order of dictionary values is guaranteed from Python 3.7
                and sorted is guaranteed to be stable as well.
        """
        most_recent = reversed(self._matches.values())
        return sorted(most_recent, reverse=True)

    def add(self, home_team: str, away_team: str) -> UUID:
        """Add new match to score board"""
        new_match = Match()
        self._matches[new_match.mid] = new_match
        return new_match.mid

    def update_score(self, match_id: UUID, home_score: int, away_score: int):
        """Update score of specific match"""
        self._matches[match_id].score = (home_score, away_score)

    def remove(self, match_id: UUID):
        """Remove match from scoreboard"""
        del self._matches[match_id]
