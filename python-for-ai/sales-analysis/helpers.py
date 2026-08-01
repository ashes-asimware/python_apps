
def calculate_total(quantity, price):
    """ Calculate total for a single item """
    return quantity * price

def format_currency(value):
    """ Format a number as currency """
    return "${:,.2f}".format(value)

