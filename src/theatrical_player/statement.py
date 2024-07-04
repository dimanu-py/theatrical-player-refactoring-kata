from src.theatrical_player.credits import Credits
from src.theatrical_player.money import Money


class Statement:

    def __init__(self) -> None:
        self.data: dict[str, str | int] = {}
        self.lines: str = ""
        self.temporary_lines: str = ""

    def fill(self, tag: str, value) -> None:
        if tag == "customer":
            self._fill_customer(value)

    def _fill_customer(self, value: str) -> None:
        self.data["customer"] = value

    def fill_performance(self, play_name: str, cost: Money, audience: int) -> None:
        self.lines += f' {play_name}: {cost.as_dollar()} ({audience} seats)\n'

    def fill_invoice(self, money: Money, credits: Credits) -> None:
        self.lines += f'Amount owed is {money.as_dollar()}\n'
        self.lines += f'You earned {credits} credits\n'

    def print(self) -> str:
        self.temporary_lines += f"Statement for {self.data['customer']}\n"
        return self.temporary_lines + self.lines
