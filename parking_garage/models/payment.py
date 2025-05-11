from models.ticket import Ticket


class Payment:
    def __init__(self, amount: float, ticket: Ticket, payment_mode):
        self.ticket = ticket
        self.amount = amount
        self.payment_mode = payment_mode
