from src.theatrical_player.performance import Performance


class Invoice:

    def __init__(self, customer: str, performances: list[Performance]) -> None:
        self.customer = customer
        self.performances = performances
