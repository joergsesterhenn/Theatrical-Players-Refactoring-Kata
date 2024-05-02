import math


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    entries = ""
    for perf in invoice['performances']:
        play = plays[perf['playID']]
        amount = calculate_amount(perf['audience'], play['type'])
        volume_credits += calculate_volume_credits(perf['audience'],
                                                   play['type'])
        entries += format_entry(amount, perf['audience'], play["name"])
        total_amount += amount

    owed_amount = total_amount/100

    return format_header(invoice) + entries + format_owed(
        owed_amount) + format_credits(volume_credits)


def format_credits(volume_credits):
    earned = f'You earned {volume_credits} credits\n'
    return earned


def format_owed(owed_amount):
    owed = f'Amount owed is {f"${owed_amount :0,.2f}"}\n'
    return owed


def format_header(invoice):
    header = f'Statement for {invoice["customer"]}\n'
    return header


def format_entry(amount, audience, play_name):
    entry = f' {play_name}: {f"${amount / 100 :0,.2f}"} ({audience} seats)\n'
    return entry


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


