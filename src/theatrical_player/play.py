class Play:

    def __init__(self, name: str, genre: str) -> None:
        self.name = name
        self.genre = genre


class PlaysCatalog:

    def __init__(self, catalog: dict[str, Play]) -> None:
        self.catalog = catalog

    def by_id(self, play_id: str) -> Play:
        return self.catalog.get(play_id)
