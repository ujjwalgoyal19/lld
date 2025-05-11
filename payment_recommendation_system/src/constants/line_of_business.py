from enum import Enum


class LineOfBusiness(Enum):
    CREDIT_CARD_BILL_PAYMENT, COMMERCE_PURCHASE, INVESTMENT_PURCHASE = range(3)
