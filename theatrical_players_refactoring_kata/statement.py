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


def format_statement(entries, invoice, amount, volume_credits,
                     statement_type="printout"):
    if statement_type == "printout":
        return (f'Statement for {invoice["customer"]}\n'
                + format_printout_entries(entries)
                + f'Amount owed is {f"${amount :0,.2f}"}\n'
                + f'You earned {volume_credits} credits\n')
    else:
        return (f'<!DOCTYPE html>\n<html>\n<body>\n<h1>Statement for {
                invoice["customer"]}</h1>\n'
                + format_html_entries(entries)
                + f'<p>Amount owed is {f"${amount :0,.2f}"}</p>\n'
                + f'<p>You earned {volume_credits
                                   } credits</p>\n</body>\n</html>\n')


def format_printout_entries(entries):
    return "".join(
        [f' {entry.get("name")}: {f"${entry.get("amount") :0,.2f}"} ({
         entry.get("audience")} seats)\n' for entry in entries]
    )


def format_html_entries(entries):
    return "".join(
        [f'<p style="margin-left: 20px;">{entry.get("name")}: {f"${entry.get("amount") :0,.2f}"} ({
         entry.get("audience")} seats)</p>\n' for entry in entries]
    )



