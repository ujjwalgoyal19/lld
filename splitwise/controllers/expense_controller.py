from typing import List

from models.expense import Expense
from models.group import Group
from models.split import Split
from models.user import User


class ExpenseController:
    def __init__(self, group: Group):
        self.__expenses: List[Expense] = []

    def add_expense(
        self,
        description: str,
        paid_by_user: User,
        total_amount: float,
        splits: List[Split],
        type,
    ):
        created_expense = Expense(
            description=description, splits=splits, total_amount=total_amount
        )
