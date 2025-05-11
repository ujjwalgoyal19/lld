from abc import ABC
from dataclasses import dataclass


@dataclass
class Product(ABC):
    _cost: int
    _product_name: str
    _brand_name: str
    _code: str
