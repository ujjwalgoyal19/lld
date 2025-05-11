from models.items.order_item import OrderItem


class Base(OrderItem):
    def __init__(self, name: str, price: str):
        super().__init__(name=name, price=price)
