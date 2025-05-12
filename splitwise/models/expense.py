import string
from typing import List
import uuid

from enums import SplitType
from models.split import Split
from models.user import User


class Expense:
    def __init__(
        self,
        description: str,
        total_amount: float,
        split_details: List[Split],
        split_type: SplitType,
        paid_by_user: User,
    ):
        self.__expense_id = str(uuid.uuid4())
        self.__description = description
        self.__total_amount = total_amount
        self.__paid_by_user = paid_by_user
        self.__split_details = split_details
        self.__split_type = split_type
