from theatrical_players_refactoring_kata.formatter import format_statement
from theatrical_players_refactoring_kata.plays_calculator import PlayCalculator


def statement(invoice, plays, statement_type="printout"):
    entries = calculate_statement_entries(invoice, plays)
    total_amount = sum([entry.get("amount") for entry in entries])
    volume_credits = sum([entry.get("credits") for entry in entries])
    return format_statement(entries,
                            invoice,
                            total_amount,
                            volume_credits,
                            statement_type)


def calculate_statement_entries(invoice, plays):
    entries = []
    for perf in invoice['performances']:
        play_entry = plays[perf['playID']]
        play_calculator = PlayCalculator.of(play_entry['type'],
                                            play_entry['name'])
        amount = play_calculator.calculate_amount(perf['audience'])/100
        volume_credits = play_calculator.calculate_credits(perf['audience'])

        entries.append({'amount': amount, 'audience': perf['audience'],
                        'name': play_entry["name"], 'credits': volume_credits})
    return entries
