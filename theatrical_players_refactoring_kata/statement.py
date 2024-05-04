from theatrical_players_refactoring_kata.plays import PlayCalculator


def statement(invoice, plays):
    entries = calculate_statement_entries(invoice, plays)
    total_amount = sum([entry.get("amount") for entry in entries])
    volume_credits = sum([entry.get("credits") for entry in entries])
    return format_statement(entries, invoice, total_amount, volume_credits)


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


def format_statement(entries, invoice, amount, volume_credits):
    return (f'Statement for {invoice["customer"]}\n'
            + format_entries(entries)
            + f'Amount owed is {f"${amount :0,.2f}"}\n'
            + f'You earned {volume_credits} credits\n')


def format_entries(entries):
    return "".join(
        [f' {entry.get("name")}: {f"${entry.get("amount") :0,.2f}"} ({
         entry.get("audience")} seats)\n' for entry in entries]
    )




