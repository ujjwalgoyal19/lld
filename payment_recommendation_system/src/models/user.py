import string
from typing import List
import uuid


class User:
    def __init__(self, name: str ):
        self.user_id = string(uuid())
        self.name=name
        self.payment_prefrences: List = [] 
