from abc import ABC


class Deal(ABC):
    def calculate_discount(self, order: any): ...
