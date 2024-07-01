import math

from src.theatrical_player.credits import Credits


class Play:

    def __init__(self, name: str, genre: str) -> None:
        self.name = name
        self.genre = genre

    def extra_credits_by_genre(self, audience: int) -> Credits:
        return Credits(math.floor(audience / 5)) if self.genre == "comedy" else Credits(0)


class PlaysCatalog:

    def __init__(self, catalog: dict[str, Play]) -> None:
        self.catalog = catalog

    def by_id(self, play_id: str) -> Play:
        return self.catalog.get(play_id)
