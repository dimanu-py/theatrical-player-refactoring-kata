from typing import Iterable

from src.theatrical_player.credits import Credits
from src.theatrical_player.money import Money
from src.theatrical_player.play import Play
from src.theatrical_player.statement import Fillable


class Performance:

    def __init__(self, play: Play, audience: int) -> None:
        self.audience = audience
        self.play = play

    def credits(self) -> Credits:
        initial_credits = Credits(max(self.audience - 30, 0))
        return initial_credits.add(self.play.credits(self.audience))

    def cost(self) -> Money:
        return self.play.cost(self.audience)

    def fill(self, fillable: Fillable) -> None:
        fillable.fill(
            "performance",
            {
                "name": self._title(),
                "cost": self.cost(),
                "audience": self.audience
            }
        )

    def _title(self) -> str:
        return self.play.title()


class PerformancesRepository:

    def __init__(self, performances: list[Performance]) -> None:
        self.performances = performances

    def __iter__(self) -> Iterable[Performance]:
        return iter(self.performances)
