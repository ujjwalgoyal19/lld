from models.user import User


class Split:
    def __init__(self, amount: float, user: User, percentage: float):
        self.__amount = amount
        self.__user = user
        self.__percentage = percentage

    @property
    def amount(self):
        return self.__amount

    @property
    def percentage(self):
        return self.__percentage

    def get_user(self):
        return self.__user
