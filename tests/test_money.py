import unittest

from src.theatrical_player.money import Money


class TestMoney(unittest.TestCase):

    def test_can_accumulate_money(self) -> None:
        initial_amount = Money(10)
        extra_amount = Money(20)

        total_amount = initial_amount.add(extra_amount)

        assert total_amount == Money(30)
