from abc import ABC, abstractclassmethod, abstractmethod


class PaymentInstrumentFactory(ABC):
    @abstractmethod
    def create_payment_instrument(
        self, type: str, issuer: str, relevance_score: float
    ): ...
