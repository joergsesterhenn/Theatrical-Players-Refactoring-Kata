import pytest
from approval_utilities.utils import get_adjacent_file
from approvaltests import verify

from theatrical_players.models.Play import Plays
from theatrical_players.models.Invoice import Invoice
from theatrical_players.statement import statement


def test_example_statement():
    with open(get_adjacent_file("invoice.json")) as f:
        invoice = Invoice.model_validate_json(f.read())
    with open(get_adjacent_file("plays.json")) as f:
        plays = Plays.model_validate_json(f.read())
    result = statement(invoice, plays)
    verify(result)


def test_statement_with_new_play_types():
    with open(get_adjacent_file("invoice_new_plays.json")) as f:
        invoice = Invoice.model_validate_json(f.read())
    with open(get_adjacent_file("new_plays.json")) as f:
        plays = Plays.model_validate_json(f.read())
    result = statement(invoice, plays)
    verify(result)


def test_statement_with_new_play_types_and_html():
    with open(get_adjacent_file("invoice_new_plays.json")) as f:
        invoice = Invoice.model_validate_json(f.read())
    with open(get_adjacent_file("new_plays.json")) as f:
        plays = Plays.model_validate_json(f.read())
    result = statement(invoice, plays, "html")
    verify(result)


def test_statement_with_unknown_type():
    with open(get_adjacent_file("invoice_unknown_type_plays.json")) as f:
        invoice = Invoice.model_validate_json(f.read())
    with open(get_adjacent_file("unknown_type_plays.json")) as f:
        plays = Plays.model_validate_json(f.read())
    with pytest.raises(ValueError) as exception_info:
        statement(invoice, plays)
    assert "unknown type" in str(exception_info.value)
