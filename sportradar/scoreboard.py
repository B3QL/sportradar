from uuid import uuid4, UUID
from dataclasses import dataclass, field
from copy import deepcopy

@dataclass
class Match:
    """Data related to single match"""
    home_team: str
    away_team: str
    mid: UUID = field(default_factory=uuid4)
    score: tuple[int, int] = (0, 0)

    def __lt__(self, other: 'Match') -> bool:
        """Compare matches"""
        return sum(self.score) < sum(other.score)

    def __str__(self) -> str:
        """Return string representation"""
        return f'{self.home_team} {self.score[0]} - {self.away_team} {self.score[1]}'

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
        return deepcopy(sorted(most_recent, reverse=True))

    def add(self, home_team: str, away_team: str) -> UUID:
        """Add new match to score board"""
        new_match = Match(home_team, away_team)
        self._matches[new_match.mid] = new_match
        return new_match.mid

    def update_score(self, match_id: UUID, home_score: int, away_score: int):
        """Update score of specific match"""
        if home_score < 0 or away_score < 0:
            raise ValueError("score must not be negative")

        self._matches[match_id].score = (home_score, away_score)

    def remove(self, match_id: UUID):
        """Remove match from scoreboard"""
        try:
            del self._matches[match_id]
        except KeyError:
            raise RuntimeError("match does not exist")

    def team_score(self, name: str) -> int:
        """Fetch score for single team"""
        scores = [
            (m.home_team, m.away_team, m.score)
            for m in self._matches.values() if m.home_team == name or m.away_team == name
        ]

        if not scores:
            raise ValueError('match does not exit')

        (home_team, away_team, score), = scores

        if home_team == name:
            return score[0]

        if away_team == name:
            return score[1]




    def __str__(self) -> str:
        """Return string representation"""
        matches = [f"{pos}. {match}" for pos, match in enumerate(self.summary, start=1)]
        return "\n".join(matches)