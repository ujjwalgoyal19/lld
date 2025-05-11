from typing import List

from models.items.base import Base
from models.items.order_item import OrderItem
from models.items.topping import Topping


class Pizza(OrderItem):
    def __init__(self, name: str, base: Base, toppings: List[Topping], price: float):
        self.__pizza_base = base
        self.__toppings: List[Topping] = toppings
        super().__init__(name=name, price=price)
