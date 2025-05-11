from typing import List

from models import Spot


class Floor:
    def __init__(self, parking_spots: List[Spot]):
        self.__parking_spots: List[Spot] = parking_spots
        pass

    def add_parking_spots(self, parking_spots: List[Spot]):
        self.__parking_spots.extend(parking_spots)

    def add_parking_spot(self, parking_spot: Spot):
        self.__parking_spots.append(parking_spot)

    def get_all_parking_spots(self):
        return self.__parking_spots
