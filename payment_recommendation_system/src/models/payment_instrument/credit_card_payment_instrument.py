from src.models.payment_instrument.payment_instrument import PaymentInstrument


class CreditCardPaymentInstrument(PaymentInstrument):
    def __init__(self, type: str, issuer: str, relevance_score: int):
        self.type = type
        self.issuer = issuer
        self.relevance_score = relevance_score

    def make_payment(self, amount: float):
        print(
            "Payment of"
            + amount
            + " made using "
            + self.issuer
            + " "
            + self.type
            + " credit card with relevance score: "
            + self.relevance_score
        )
