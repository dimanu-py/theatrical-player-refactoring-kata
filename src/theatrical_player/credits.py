import math
from abc import ABC, abstractmethod


class Credits:

    def __init__(self, initial_credits: float) -> None:
        self._credits = initial_credits

    def add(self, other: "Credits") -> "Credits":
        return Credits(self._credits + other._credits)

    def __eq__(self, other: "Credits") -> bool:
        return self._credits == other._credits

    def __str__(self) -> str:
        return f"{math.floor(self._credits)}"


class CreditsCalculationStrategy(ABC):

    @abstractmethod
    def credits(self, audience: int) -> Credits:
        """Calculate play's credits"""


class NoExtraCredits(CreditsCalculationStrategy):

    def credits(self, audience: int) -> Credits:
        return Credits(0)


class AudienceBasedCredits(CreditsCalculationStrategy):

    def credits(self, audience: int) -> Credits:
        return Credits(audience / 5)
