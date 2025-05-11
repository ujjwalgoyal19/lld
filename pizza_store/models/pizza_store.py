from typing import Dict, List

from models.deals.deal import Deal
from models.menu import Menu


class PizzaStore:
    def __init__(self, name: str):
        self.__name = name
        self.__menu = Menu()

    def get_name(self):
        return self.__name

    def get_menu(self):
        return self.__menu

    def build_pizza(self):
        return Pizz
