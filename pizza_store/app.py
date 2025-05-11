from enums import ItemType
from models.pizza_store import PizzaStore


class App:
    def __init__(self):
        self.store = PizzaStore(name="Jaipur")

    def run(self):
        menu = self.store.get_menu()

        menu.add_menu_item(name="Thin Crust", price="80", type=ItemType.BASE)
        menu.add_menu_item(name="Cola", price="40", type=ItemType.DRINK)
        menu.add_menu_item(name="Mushroom", price="50", type=ItemType.TOPPING)
        menu.add_menu_item(name="Cheese", price="50", type=ItemType.TOPPING)

        thinCrustCheesePepperoniPizza = self.store.buildPizza()
