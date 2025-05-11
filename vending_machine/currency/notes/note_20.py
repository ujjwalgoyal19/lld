from vending_machine.currency.currency import Currency
from vending_machine.currency.currency_type import CurrencyType


class Note20(Currency):
    def __init__(self):
        super().__init__(20, CurrencyType.NOTE)
