from typing import Set

from src.constants.line_of_business import LineOfBusiness


class CartItem:
    def __init__(
        self,
        item_name: str,
        item_price: int,
        line_of_business: LineOfBusiness,
        supported_payment_methods: Set[str],
    ):
        self.item_name = item_name
        self.item_price = item_price
        self.line_of_business = line_of_business
        self.supported_payment_methods = supported_payment_methods

    def get_item_price(self):
        return self.item_price
