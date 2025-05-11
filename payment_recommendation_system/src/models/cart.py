from typing import List

from src.models.cart_item import CartItem


class Cart:
    def __init__(self):
        self.cart_items: List[CartItem] = []
        self.total_amount: float = 0.0

    def add_item(self, new_cart_item: CartItem):
        self.cart_items.append(new_cart_item)
        total_amount += new_cart_item.get_item_price()

    def get_cart_items(self) -> List[CartItem]:
        return self.cart_items

    def get_total_amount(self) -> float:
        return self.total_amount
