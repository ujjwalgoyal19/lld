from enums import SplitType
from models.user import User


class Split:
    def __init__(
        self, split_type: SplitType, user: User, amount: float, percentage: float = 0
    ):
        self.__split_type = split_type
        self.__user = user
        self.__amount = amount
        self.__percentage = percentage

    @property
    def split_type(self):
        return self.__split_type

    @property
    def amount(self):
        return self.__amount

    @property
    def percentage(self):
        return self.__percentage

    def get_user(self):
        return self.__user
