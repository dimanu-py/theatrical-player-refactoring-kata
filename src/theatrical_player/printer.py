from src.theatrical_player.invoice import Invoice
from src.theatrical_player.statement import PlainTextStatement, Fillable


class StatementPrinter:

    def __init__(self) -> None:
        self.statement: Fillable = PlainTextStatement()

    def print(self, invoice: Invoice):
        invoice.fill(self.statement)
        return self.statement.print()
