from typing import Dict, List

from models.balance import Balance
from models.balance_sheet import BalanceSheet
from models.split import Split
from models.user import User


class BalanceSheetController:

    def __increment_user_get_back_amount(
        self, user_id: str, user: User, amount: float
    ) -> None:
        user_balance_sheet = user.get_balance_sheet()
        user_balance_sheet.set_total_money_get_back(
            total_money_get_back=user_balance_sheet.get_total_money_get_back() + amount
        )
        user_balances = user_balance_sheet.get_users()
        user_balance: Balance = user_balances[user_id]
        user_balance.set_amount_owe(amount_owe=user_balance.get_amount_owe() + amount)
        user_balances[user_id] = user_balance
        user_balance_sheet.set_users(user_balances)

    def __increment_user_owed_amount(
        self, user_id: str, user: User, amount: float
    ) -> None:

        user_balance_sheet = user.get_balance_sheet()
        user_balance_sheet.set_total_money_owed(
            total_money_owed=user_balance_sheet.get_total_money_owed() + amount
        )
        user_balances = user_balance_sheet.get_users()
        user_balance: Balance = user_balances[user_id]
        user_balance.set_amount_get_back(
            amount_get_back=user_balance.get_amount_get_back() + amount
        )
        user_balances[user_id] = user_balance
        user_balance_sheet.set_users(user_balances)

    def add_expense_to_balance_sheet(
        self, user: User, split_details: List[Split], total_amount: float
    ) -> None:
        user_balance_sheet: BalanceSheet = user.get_balance_sheet()

        user_balance_sheet.set_total_payment_done(
            total_payment_done=user_balance_sheet.get_total_payment_done()
            + total_amount
        )

        for split in split_details:
            current_split_user = split.get_user()
            if current_split_user == user:
                user_balance_sheet.set_total_expense_done(
                    total_expense_done=user_balance_sheet.get_total_expense_done()
                    + split.amount
                )
            else:
                self.__increment_user_owed_amount(
                    user_id=current_split_user.get_user_id(),
                    user=current_split_user,
                    amount=split.amount,
                )
                self.__increment_user_get_back_amount(
                    user_id=user.get_user_id(),
                    user=user,
                    amount=split.amount,
                )
