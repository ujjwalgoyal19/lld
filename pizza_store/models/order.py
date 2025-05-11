import string
import uuid
from typing import List

from models.items.order_item import OrderItem
from models.pizza_store import PizzaStore


class Order:
    def __init__(self, store: PizzaStore):
        self.__order_id = string(uuid.uuid4())
        self.__store = store
        self.items: List[OrderItem] = []

    def add_item(self, order_item: OrderItem):
        self.items.append(order_item)

    def remove_item(self, order_item: str):
        self.items.remove(order_item)

    def calculate_total(self):
        sub_total = 0
        for item in self.items:
            sub_total += item.get_price()

        discounts = 0
        for deal in self.__store.getDeals():
            discounts += deal.calculate_discounts(self)

        return sub_total - discounts
