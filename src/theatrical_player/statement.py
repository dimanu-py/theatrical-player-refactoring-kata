import math

from src.theatrical_player.credits import Credits
from src.theatrical_player.money import Money


class StatementPrinter:

    def __init__(self) -> None:
        self.money = Money(initial_amount=0)
        self.credits = Credits(initial_credits=0)

    def print(self, invoice, plays):
        result = f'Statement for {invoice["customer"]}\n'

        for perf in invoice['performances']:
            play = plays[perf['playID']]
            if play['type'] == "tragedy":
                performance_amount = Money(40000)
                if perf['audience'] > 30:
                    extra_amount_by_audience = Money(1000 * (perf['audience'] - 30))
                    performance_amount = performance_amount.add(extra_amount_by_audience)
            elif play['type'] == "comedy":
                performance_amount = Money(30000)
                if perf['audience'] > 20:
                    extra_amount_by_audience = Money(10000 + 500 * (perf['audience'] - 20))
                    performance_amount = performance_amount.add(extra_amount_by_audience)

                comedy_extra_amount = Money(300 * perf['audience'])
                performance_amount = performance_amount.add(comedy_extra_amount)

            else:
                raise ValueError(f'unknown type: {play["type"]}')

            extra_credits_by_audience = Credits(max(perf['audience'] - 30, 0))
            self.credits = self.credits.add(extra_credits_by_audience)

            if "comedy" == play["type"]:
                comedy_extra_credits = Credits(math.floor(perf['audience'] / 5))
                self.credits = self.credits.add(comedy_extra_credits)
            # print line for this order
            result += f' {play["name"]}: {performance_amount.as_dollar()} ({perf["audience"]} seats)\n'
            self.money = self.money.add(performance_amount)

        result += f'Amount owed is {self.money.as_dollar()}\n'
        result += f'You earned {self.credits} credits\n'
        return result
