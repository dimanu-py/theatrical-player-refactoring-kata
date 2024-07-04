from src.theatrical_player.invoice import Invoice
from src.theatrical_player.play import PlaysCatalog
from src.theatrical_player.statement import Statement


class StatementPrinter:

    def __init__(self) -> None:
        self.statement: Statement = Statement()

    def print(self, invoice: Invoice, catalog: PlaysCatalog):
        invoice.fill(self.statement, catalog)
        return self.statement.print()
