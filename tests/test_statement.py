import json

import pytest
from approval_utilities.utils import get_adjacent_file
from approvaltests import verify
from theatrical_players_refactoring_kata.statement import statement


def test_example_statement():
    with open(get_adjacent_file("invoice.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("plays.json")) as f:
        plays = json.loads(f.read())
    result = statement(invoice, plays)
    verify(result)


def test_statement_with_new_play_types():
    with open(get_adjacent_file("invoice_new_plays.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("new_plays.json")) as f:
        plays = json.loads(f.read())
    result = statement(invoice, plays)
    verify(result)


def test_statement_with_new_play_types_and_html():
    with open(get_adjacent_file("invoice_new_plays.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("new_plays.json")) as f:
        plays = json.loads(f.read())
    result = statement(invoice, plays, "html")
    verify(result)
