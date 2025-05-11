from abc import ABC
from typing import List

from vending_machine.currency.currency_type import CurrencyType


class Currency(ABC):
    _value: int
    _type: CurrencyType

    def __init__(self, currency_value: int, currency_type: CurrencyType) -> None:
        self._value = currency_value
        self._type = currency_type

    def get_currency(self) -> List[int, CurrencyType]:
        return self._value, self._type
