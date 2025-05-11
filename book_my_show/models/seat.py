from dataclasses import dataclass

from book_my_show.enums.seat_category import SeatCategory


@dataclass
class Seat:
    __seat_id: int
    __row: int
    __seat_category: SeatCategory

    @property
    def get_seat_id(self):
        return self.__seat_id

    @__seat_id.setter
    def set_seat_id(self, seat_id):
        self.__seat_id = seat_id

    @property
    def get_row(self):
        return self.__row

    @__row.setter
    def set_row(self, row):
        self.__row = row

    @property
    def get_seat_category(self):
        return self.__seat_category

    @__seat_category.setter
    def set_seat_category(self, seat_category):
        self.__seat_category = seat_category
