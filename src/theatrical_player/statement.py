from src.theatrical_player.credits import Credits
from src.theatrical_player.invoice import Invoice
from src.theatrical_player.money import Money
from src.theatrical_player.play import PlaysCatalog


class StatementPrinter:

    def __init__(self) -> None:
        self.invoice_money = Money(initial_amount=0)
        self.invoice_credits = Credits(initial_credits=0)

    def print(self, invoice: Invoice, catalog: PlaysCatalog):
        result = f'Statement for {invoice.customer}\n'

        for performance in invoice.performances:
            play = catalog.by_id(performance.play_id)

            performance_amount = performance.compute_amount(play)
            performance_credits = performance.compute_credits(play)

            self.invoice_credits = self.invoice_credits.add(performance_credits)
            self.invoice_money = self.invoice_money.add(performance_amount)

            # print line for this order
            result += f' {play.name}: {performance_amount.as_dollar()} ({performance.audience} seats)\n'

        result += f'Amount owed is {self.invoice_money.as_dollar()}\n'
        result += f'You earned {self.invoice_credits} credits\n'
        return result

