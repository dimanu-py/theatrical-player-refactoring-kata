import unittest

from approvaltests import verify

from src.theatrical_player.invoice import Invoice
from src.theatrical_player.performance import Performance, PerformancesRepository
from src.theatrical_player.play import Play, PlaysCatalog, Tragedy, Comedy
from src.theatrical_player.printer import StatementPrinter
from tests.conftest import IntelliJDiffReporter


class TestStatementPrinter(unittest.TestCase):
    CUSTOMER = "BigCo"

    def setUp(self):
        self.statement_printer = StatementPrinter()
        self.intellij_diff_reporter = IntelliJDiffReporter()

    def test_can_produce_invoice_with_valid_plays(self):
        performances = PerformancesRepository([
            Performance(Tragedy("Hamlet"), 55),
            Performance(Comedy("As You Like It"), 35),
            Performance(Tragedy("Othello"), 40)
        ])
        invoice = Invoice(customer=self.CUSTOMER, performances=performances)

        verify(
            self.statement_printer.print(invoice),
            reporter=self.intellij_diff_reporter
        )

    def test_cannot_produce_invoice_of_unknown_plays_type(self):
        with self.assertRaises(ValueError) as exception_info:
            PlaysCatalog({
                "henry-v": Play.create("Henry V", "history"),
                "as-like": Play.create("As You Like It", "pastoral")
            })
        self.assertIn("unknown type", str(exception_info.exception))
