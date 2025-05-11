from abc import ABC, abstractmethod
from typing import List, Set

from src.models.cart_item import CartItem


class PaymentComputationStrategy(ABC):
    @abstractmethod
    def compute_payment_methods(self, cart_items: List[CartItem]) -> Set[str]: ...
