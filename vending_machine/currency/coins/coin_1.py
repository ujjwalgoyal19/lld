from vending_machine.currency.currency import Currency
from vending_machine.currency.currency_type import CurrencyType


class Coin1(Currency):
    def __init__(self):
        super().__init__(1, CurrencyType.COIN)
