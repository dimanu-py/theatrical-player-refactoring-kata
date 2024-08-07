from abc import abstractmethod, ABC
from enum import StrEnum

from src.theatrical_player.credits import Credits, CreditsCalculationStrategy, AudienceBasedCredits, NoExtraCredits
from src.theatrical_player.money import Money


class Genres(StrEnum):
    COMEDY = "comedy"
    TRAGEDY = "tragedy"


class Play(ABC):
    DEFAULT_CREDIT_STRATEGY = NoExtraCredits()

    def __init__(self, name: str) -> None:
        self.name = name
        self.credit_strategy: CreditsCalculationStrategy = self.DEFAULT_CREDIT_STRATEGY

    @classmethod
    def create(cls, name: str, genre: str) -> 'Play':
        if genre == Genres.COMEDY:
            return Comedy(name)
        if genre == Genres.TRAGEDY:
            return Tragedy(name)
        raise ValueError(f'unknown type: {genre}')

    def credits(self, audience: int) -> Credits:
        return self.credit_strategy.credits(audience)

    @abstractmethod
    def cost(self, audience: int) -> Money:
        """Calculate play's cost"""

    def title(self) -> str:
        return self.name


class Comedy(Play):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.credit_strategy = AudienceBasedCredits()

    def cost(self, audience: int) -> Money:
        base_cost = Money(30000)
        return base_cost.add(self._extra_cost_by_audience(audience))

    @staticmethod
    def _extra_cost_by_audience(audience: int) -> Money:
        always_applied_extra = Money(300 * audience)
        extra_cost_by_audience = Money(10000 + 500 * (audience - 20)) if audience > 20 else Money(0)
        return always_applied_extra.add(extra_cost_by_audience)


class Tragedy(Play):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.credit_strategy = NoExtraCredits()

    def cost(self, audience: int) -> Money:
        base_cost = Money(40000)
        return base_cost.add(self._extra_cost_by_audience(audience))

    @staticmethod
    def _extra_cost_by_audience(audience: int) -> Money:
        return Money(1000 * (audience - 30)) if audience > 30 else Money(0)
