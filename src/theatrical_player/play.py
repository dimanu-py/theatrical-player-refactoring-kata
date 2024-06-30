class Play:

    def __init__(self, name: str, genre: str) -> None:
        self.name = name
        self.genre = genre


class PlaysCatalog:

    def __init__(self, catalog: dict[str, Play]) -> None:
        self.catalog = catalog
