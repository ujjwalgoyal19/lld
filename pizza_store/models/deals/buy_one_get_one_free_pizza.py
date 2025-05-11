from models.deals.deal import Deal


class BuyOneGetOneFree(Deal):
    def calculate_discount(self, order):
        return super().calculate_discount(order)
