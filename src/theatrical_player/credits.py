class Credits:

    def __init__(self, initial_credits: int) -> None:
        self.credits = initial_credits

    def add(self, other: "Credits") -> "Credits":
        return Credits(self.credits + other.credits)

    def __eq__(self, other: "Credits") -> bool:
        return self.credits == other.credits

    def __str__(self) -> str:
        return f"{self.credits}"
