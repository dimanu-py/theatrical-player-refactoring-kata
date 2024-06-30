from src.theatrical_player.credits import Credits
from src.theatrical_player.invoice import Invoice
from src.theatrical_player.money import Money
from src.theatrical_player.performance import Performance
from src.theatrical_player.play import Play, PlaysCatalog


class StatementPrinter:

    def __init__(self) -> None:
        self.invoice_money = Money(initial_amount=0)
        self.invoice_credits = Credits(initial_credits=0)

    def print(self, invoice: Invoice, catalog: PlaysCatalog):
        result = f'Statement for {invoice.customer}\n'

        for performance in invoice.performances:
            play = catalog.by_id(performance.play_id)

            performance_amount = self.compute_performance_amount(performance, play)
            performance_credits = performance.compute_credits(play)

            self.invoice_credits = self.invoice_credits.add(performance_credits)
            self.invoice_money = self.invoice_money.add(performance_amount)

            # print line for this order
            result += f' {play.name}: {performance_amount.as_dollar()} ({performance.audience} seats)\n'

        result += f'Amount owed is {self.invoice_money.as_dollar()}\n'
        result += f'You earned {self.invoice_credits} credits\n'
        return result

    def compute_performance_amount(self, performance: Performance, play: Play) -> Money:
        if play.genre == "tragedy":
            performance_amount = Money(40000)
            performance_amount = performance_amount.add(performance.tragedy_extra_amount_by_audience())
            performance_amount = performance_amount.add(performance.tragedy_extra_amount())
            return performance_amount

        if play.genre == "comedy":
            performance_amount = Money(30000)
            performance_amount = performance_amount.add(performance.comedy_extra_amount_by_audience())
            performance_amount = performance_amount.add(performance.comedy_extra_amount())
            return performance_amount

        raise ValueError(f'unknown type: {play.genre}')

