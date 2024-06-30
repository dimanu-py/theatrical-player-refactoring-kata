import unittest

from approvaltests import verify

from src.theatrical_player.invoice import Invoice
from src.theatrical_player.performance import Performance, PerformancesRepository
from src.theatrical_player.play import Play, PlaysCatalog
from src.theatrical_player.statement import StatementPrinter
from tests.conftest import IntelliJDiffReporter


class TestStatement(unittest.TestCase):
    CUSTOMER = "BigCo"

    def setUp(self):
        self.statement_printer = StatementPrinter()
        self.intellij_diff_reporter = IntelliJDiffReporter()

    def test_can_produce_invoice_with_valid_plays(self):
        performances = PerformancesRepository([
            Performance("hamlet", 55),
            Performance("as-like", 35),
            Performance("othello", 40)
        ])
        catalog = PlaysCatalog({
            "hamlet": Play("Hamlet", "tragedy"),
            "as-like": Play("As You Like It", "comedy"),
            "othello": Play("Othello", "tragedy")
        })
        invoice = Invoice(customer=self.CUSTOMER, performances=performances)

        verify(
            self.statement_printer.print(invoice, catalog),
            reporter=self.intellij_diff_reporter
        )

    def test_cannot_produce_invoice_of_unknown_plays_type(self):
        performances = PerformancesRepository([
            Performance("henry-v", 53),
            Performance("as-like", 55)
        ])
        catalog = PlaysCatalog({
            "henry-v": Play("Henry V", "history"),
            "as-like": Play("As You Like It", "pastoral")
        })
        invoice = Invoice(customer=self.CUSTOMER, performances=performances)

        with self.assertRaises(ValueError) as exception_info:
            self.statement_printer.print(invoice, catalog)
        self.assertIn("unknown type", str(exception_info.exception))
