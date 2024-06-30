import math
from typing import Iterable

from src.theatrical_player.credits import Credits
from src.theatrical_player.money import Money
from src.theatrical_player.play import Play


class Performance:

    def __init__(self, play_id: str, audience: int) -> None:
        self.play_id = play_id
        self.audience = audience

    def compute_credits(self, play: Play) -> Credits:
        initial_credits = Credits(max(self.audience - 30, 0))
        return initial_credits.add(self._extra_credits_by_genre(play))

    def _extra_credits_by_genre(self, play: Play) -> Credits:
        if "comedy" == play.genre:
            return Credits(math.floor(self.audience / 5))
        return Credits(0)

    def comedy_extra_amount(self) -> Money:
        return Money(300 * self.audience)

    def comedy_extra_amount_by_audience(self) -> Money:
        if self.audience > 20:
            return Money(10000 + 500 * (self.audience - 20))
        return Money(0)

    def tragedy_extra_amount(self) -> Money:
        return Money(0)

    def tragedy_extra_amount_by_audience(self) -> Money:
        if self.audience > 30:
            return Money(1000 * (self.audience - 30))
        return Money(0)


class PerformancesRepository:


    def __init__(self, performances: list[Performance]) -> None:
        self.performances = performances
    def __iter__(self) -> Iterable[Performance]:
        return iter(self.performances)
