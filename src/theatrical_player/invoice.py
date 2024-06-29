from src.theatrical_player.performance import Performance, PerformancesRepository


class Invoice:

    def __init__(self, customer: str, performances: list[Performance], performances_repository: PerformancesRepository = None) -> None:
        self.customer = customer
        self.performances = performances
        self.performances_repository = performances_repository
