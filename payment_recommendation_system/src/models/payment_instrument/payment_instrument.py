from abc import ABC, abstractmethod


class PaymentInstrument(ABC):
    @abstractmethod
    def make_payment(self, amount: float) -> bool: ...
