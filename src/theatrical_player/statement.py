from src.theatrical_player.credits import Credits
from src.theatrical_player.invoice import Invoice
from src.theatrical_player.money import Money
from src.theatrical_player.performance import Performance
from src.theatrical_player.play import Play


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
