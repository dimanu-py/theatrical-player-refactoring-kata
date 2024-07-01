from typing import Iterable

from src.theatrical_player.credits import Credits
from src.theatrical_player.money import Money
from src.theatrical_player.play import Play


class Performance:

    def __init__(self, play_id: str, audience: int) -> None:
        self.play_id = play_id
        self.audience = audience

    def credits(self, play: Play) -> Credits:
        initial_credits = Credits(max(self.audience - 30, 0))
        return initial_credits.add(play.credits(self.audience))

    def cost(self, play: Play) -> Money:
        return play.cost(self.audience)


class PerformancesRepository:

    def __init__(self, performances: list[Performance]) -> None:
        self.performances = performances

    def __iter__(self) -> Iterable[Performance]:
        return iter(self.performances)
