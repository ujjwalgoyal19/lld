import string
import uuid
from typing import List, Set

from controllers.expense_controller import ExpenseController
from enums import SplitType
from models.expense import Expense
from models.split import Split
from models.user import User


class Group:
    def __init__(
        self,
        group_name,
    ):
        self.__member_ids: Set[str] = {}
        self.__group_id = str(uuid.uuid4())
        self.__group_name = group_name
        self.__members: List[User] = []
        self.__expenses: List[Expense] = []
        self.__expense_controller = ExpenseController()

    @property
    def group_name(self):
        return self.__group_name

    def get_group_id(self):
        return self.__group_id

    def add_member(self, user: User):
        if user.get_user_id() in self.__member_ids:
            raise ValueError("User is already a member of this group.")
        self.__members.append(user)
        self.__member_ids.add(user.get_user_id())

    def add_expense(
        self,
        description: str,
        total_amount: float,
        splits: List[Split],
        paid_by_user: User,
        split_type: SplitType,
    ):
        if paid_by_user.get_user_id() not in self.__member_ids:
            raise ValueError("Paid by user is not a member of this group.")
        if len(splits) != len(self.__members):
            raise ValueError("Number of splits must match the number of members.")
        created_expense = self.__expense_controller.add_expense(
            description=description,
            paid_by_user=paid_by_user,
            total_amount=total_amount,
            splits=splits,
            split_type=split_type,
        )
        self.__expenses.append(created_expense)
