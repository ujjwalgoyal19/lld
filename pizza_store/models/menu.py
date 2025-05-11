import string
import uuid
from typing import Dict

from enums import ItemType
from models.items.base import Base
from models.items.drink import Drink
from models.items.order_item import OrderItem
from models.items.topping import Topping


class ItemFactory:
    def create_item(self, type: ItemType, name: str, price: float):
        if type == ItemType.BASE:
            return Base(name=name, price=price)
        elif type == ItemType.TOPPING:
            return Topping(name=name, price=price)
        elif type == ItemType.DRINK:
            return Drink(name=name, price=price)
        else:
            raise ValueError("No such item type can be created")


class MenuItem:
    def __init__(self, price: float, order_item: OrderItem):
        self.price = price
        self.order_item = order_item

    def update_price(self, new_price: float):
        self.price = new_price


class Menu:
    def __init__(self):
        self.__menu_items: Dict[str, MenuItem] = {}

    def add_menu_item(self, name: str, price: float, type: ItemType):
        item_id = string(uuid.uuid4())
        self.__menu_items[item_id] = MenuItem(
            price=price,
            order_item=ItemFactory().create_item(name=name, price=price, type=type),
        )

    def remove_menu_item(self, item_id: str):
        self.__menu_items.pop(item_id)

    def update_menu_item_price(self, item_id: str, new_price: float):
        self.__menu_items[item_id].update_price(new_price=new_price)

    def get_menu_item(self, item_id: str):
        return self.__menu_items[item_id]
