from theatrical_players_refactoring_kata.formatter import format_statement
from theatrical_players_refactoring_kata.plays_calculator import PlayCalculator


def statement(invoice, plays, statement_type="printout"):
    """
    Formats a statement for an invoice depending on  statement_type.
    :param invoice: invoice data
    :param plays: list of plays
    :param statement_type: format in which to render
           the statement (html, printout)
    :return: formated statement
    """
    entries = calculate_statement_entries(invoice['performances'], plays)
    total_amount = sum([entry.get("amount") for entry in entries])
    volume_credits = sum([entry.get("credits") for entry in entries])
    return format_statement(entries,
                            invoice["customer"],
                            total_amount,
                            volume_credits,
                            statement_type)


def calculate_statement_entries(performances, plays):
    """
    Calculates a list of entry dicts with all required information per play.
    :param performances: list of performances
    :param plays: list of plays
    :return: list of entry dicts with all required information per play
    """
    entries = []
    for performance in performances:
        play = plays[performance['playID']]
        play_calculator = PlayCalculator.of(play['type'],
                                            play['name'])
        amount = play_calculator.calculate_amount(performance['audience'])/100
        volume_credits = (
            play_calculator.calculate_credits(performance['audience']))

        entries.append({'amount': amount, 'audience': performance['audience'],
                        'name': play["name"], 'credits': volume_credits})
    return entries
