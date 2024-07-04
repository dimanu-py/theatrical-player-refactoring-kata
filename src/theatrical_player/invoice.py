from src.theatrical_player.credits import Credits
from src.theatrical_player.money import Money
from src.theatrical_player.performance import PerformancesRepository
from src.theatrical_player.play import PlaysCatalog
from src.theatrical_player.statement import Statement


class Invoice:

    def __init__(self, customer: str, performances: PerformancesRepository) -> None:
        self.customer = customer
        self.performances = performances
        self.invoice_money: Money = Money(initial_amount=0)
        self.invoice_credits: Credits = Credits(initial_credits=0)

    def fill(self, statement: Statement, catalog: PlaysCatalog) -> None:
        statement.fill_customer(self.customer)

        for performance in self.performances:
            play = catalog.by_id(performance.play_id)
            statement.fill_performance(play.name, performance.cost(play), performance.audience)

        statement.fill_invoice(self._cost(catalog), self._credits(catalog))

    def _cost(self, catalog: PlaysCatalog) -> Money:
        for performance in self.performances:
            play = catalog.by_id(performance.play_id)
            self.invoice_money = self.invoice_money.add(performance.cost(play))
        return self.invoice_money

    def _credits(self, catalog: PlaysCatalog) -> Credits:
        for performance in self.performances:
            play = catalog.by_id(performance.play_id)
            self.invoice_credits = self.invoice_credits.add(performance.credits(play))
        return self.invoice_credits
