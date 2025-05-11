from dataclasses import dataclass
from typing import List

from book_my_show.models.seat import Seat


@dataclass
class Screen:
    __screen_id: int
    __seats: List[Seat]

    @property
    def get_screen_id(self):
        return self.__screen_id

    @__screen_id.setter
    def set_screen_id(self, screen_id):
        self.__screen_id = screen_id

    @property
    def get_seats(self):
        return self.__seats

    @__seats.setter
    def set_seats(self, seats):
        self.__seats = seats
