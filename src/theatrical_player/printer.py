from src.theatrical_player.credits import Credits
from src.theatrical_player.invoice import Invoice
from src.theatrical_player.money import Money
from src.theatrical_player.play import PlaysCatalog
from src.theatrical_player.statement import Statement


class StatementPrinter:

    def __init__(self) -> None:
        self.invoice_money: Money = Money(initial_amount=0)
        self.invoice_credits: Credits = Credits(initial_credits=0)
        self.statement: Statement = Statement()

    def print(self, invoice: Invoice, catalog: PlaysCatalog):
        self.statement.fill_customer(invoice.customer)

        for performance in invoice.performances:
            play = catalog.by_id(performance.play_id)
            self.invoice_credits = self.invoice_credits.add(performance.credits(play))
            self.invoice_money = self.invoice_money.add(performance.cost(play))

            self.statement.fill_performance(play.name, performance.cost(play), performance.audience)

        self.statement.fill_invoice(self.invoice_money, self.invoice_credits)
        return self.statement.print()
