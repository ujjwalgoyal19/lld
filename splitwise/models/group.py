import string
import uuid
from typing import List, Set

from controllers.expense_controller import ExpenseController
from models.expense import Expense
from models.user import User


class Group:
    def __init__(self, group_name):
        self.__member_ids: Set[str] = {}
        self.__group_id = string(uuid.uuid4())
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



    def add_expense(self, description: str, total_amount: float, )