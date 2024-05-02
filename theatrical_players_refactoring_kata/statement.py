import math


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    header = f'Statement for {invoice["customer"]}\n'
    entries = ""
    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        volume_credits += calculate_performance_volume_credits(
            perf['audience'], play["type"])

        # print line for this order
        amount = this_amount/100
        entries += f' {play["name"]}: {f"${amount :0,.2f}"} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    amount1 = total_amount/100
    owed = f'Amount owed is {f"${amount1 :0,.2f}"}\n'
    earned = f'You earned {volume_credits} credits\n'
    return header + entries + owed + earned


def calculate_performance_volume_credits(perf_audience, play_type):
    # add volume credits
    audience_volume_credits = max(perf_audience - 30, 0)
    # add extra credit for every ten comedy attendees
    comedy_volume_credits = 0
    if "comedy" == play_type:
        comedy_volume_credits = math.floor(perf_audience / 5)
    performance_volume_credits = (
            audience_volume_credits + comedy_volume_credits)
    return performance_volume_credits


