class Performance:

    def __init__(self, play_id: str, audience: int) -> None:
        self.play_id = play_id
        self.audience = audience


class PerformancesRepository:

    def __init__(self, performances: list[Performance]) -> None:
        self.performances = performances
