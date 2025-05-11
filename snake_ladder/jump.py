from typing import List


class Jump:
    def __init__(self, end):
        self.__end = end

    def get_end(self) -> List[int]:
        return self.__end
