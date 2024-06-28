import unittest

from src.theatrical_player.credits import Credits


class TestCredits(unittest.TestCase):

    def test_can_accumulate_credits(self):
        initial_credits = Credits(initial_credits=5)
        extra_credits = Credits(initial_credits=10)

        total_credits = initial_credits.add(extra_credits)

        assert total_credits == Credits(initial_credits=15)
