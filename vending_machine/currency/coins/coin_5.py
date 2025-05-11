from vending_machine.currency.currency import Currency
from vending_machine.currency.currency_type import CurrencyType


class Coin5(Currency):
    def __init__(self):
        super().__init__(5, CurrencyType.COIN)
