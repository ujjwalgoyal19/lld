from typing import List

from models.group import Group
from models.user import User


class GroupController:
    def __init__(self):
        self.__group_list: List[Group] = []

    def create_group(self, group_name: str, created_by_user: User):
        created_group = Group(group_name=group_name, created_by_user=created_by_user)
        created_group.add_member(created_by_user)
        self.__group_list.append(created_group)

    def get_group_by_id(self, group_id: str):
        for group in self.__group_list:
            if group.get_group_id() == group_id:
                return group
        return None
