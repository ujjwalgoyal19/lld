from vending_machine.currency.currency import Currency
from vending_machine.currency.currency_type import CurrencyType


class Note200(Currency):
    def __init__(self):
        super().__init__(200, CurrencyType.NOTE)
