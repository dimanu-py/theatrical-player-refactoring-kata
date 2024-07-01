from src.theatrical_player.credits import Credits
from src.theatrical_player.invoice import Invoice
from src.theatrical_player.money import Money
from src.theatrical_player.performance import Performance
from src.theatrical_player.play import PlaysCatalog, Play


class Statement:

    def __init__(self) -> None:
        self.lines: str = ""

    def fill_customer(self, invoice: Invoice) -> None:
        self.lines += f'Statement for {invoice.customer}\n'

    def fill_performance(self, play: Play, performance: Performance) -> None:
        self.lines += f' {play.name}: {performance.cost(play).as_dollar()} ({performance.audience} seats)\n'

    def fill_invoice(self, money: Money, credits: Credits) -> None:
        self.lines += f'Amount owed is {money.as_dollar()}\n'
        self.lines += f'You earned {credits} credits\n'

    def print(self) -> str:
        return self.lines


class StatementPrinter:

    def __init__(self) -> None:
        self.invoice_money: Money = Money(initial_amount=0)
        self.invoice_credits: Credits = Credits(initial_credits=0)
        self.statement: Statement = Statement()

    def print(self, invoice: Invoice, catalog: PlaysCatalog):
        self.statement.fill_customer(invoice)

        for performance in invoice.performances:

            play = catalog.by_id(performance.play_id)
            self.invoice_credits = self.invoice_credits.add(performance.credits(play))
            self.invoice_money = self.invoice_money.add(performance.cost(play))

            self.statement.fill_performance(play, performance)

        self.statement.fill_invoice(self.invoice_money, self.invoice_credits)
        return self.statement.print()
