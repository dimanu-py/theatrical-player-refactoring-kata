from typing import Iterable

from src.theatrical_player.credits import Credits
from src.theatrical_player.money import Money
from src.theatrical_player.play import Play


class Performance:

    def __init__(self, play_id: str, audience: int) -> None:
        self.play_id = play_id
        self.audience = audience

    def credits(self, play: Play) -> Credits:
        initial_credits = Credits(max(self.audience - 30, 0))
        return initial_credits.add(play.credits(self.audience))

    def amount(self, play: Play) -> Money:
        if play.genre == "tragedy":
            performance_amount = Money(40000)
            performance_amount = performance_amount.add(self._tragedy_extra_amount_by_audience())
            performance_amount = performance_amount.add(self._tragedy_extra_amount())
            return performance_amount

        if play.genre == "comedy":
            performance_amount = Money(30000)
            performance_amount = performance_amount.add(self._comedy_extra_amount_by_audience())
            performance_amount = performance_amount.add(self._comedy_extra_amount())
            return performance_amount

        raise ValueError(f'unknown type: {play.genre}')

    def _comedy_extra_amount(self) -> Money:
        return Money(300 * self.audience)

    def _comedy_extra_amount_by_audience(self) -> Money:
        return Money(10000 + 500 * (self.audience - 20)) if self.audience > 20 else Money(0)

    def _tragedy_extra_amount(self) -> Money:
        return Money(0)

    def _tragedy_extra_amount_by_audience(self) -> Money:
        return Money(1000 * (self.audience - 30)) if self.audience > 30 else Money(0)


class PerformancesRepository:

    def __init__(self, performances: list[Performance]) -> None:
        self.performances = performances

    def __iter__(self) -> Iterable[Performance]:
        return iter(self.performances)
