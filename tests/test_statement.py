import unittest

from approvaltests import verify

from src.theatrical_player.performance import Performance
from src.theatrical_player.play import Play
from src.theatrical_player.statement import StatementPrinter
from tests.conftest import IntelliJDiffReporter


class TestStatement(unittest.TestCase):

    def setUp(self):
        self.statement_printer = StatementPrinter()
        self.intellij_diff_reporter = IntelliJDiffReporter()

    def test_can_produce_invoice_with_valid_plays(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                Performance("hamlet", 55),
                Performance("as-like", 35),
                Performance("othello", 40)
            ]
        }
        plays = {
            "hamlet": Play("Hamlet", "tragedy"),
            "as-like": Play("As You Like It", "comedy"),
            "othello": Play("Othello", "tragedy")
        }

        verify(
            self.statement_printer.print(invoice, plays),
            reporter=self.intellij_diff_reporter
        )

    def test_cannot_produce_invoice_of_unknown_plays_type(self):
        invoice = {
            "customer": "BigCoII",
            "performances": [
                Performance("henry-v", 53),
                Performance("as-like", 55)
            ]
        }
        plays = {
            "henry-v": Play("Henry V", "history"),
            "as-like": Play("As You Like It", "pastoral")
        }

        with self.assertRaises(ValueError) as exception_info:
            self.statement_printer.print(invoice, plays)
        self.assertIn("unknown type", str(exception_info.exception))
