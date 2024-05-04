def format_statement(entries: [], customer: str, amount: int,
                     volume_credits: int, statement_type="printout"):
    """
    :param entries: List of entry dicts
    :param customer: Name of the customer
    :param amount: Total amount owed
    :param volume_credits: Volume credit for invoice
    :param statement_type: how to render the statement (html/printout)
    :return: statement rendered according to type
    """
    if statement_type == "printout":
        return (f'Statement for {customer}\n'
                + format_printout_entries(entries)
                + f'Amount owed is {f"${amount:0,.2f}"}\n'
                + f'You earned {volume_credits} credits\n')
    elif statement_type == "html":
        return (f'<!DOCTYPE html>\n<html>\n<body>\n<h1>Statement for {
                customer}</h1>\n'
                + format_html_entries(entries)
                + f'<p>Amount owed is {f"${amount:0,.2f}"}</p>\n'
                + f'<p>You earned {volume_credits
                                   } credits</p>\n</body>\n</html>\n')
    else:
        raise Exception("Unknown type of statement: " + statement_type)


def format_printout_entries(entries):
    return "".join(
        [f' {entry.get("name")}: {f"${entry.get("amount"):0,.2f}"} ({
         entry.get("audience")} seats)\n' for entry in entries]
    )


def format_html_entries(entries):
    return "".join(
        [f'<p style="margin-left: 20px;">{
         entry.get("name")}: {f"${
          entry.get("amount"):0,.2f}"} ({
          entry.get("audience")} seats)</p>\n' for entry in entries]
    )
