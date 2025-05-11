from dataclasses import dataclass
from multiprocessing import current_process
from typing import Dict

from vending_machine.inventory.product import Product


@dataclass
class InventoryUnit:
    product: Product
    total_units: int

    def get_product(self):
        return self.product

    def update_units(self, updated_units: int):
        self.total_units = updated_units

    def get_units(self):
        return self.total_units


class InventoryManager:
    _max_product_allowed: int
    _products: Dict[str, InventoryUnit]

    def add_product_in_inventory(self, product_to_add: Product, total_units: int):
        self._products[product_to_add._code] = InventoryUnit(
            product=product_to_add, total_units=total_units
        )

    def discard_product_from_inventory(self, product_to_discard: Product):
        self._products.pop(product_to_discard._code)

    def purchase_product_units(self, product_code: str, units_purchased: int):
        current_product = self._products[product_code]
        current_product.update_units(current_product.get_units() + units_purchased)

    def sell_product_units(self, product_code: str, units_sold: int):
        current_product = self._products[product_code]
        current_product_units = current_product.get_units()
        if units_sold > current_product_units:
            raise ValueError(
                f"Current product only have {current_product_units} units, therefore order for {units_sold} units can't be placed"
            )
        current_product.update_units(current_product.get_units() - units_sold)
