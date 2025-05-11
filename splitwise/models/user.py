import string
import uuid

from models.balance_sheet import BalanceSheet


class User:
    def __init__(self, user_name: str):
        self.__user_id = string(uuid.uuid4())
        self.__user_name = user_name
        self.__balance_sheet = BalanceSheet()

    @property
    def user_name(self):
        return self.__user_name

    def get_user_id(self):
        return self.__user_id

    def get_balance_sheet(self):
        return self.__balance_sheet
