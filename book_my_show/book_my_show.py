from ast import List
from dataclasses import dataclass

from book_my_show.enums.city import City
from book_my_show.enums.seat_category import SeatCategory
from book_my_show.models.movie import Movie
from book_my_show.models.screen import Screen
from book_my_show.models.seat import Seat
from book_my_show.movie_controller import MovieController
from book_my_show.theatre_controller import TheatreController


class BookMyShow:
    def __init__(self):
        self.__movie_controller = MovieController()
        self.__theatre_controller = TheatreController()

    def initialize(self):
        self.__create_movies()
        self.__create_theatre()

    def __create_theatre(self):

        self.__theatre_controller()

    def __create_screens(self) -> List[Screen]:
        screens: List[Screen] = List()
        for i in range(0, 4):
            screens.append(Screen(i + 1, self.__create_seats()))

        return screens

    def __create_seats(self) -> List[Seat]:
        seats: List[Seat] = List()

        for i in range(0, 40):
            seats.append(Seat(i + 1, SeatCategory.SILVER))

        for i in range(40, 70):
            seats.append(Seat(i + 1, SeatCategory.GOLD))

        for i in range(70, 100):
            seats.append(Seat(i + 1, SeatCategory.PLATINUM))

        return seats

    def __create_movies(self):
        avengers_movie = Movie(1, "AVENGERS", 140)
        bahubali_movie = Movie(2, "BAHUBALI", 160)

        self.__movie_controller.add_movie(avengers_movie, City.JAIPUR)
        self.__movie_controller.add_movie(bahubali_movie, City.JAIPUR)
        self.__movie_controller.add_movie(avengers_movie, City.DELHI)
        self.__movie_controller.add_movie(bahubali_movie, City.DELHI)


if __name__ == "__main__":
    book_my_show: BookMyShow = BookMyShow()

    book_my_show.initialize()
    book_my_show.createBooking(City.JAIPUR, "AVENGERS")
    book_my_show.createBooking(City.DELHI, "AVENGERS")
