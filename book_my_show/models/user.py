from dataclasses import dataclass


@dataclass
class User:
    __user_id: int
    __user_name: str

    @property
    def get_user_id(self):
        return self.__user_id

    @__user_id.setter
    def set_user_id(self, user_id):
        self.__user_id = user_id

    @property
    def get_user_name(self):
        return self.__user_name

    @__user_name.setter
    def set_user_name(self, user_name):
        self.__user_name = user_name
