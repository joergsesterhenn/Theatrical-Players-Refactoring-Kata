import math

from theatrical_players_refactoring_kata.plays import Play


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    entries = ""
    for perf in invoice['performances']:
        play_entry = plays[perf['playID']]
        play = Play.of(play_entry['type'], play_entry['name'])
        amount = play.calculate_amount(perf['audience'])
        volume_credits += play.calculate_credits(perf['audience'])
        entries += format_entry(amount, perf['audience'], play_entry["name"])
        total_amount += amount

    return format_header(invoice) + entries + format_owed(
        total_amount / 100) + format_credits(volume_credits)


def format_credits(volume_credits):
    return f'You earned {volume_credits} credits\n'


def format_owed(owed_amount):
    return f'Amount owed is {f"${owed_amount :0,.2f}"}\n'


def format_header(invoice):
    return f'Statement for {invoice["customer"]}\n'


def format_entry(amount, audience, play_name):
    return f' {play_name}: {f"${amount / 100 :0,.2f}"} ({audience} seats)\n'

