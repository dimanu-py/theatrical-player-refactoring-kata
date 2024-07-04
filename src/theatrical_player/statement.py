from src.theatrical_player.money import Money


class Statement:

    def __init__(self) -> None:
        self.cost: float = 0.0
        self.credits: int = 0
        self.customer: str = ""
        self.lines: str = ""
        self.temporary_lines: str = ""

    def fill(self, tag: str, value) -> None:
        if tag == "customer":
            self._fill_customer(value)
        elif tag == "credits":
            self._fill_credits(value)
        elif tag == "cost":
            self._fill_cost(value)

    def _fill_cost(self, value: Money) -> None:
        self.cost = value.as_dollar()

    def _fill_credits(self, value: int) -> None:
        self.credits = value

    def _fill_customer(self, value: str) -> None:
        self.customer = value

    def fill_performance(self, play_name: str, cost: Money, audience: int) -> None:
        self.lines += f' {play_name}: {cost.as_dollar()} ({audience} seats)\n'

    def print(self) -> str:
        self.temporary_lines = f"Statement for {self.customer}\n"
        temp_result = self.temporary_lines + self.lines
        self.temporary_lines = f"Amount owed is {self.cost}\n"
        self.temporary_lines += f"You earned {self.credits} credits\n"
        return temp_result + self.temporary_lines
