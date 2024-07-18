from abc import ABCMeta, abstractmethod
from collections import defaultdict
from typing import Any

from src.theatrical_player.money import Money


class Fillable(metaclass=ABCMeta):
    @abstractmethod
    def fill(self, tag, value):
        pass

    @abstractmethod
    def print(self):
        pass


class PlainTextStatement(Fillable):

    def __init__(self) -> None:
        self.lines: str = ""
        self.content: defaultdict[str, Any] = defaultdict(list)

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
        self.lines += f"Statement for {self.content["customer"]}\n"
        for performance in self.content["performance"]:
            self.lines += f" {performance['name']}: {performance['cost']} ({performance['audience']} seats)\n"
        self.lines += f"Amount owed is {self.content["cost"]}\n"
        self.lines += f"You earned {self.content["credits"]} credits\n"
        return self.lines

    def _fill_cost(self, value: Money) -> None:
        self.content["cost"] = value.as_dollar()

    def _fill_credits(self, value: int) -> None:
        self.content["credits"] = value

    def _fill_customer(self, value: str) -> None:
        self.content["customer"] = value

    def _fill_performance(self, play_name: str, cost: Money, audience: int) -> None:
        self.content["performance"].append({
            "name": play_name,
            "cost": cost.as_dollar(),
            "audience": audience
        })
