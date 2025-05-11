from typing import List

from models.user import User
from singleton import SingletonMeta


class UserController(meta=SingletonMeta):
    def __init__(self):
        self.__user_list: List[User] = []

    def create_user(self, user_name):
        created_user = User(user_name=user_name)
        self.__user_list.append(created_user)
