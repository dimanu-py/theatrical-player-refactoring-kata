import math
from typing import Iterable

from src.theatrical_player.credits import Credits
from src.theatrical_player.play import Play


class Performance:

    def __init__(self, play_id: str, audience: int) -> None:
        self.play_id = play_id
        self.audience = audience

    def extra_credits_by_genre(self, play: Play) -> Credits:
        if "comedy" == play.genre:
            return Credits(math.floor(self.audience / 5))
        return Credits(0)


class PerformancesRepository:

    def __init__(self, performances: list[Performance]) -> None:
        self.performances = performances

    def __iter__(self) -> Iterable[Performance]:
        return iter(self.performances)
