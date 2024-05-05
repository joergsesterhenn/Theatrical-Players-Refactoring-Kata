from abc import ABCMeta, abstractmethod
from typing import Self


class StatementFormatter(metaclass=ABCMeta):

    @abstractmethod
    def format_statement(self, amount: int, customer: str, entries: [],
                         volume_credits: int) -> str:
        """
        :param entries: List of entry dicts
        :param customer: Name of the customer
        :param amount: Total amount owed
        :param volume_credits: Volume credit for invoice
        :return: statement rendered according to type
        """
        pass

    @classmethod
    def of(cls, statement_type: str) -> Self:
        if statement_type == "plain_text":
            return PlainTextStatementFormatter()
        elif statement_type == "html":
            return HTMLStatementFormatter()
        else:
            raise Exception("Unknown type of statement: " + statement_type)


class HTMLStatementFormatter(StatementFormatter):
    def format_statement(self, amount, customer, entries,
                         volume_credits) -> str:
        return (f'<!DOCTYPE html>\n<html>\n<body>\n<h1>Statement for {
                customer}</h1>\n' + self.format_entries(entries)
                + f'<p>Amount owed is {f"${amount:0,.2f}"}</p>\n'
                + f'<p>You earned {volume_credits
                                   } credits</p>\n</body>\n</html>\n')

    @staticmethod
    def format_entries(entries):
        return "".join(
            [f'<p style="margin-left: 20px;">{
             entry.get("name")}: {f"${
              entry.get("amount"):0,.2f}"} ({
              entry.get("audience")} seats)</p>\n' for entry in entries]
        )


class PlainTextStatementFormatter(StatementFormatter):
    def format_statement(self, amount, customer, entries,
                         volume_credits) -> str:
        return (f'Statement for {customer}\n'
                + self.format_entries(entries)
                + f'Amount owed is {f"${amount:0,.2f}"}\n'
                + f'You earned {volume_credits} credits\n')

    @staticmethod
    def format_entries(entries):
        return "".join(
            [f' {entry.get("name")}: {f"${entry.get("amount"):0,.2f}"} ({
             entry.get("audience")} seats)\n' for entry in entries]
        )
