import string
import uuid
from abc import ABC
from typing import List

from enums import UserType
from models import Payment
from models.vehicle import Vehicle


class User(ABC):
    def __init__(self, name: str, type: UserType):
        self.user_id = string(uuid())
        self.name = name
        self.type = type


class Customer(User):
    def __init__(self, name: str, vehicle: Vehicle):
        self.vehicle = vehicle
        self.ticket = None
        self.payments: List[Payment] = []
        super().__init__(name=name, type=UserType.CUSTOMER)


class Admin(User):
    def __init__(self, name: str):
        super().__init__(name=name, type=UserType.ADMIN)
