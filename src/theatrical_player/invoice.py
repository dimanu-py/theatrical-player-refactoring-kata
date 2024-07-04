from src.theatrical_player.credits import Credits
from src.theatrical_player.money import Money
from src.theatrical_player.performance import PerformancesRepository
from src.theatrical_player.play import PlaysCatalog
from src.theatrical_player.statement import Statement


class Invoice:

    def __init__(self, customer: str, performances: PerformancesRepository) -> None:
        self.customer = customer
        self.performances = performances
        self._cost: Money = Money(initial_amount=0)
        self._credits: Credits = Credits(initial_credits=0)

    def fill(self, statement: Statement, catalog: PlaysCatalog) -> None:
        statement.fill("customer", self.customer)

        for performance in self.performances:
            play = catalog.by_id(performance.play_id)
            statement.fill_performance(play.name, performance.cost(play), performance.audience)

        statement.fill_invoice(self.cost(catalog), self.credits(catalog))

    def cost(self, catalog: PlaysCatalog) -> Money:
        for performance in self.performances:
            play = catalog.by_id(performance.play_id)
            self._cost = self._cost.add(performance.cost(play))
        return self._cost

    def credits(self, catalog: PlaysCatalog) -> Credits:
        for performance in self.performances:
            play = catalog.by_id(performance.play_id)
            self._credits = self._credits.add(performance.credits(play))
        return self._credits
