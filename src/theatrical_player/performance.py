from typing import Iterable

from src.theatrical_player.credits import Credits
from src.theatrical_player.money import Money
from src.theatrical_player.play import PlaysCatalog
from src.theatrical_player.statement import Fillable


class Performance:

    def __init__(self, play_id: str, audience: int, catalog: PlaysCatalog) -> None:
        self.play_id = play_id
        self.audience = audience
        self.catalog = catalog

    def credits(self) -> Credits:
        play = self.catalog.by_id(self.play_id)
        initial_credits = Credits(max(self.audience - 30, 0))
        return initial_credits.add(play.credits(self.audience))

    def cost(self) -> Money:
        play = self.catalog.by_id(self.play_id)
        return play.cost(self.audience)

    def fill(self, fillable: Fillable) -> None:
        fillable.fill(
            "performance",
            {
                "name": self._title(self.catalog),
                "cost": self.cost(),
                "audience": self.audience
            }
        )

    def _title(self, catalog: PlaysCatalog) -> str:
        play = catalog.by_id(self.play_id)
        return play.title()


class PerformancesRepository:

    def __init__(self, performances: list[Performance]) -> None:
        self.performances = performances

    def __iter__(self) -> Iterable[Performance]:
        return iter(self.performances)
