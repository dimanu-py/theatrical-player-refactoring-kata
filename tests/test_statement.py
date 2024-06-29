import json
import unittest

from approvaltests import verify

from src.theatrical_player.statement import StatementPrinter
from tests.conftest import IntelliJDiffReporter


def open_json_at(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return json.loads(file.read())


class TestStatement(unittest.TestCase):

    def setUp(self):
        self.statement_printer = StatementPrinter()
        self.intellij_diff_reporter = IntelliJDiffReporter()

    def test_can_produce_invoice_with_valid_plays(self):
        invoice = open_json_at("tests/test_files/invoice.json")
        plays = open_json_at("tests/test_files/plays.json")

        verify(
            self.statement_printer.print(invoice, plays),
            reporter=self.intellij_diff_reporter
        )

    def test_cannot_produce_invoice_of_unknown_plays_type(self):
        invoice = open_json_at("tests/test_files/invoice_new_plays.json")
        plays = open_json_at("tests/test_files/new_plays.json")

        with self.assertRaises(ValueError) as exception_info:
            self.statement_printer.print(invoice, plays)
        self.assertIn("unknown type", str(exception_info.exception))
