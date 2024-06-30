import math

from src.theatrical_player.credits import Credits
from src.theatrical_player.invoice import Invoice
from src.theatrical_player.money import Money
from src.theatrical_player.performance import Performance
from src.theatrical_player.play import Play, PlaysCatalog


class StatementPrinter:

    def __init__(self) -> None:
        self.invoice_money = Money(initial_amount=0)
        self.invoice_credits = Credits(initial_credits=0)

    def print(self, invoice: Invoice, plays: dict[str, Play], catalog: PlaysCatalog = None):
        result = f'Statement for {invoice.customer}\n'

        for performance in invoice.performances:
            play = plays.get(performance.play_id)

            performance_amount = self.compute_performance_amount(performance, play)
            performance_credits = self.compute_performance_credits(performance, play)

            self.invoice_credits = self.invoice_credits.add(performance_credits)
            self.invoice_money = self.invoice_money.add(performance_amount)

            # print line for this order
            result += f' {play.name}: {performance_amount.as_dollar()} ({performance.audience} seats)\n'

        result += f'Amount owed is {self.invoice_money.as_dollar()}\n'
        result += f'You earned {self.invoice_credits} credits\n'
        return result

    def compute_performance_credits(self, performance: Performance, play: Play) -> Credits:
        performance_credits = Credits(max(performance.audience - 30, 0))
        performance_credits = performance_credits.add(self.extra_credits_by_genre(performance, play))
        return performance_credits

    @staticmethod
    def extra_credits_by_genre(performance: Performance, play: Play) -> Credits:
        if "comedy" == play.genre:
            return Credits(math.floor(performance.audience / 5))
        return Credits(0)

    def compute_performance_amount(self, performance: Performance, play: Play) -> Money:
        if play.genre == "tragedy":
            performance_amount = Money(40000)
            performance_amount = performance_amount.add(self.tragedy_extra_amount_by_audience(performance))
            return performance_amount

        if play.genre == "comedy":
            performance_amount = Money(30000)
            performance_amount = performance_amount.add(self.comedy_extra_amount_by_audience(performance))
            performance_amount = performance_amount.add(self.comedy_extra_amount_by_genre(performance))
            return performance_amount

        raise ValueError(f'unknown type: {play.genre}')

    @staticmethod
    def comedy_extra_amount_by_genre(performance: Performance) -> Money:
        return Money(300 * performance.audience)

    @staticmethod
    def comedy_extra_amount_by_audience(performance: Performance) -> Money:
        if performance.audience > 20:
            return Money(10000 + 500 * (performance.audience - 20))
        return Money(0)

    @staticmethod
    def tragedy_extra_amount_by_audience(performance: Performance) -> Money:
        if performance.audience > 30:
            return Money(1000 * (performance.audience - 30))
        return Money(0)
