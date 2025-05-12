from typing import Dict

from models.balance import Balance


class BalanceSheet:
    def __init__(self):
        self.__total_expense_done = 0
        self.__total_payment_done = 0
        self.__total_money_owed = 0
        self.__total_money_get_back = 0
        self.__users: Dict[str, Balance] = []

    def set_total_expense_done(self, total_expense_done):
        self.__total_expense_done = total_expense_done

    def set_total_payment_done(self, total_payment_done):
        self.__total_payment_done = total_payment_done

    def set_total_money_owed(self, total_money_owed):
        self.__total_money_owed = total_money_owed

    def set_total_money_get_back(self, total_money_get_back):
        self.__total_money_get_back = total_money_get_back

    def set_users(self, users: Dict[str, Balance]):
        self.__users = users

    def get_total_expense_done(self):
        return self.__total_expense_done

    def get_total_payment_done(self):
        return self.__total_payment_done

    def get_total_money_owed(self):
        return self.__total_money_owed

    def get_total_money_get_back(self):
        return self.__total_money_get_back

    def get_users(self):
        return self.__users
