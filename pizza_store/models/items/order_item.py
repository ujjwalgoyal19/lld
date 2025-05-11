import string
import uuid
from abc import ABC, abstractmethod


class OrderItem(ABC):
    def __init__(self, name: str, price: float):
        self.__item_id = string(uuid.uuid4())
        self.__price = price
        self.__name = name

    def get_item_id(self):
        return self.__item_id

    @abstractmethod
    def get_price(self):
        return self.__price

    @abstractmethod
    def get_name(self):
        return self.__name
