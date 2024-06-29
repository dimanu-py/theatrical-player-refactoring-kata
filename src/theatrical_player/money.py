class Money:

    def __init__(self, initial_amount: int) -> None:
        self._amount = initial_amount

    def add(self, other: "Money") -> "Money":
        return Money(self._amount + other._amount)

    def as_dollar(self) -> str:
        return f"${self._amount / 100:0,.2f}"

    def __eq__(self, other: "Money") -> bool:
        return self._amount == other._amount
