import math
from abc import abstractmethod, ABC

from src.theatrical_player.credits import Credits
from src.theatrical_player.money import Money


class Play(ABC):

    def __init__(self, name: str, genre: str) -> None:
        self.name = name
        self.genre = genre

    @classmethod
    def create(cls, name: str, genre: str) -> 'Play':
        if genre == "comedy":
            return Comedy(name, genre)
        if genre == "tragedy":
            return Tragedy(name, genre)
        raise ValueError(f'unknown type: {genre}')

    @abstractmethod
    def credits(self, audience: int) -> Credits:
        """Calculate play's credits"""

    @abstractmethod
    def cost(self, audience: int) -> Money:
        """Calculate play's cost"""


class Comedy(Play):

    def credits(self, audience: int) -> Credits:
        return Credits(math.floor(audience / 5))

    def cost(self, audience: int) -> Money:
        base_cost = Money(30000)
        return base_cost.add(self._extra_cost_by_audience(audience))

    @staticmethod
    def _extra_cost_by_audience(audience: int) -> Money:
        always_applied_extra = Money(300 * audience)
        extra_cost_by_audience = Money(10000 + 500 * (audience - 20)) if audience > 20 else Money(0)
        return always_applied_extra.add(extra_cost_by_audience)


class Tragedy(Play):

    def credits(self, audience: int) -> Credits:
        return Credits(0)

    def cost(self, audience: int) -> Money:
        base_cost = Money(40000)
        return base_cost.add(self._extra_cost_by_audience(audience))

    @staticmethod
    def _extra_cost_by_audience(audience: int) -> Money:
        return Money(1000 * (audience - 30)) if audience > 30 else Money(0)


class PlaysCatalog:

    def __init__(self, catalog: dict[str, Play]) -> None:
        self.catalog = catalog

    def by_id(self, play_id: str) -> Play:
        return self.catalog.get(play_id)
