from src.theatrical_player.performance import PerformancesRepository


class Invoice:

    def __init__(self, customer: str, performances: PerformancesRepository) -> None:
        self.customer = customer
        self.performances = performances
