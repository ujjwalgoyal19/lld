from dataclasses import dataclass
from typing import List

from book_my_show.models.payment import Payment
from book_my_show.models.seat import Seat
from book_my_show.models.show import Show


@dataclass
class Booking:
    __show: Show
    __booked_seats: List[Seat]
    __payment: Payment

    @property
    def get_show(self):
        return self.__show

    @__show.setter
    def set_show(self, show):
        self.__show = show

    @property
    def get_booked_seats(self):
        return self.__booked_seats

    @__booked_seats.setter
    def set_booked_seats(self, booked_seats):
        self.__booked_seats = booked_seats

    @property
    def get_payment(self):
        return self.__payment

    @__payment.setter
    def set_payment(self, payment: Payment):
        self.__payment = payment
