from abc import ABC, abstractmethod
from ast import List

from src.models.payment_instrument.payment_instrument import PaymentInstrument
from src.models.cart import Cart
from src.models.user import User


class PaymentRecommendationStrategy(ABC):
    @abstractmethod
    def recommend_payment_instruments(
        cart: Cart, user: User
    ) -> List[PaymentInstrument]: ...
