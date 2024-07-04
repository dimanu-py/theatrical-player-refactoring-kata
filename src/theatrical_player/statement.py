from abc import ABCMeta, abstractmethod
from typing import Any

from src.theatrical_player.money import Money


class Fillable(metaclass=ABCMeta):
    @abstractmethod
    def fill(self, tag, value):
        pass

    @abstractmethod
    def print(self):
        pass


class Statement(Fillable):

    def __init__(self) -> None:
        self.cost: float = 0.0
        self.credits: int = 0
        self.customer: str = ""
        self.performance: list[dict[str, Any]] = []
        self.lines: str = ""

    def fill(self, tag: str, value) -> None:
        if tag == "customer":
            self._fill_customer(value)
        elif tag == "credits":
            self._fill_credits(value)
        elif tag == "cost":
            self._fill_cost(value)
        elif tag == "performance":
            self._fill_performance(value["name"], value["cost"], value["audience"])
        else:
            raise ValueError(f"Unknown tag: {tag}")

    def print(self) -> str:
        self.lines += f"Statement for {self.customer}\n"
        for performance in self.performance:
            self.lines += f" {performance['name']}: {performance['cost']} ({performance['audience']} seats)\n"
        self.lines += f"Amount owed is {self.cost}\n"
        self.lines += f"You earned {self.credits} credits\n"
        return self.lines

    def _fill_cost(self, value: Money) -> None:
        self.cost = value.as_dollar()

    def _fill_credits(self, value: int) -> None:
        self.credits = value

    def _fill_customer(self, value: str) -> None:
        self.customer = value

    def _fill_performance(self, play_name: str, cost: Money, audience: int) -> None:
        self.performance.append(
            {
                "name": play_name,
                "cost": cost.as_dollar(),
                "audience": audience
            }
        )
