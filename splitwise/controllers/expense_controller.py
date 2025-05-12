from typing import List

from controllers.balance_sheet_controller import BalanceSheetController
from enums import SplitType
from factory.split_validatior_factory import SplitValidatorFactory
from models.expense import Expense
from models.group import Group
from models.split import Split
from models.split_validator import split_validator
from models.split_validator.split_validator import SplitValidator
from models.user import User


class ExpenseController:
    def __init__(self):
        self.__balance_sheet_controller = BalanceSheetController()

    def add_expense(
        self,
        description: str,
        paid_by_user: User,
        total_amount: float,
        splits: List[Split],
        type: SplitType,
    ):
        split_validator: SplitValidator = SplitValidatorFactory().build_split_validator(
            split_type=type
        )
        if not split_validator.validate(total_amount=total_amount, splits=splits):
            raise ValueError("Invalid splits for the given total amount.")
        new_expense = Expense(
            description=description,
            splits=splits,
            total_amount=total_amount,
            paid_by_user=paid_by_user,
            type=type,
        )
        self.__balance_sheet_controller.add_expense_to_balance_sheet(
            split_details=splits,
            total_amount=total_amount,
            user=paid_by_user,
        )
        return new_expense
