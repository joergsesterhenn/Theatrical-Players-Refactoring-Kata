import math


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    header = f'Statement for {invoice["customer"]}\n'
    entries = ""
    for perf in invoice['performances']:
        play = plays[perf['playID']]
        play_type = play['type']
        audience = perf['audience']

        this_amount = calculate_amount(audience, play_type)
        volume_credits += calculate_volume_credits(audience, play_type)

        # print line for this order
        entries += f' {play["name"]}: {f"${this_amount / 100 :0,.2f}"} ({audience} seats)\n'
        total_amount += this_amount

    owed_amount = total_amount/100
    owed = f'Amount owed is {f"${owed_amount :0,.2f}"}\n'
    earned = f'You earned {volume_credits} credits\n'
    return header + entries + owed + earned


def calculate_amount(audience, play_type):
    if play_type == "tragedy":
        this_amount = 40000
        if audience > 30:
            this_amount += 1000 * (audience - 30)
    elif play_type == "comedy":
        this_amount = 30000
        if audience > 20:
            this_amount += 10000 + 500 * (audience - 20)

        this_amount += 300 * audience

    else:
        raise ValueError(f'unknown type: {play_type}')
    return this_amount


def calculate_volume_credits(perf_audience, play_type):
    # add volume credits
    audience_volume_credits = max(perf_audience - 30, 0)
    # add extra credit for every ten comedy attendees
    comedy_volume_credits = 0
    if "comedy" == play_type:
        comedy_volume_credits = math.floor(perf_audience / 5)
    performance_volume_credits = (
            audience_volume_credits + comedy_volume_credits)
    return performance_volume_credits


