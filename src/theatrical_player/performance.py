from typing import Iterable

from src.theatrical_player.credits import Credits
from src.theatrical_player.money import Money
from src.theatrical_player.play import PlaysCatalog
from src.theatrical_player.statement import Fillable


class Performance:

    def __init__(self, play_id: str, audience: int, catalog: PlaysCatalog) -> None:
        self.audience = audience
        self.catalog = catalog
        self.play = catalog.by_id(play_id)

    def credits(self) -> Credits:
        play = self.catalog.by_id(self.play_id)
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
