from typing import List

from models.balance import Balance


class BalanceSheet:
    def __init__(self):
        self.__total_expense_done = 0
        self.__total_payment_done = 0
        self.__total_money_owed = 0
        self.__total_money_get_back = 0
        self.__users: List[Balance] = []
