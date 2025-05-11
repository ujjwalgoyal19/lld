from models.items.order_item import OrderItem


class Drink(OrderItem):
    def __init__(self, name: str, price: float):
        super().__init__(name=name, price=price)
