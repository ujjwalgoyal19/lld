from typing import List

from models.entry import Entry
from models.exit import Exit
from models.floor import Floor
from singleton import SingletonMeta


class ParkingLot(metaclass=SingletonMeta):
    def __init__(self):
        self.__parking_floors: List[Floor] = []
        self.__entries: List[Entry] = []
        self.__exits: List[Exit] = []

    @property
    def floors(self):
        return self.__parking_floors
