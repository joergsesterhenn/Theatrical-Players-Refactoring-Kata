from theatrical_players.models.Invoice import Invoice
from theatrical_players.models.Performance import Performance
from theatrical_players.models.Play import Plays
from theatrical_players.statement_formatter import StatementFormatter
from theatrical_players.plays_calculator import PlayCalculator


def statement(invoice: Invoice, plays: Plays, statement_type="plain_text"):
    """
    Formats a statement for an invoice depending on  statement_type.
    :param invoice: invoice data
    :param plays: list of plays
    :param statement_type: format in which to render
           the statement (html, plain_text)
    :return: formated statement
    """
    entries = calculate_statement_entries(invoice.performances, plays)
    total_amount = sum([entry.get("amount") for entry in entries])
    volume_credits = sum([entry.get("credits") for entry in entries])
    return StatementFormatter.of(statement_type).format_statement(
                            total_amount,
                            invoice.customer,
                            entries,
                            volume_credits)


def calculate_statement_entries(performances: list[Performance], plays: Plays):
    """
    Calculates a list of entry dicts with all required information per play.
    :param performances: list of performances
    :param plays: list of plays
    :return: list of entry dicts with all required information per play
    """
    entries = []
    for performance in performances:
        play = plays.__getitem__(performance.playID)
        play_calculator = PlayCalculator.of(play.type)
        amount = play_calculator.calculate_amount(performance.audience)/100
        volume_credits = (
            play_calculator.calculate_credits(performance.audience))

        entries.append({'amount': amount, 'audience': performance.audience,
                        'name': play.name, 'credits': volume_credits})
    return entries
