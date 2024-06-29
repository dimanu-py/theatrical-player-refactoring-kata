import math

from src.theatrical_player.credits import Credits
from src.theatrical_player.money import Money


def statement_printer(invoice, plays):
    total_amount = 0
    invoice_amount = Money(initial_amount=total_amount)
    invoice_credits = Credits(initial_credits=0)
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            performance_amount = Money(this_amount)
            if perf['audience'] > 30:
                extra_amount_by_audience = 1000 * (perf['audience'] - 30)
                this_amount += extra_amount_by_audience
                performance_amount = performance_amount.add(Money(extra_amount_by_audience))
        elif play['type'] == "comedy":
            this_amount = 30000
            performance_amount = Money(this_amount)
            if perf['audience'] > 20:
                extra_amount_by_audience = 10000 + 500 * (perf['audience'] - 20)
                this_amount += extra_amount_by_audience
                performance_amount = performance_amount.add(Money(extra_amount_by_audience))

            comedy_extra_amount = 300 * perf['audience']
            this_amount += comedy_extra_amount
            performance_amount = performance_amount.add(Money(comedy_extra_amount))

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        extra_credits_by_audience = Credits(max(perf['audience'] - 30, 0))
        invoice_credits = invoice_credits.add(extra_credits_by_audience)

        if "comedy" == play["type"]:
            comedy_extra_credits = Credits(math.floor(perf['audience'] / 5))
            invoice_credits = invoice_credits.add(comedy_extra_credits)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount
        invoice_amount = invoice_amount.add(performance_amount)

    result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
    result += f'You earned {invoice_credits} credits\n'
    return result

