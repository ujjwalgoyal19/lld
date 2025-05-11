from abc import ABC, abstractmethod


class Note(ABC):
    _value: int

    @abstractmethod
    def __init__(self, value):
        self._value = value

    def get_value(self) -> int:
        return self._value
