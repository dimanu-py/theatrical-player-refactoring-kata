from src.theatrical_player.invoice import Invoice
from src.theatrical_player.statement import Statement


class StatementPrinter:

    def __init__(self) -> None:
        self.statement: Statement = Statement()

    def print(self, invoice: Invoice):
        invoice.fill(self.statement)
        return self.statement.print()
