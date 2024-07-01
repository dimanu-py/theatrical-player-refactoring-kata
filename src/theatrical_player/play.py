import math

from src.theatrical_player.credits import Credits
from src.theatrical_player.money import Money


class Play:

    def __init__(self, name: str, genre: str) -> None:
        self.name = name
        self.genre = genre

    def credits(self, audience: int) -> Credits:
        return Credits(math.floor(audience / 5)) if self.genre == "comedy" else Credits(0)

    def comedy_amount(self, audience: int) -> Money:
        performance_amount = Money(30000)
        performance_amount = performance_amount.add(self._comedy_extra_amount_by_audience(audience))
        performance_amount = performance_amount.add(self._comedy_extra_amount_by_genre(audience))
        return performance_amount

    def tragedy_amount(self, audience: int) -> Money:
        performance_amount = Money(40000)
        performance_amount = performance_amount.add(self._tragedy_extra_amount_by_audience(audience))
        performance_amount = performance_amount.add(self._tragedy_extra_amount_by_genre())
        return performance_amount

    @staticmethod
    def _tragedy_extra_amount_by_genre() -> Money:
        return Money(0)

    @staticmethod
    def _tragedy_extra_amount_by_audience(audience):
        return Money(1000 * (audience - 30)) if audience > 30 else Money(0)

    @staticmethod
    def _comedy_extra_amount_by_genre(audience):
        return Money(300 * audience)

    @staticmethod
    def _comedy_extra_amount_by_audience(audience):
        return Money(10000 + 500 * (audience - 20)) if audience > 20 else Money(0)


class PlaysCatalog:

    def __init__(self, catalog: dict[str, Play]) -> None:
        self.catalog = catalog
    def by_id(self, play_id: str) -> Play:
        return self.catalog.get(play_id)
