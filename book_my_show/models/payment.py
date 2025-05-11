from dataclasses import dataclass
from enum import Enum


class PaymentStatus(Enum):
    FAILED = "failed"
    COMPLETED = "completed"
    IN_PROGRESS = "in-progress"


@dataclass
class Payment:
    __payment_id: int
    __amount: int
    __status: PaymentStatus

    @property
    def get_payment_id(self):
        return self.__payment_id

    @__payment_id.setter
    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    @property
    def get_amount(self):
        return self.__amount

    @__amount.setter
    def set_amount(self, amount):
        self.__amount = amount

    @property
    def get_status(self):
        return self.__status

    @__status.setter
    def set_status(self, status):
        self.__status = status
