from typing import List

from models.items.topping import Topping
from models.menu import Menu, MenuItem


class PizzaBuilder:
    def __init__(self, menu: Menu):
        self.__menu = menu
        self.__base: MenuItem = None
        self.__toppings: List[MenuItem] = []

    # There can only be one base for a pizza
    def select_base(self, item_id: str):
        menu_item = self.__menu.get_menu_item(item_id=item_id)
        # if menu_item.
        self.__base = self.__menu.get_menu_item(item_id=item_id)
