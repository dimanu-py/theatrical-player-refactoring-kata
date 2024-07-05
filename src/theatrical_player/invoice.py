from src.theatrical_player.credits import Credits
from src.theatrical_player.money import Money
from src.theatrical_player.performance import PerformancesRepository
from src.theatrical_player.statement import Fillable


class Invoice:

    def __init__(self, customer: str, performances: PerformancesRepository) -> None:
        self.customer = customer
        self.performances = performances
        self._cost: Money = Money(initial_amount=0)
        self._credits: Credits = Credits(initial_credits=0)

    def fill(self, fillable: Fillable) -> None:
        fillable.fill("customer", self.customer)

        for performance in self.performances:
            performance.fill(fillable)

        fillable.fill("cost", self.cost())
        fillable.fill("credits", self.credits())

    def cost(self) -> Money:
        for performance in self.performances:
            self._cost = self._cost.add(performance.cost())
        return self._cost

    def credits(self) -> Credits:
        for performance in self.performances:
            self._credits = self._credits.add(performance.credits())
        return self._credits
