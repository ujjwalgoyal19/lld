from dataclasses import dataclass
from typing import List

from book_my_show.models.movie import Movie
from book_my_show.models.screen import Screen


@dataclass
class Show:
    __show_id: int
    __movie: Movie
    __screen: Screen
    __show_start_time: int
    __booked_seat_ids: List[int]

    @property
    def get_show_id(self) -> int:
        return self.__show_id

    @__show_id.setter
    def set_show_id(self, show_id):
        self.__show_id = show_id

    @property
    def get_movie(self) -> Movie:
        return self.__movie

    @__movie.setter
    def set_movie(self, movie):
        self.__movie = movie

    @property
    def get_screen(self):
        return self.__screen

    @__screen.setter
    def set_screen(self, screen):
        self.__screen = screen

    @property
    def get_show_start_time(self):
        return self.__show_start_time

    @__show_start_time.setter
    def set_show_start_time(self, show_start_time):
        self.__show_start_time = show_start_time

    @property
    def get_booked_seat_ids(self):
        return self.__booked_seat_ids

    @__booked_seat_ids.setter
    def set_booked_seat_ids(self, booked_seat_ids):
        self.__booked_seat_ids = booked_seat_ids

    def is_show_for_movie(self, movie: Movie) -> bool:
        return self.__movie.get_movie_id() == movie.get_movie_id()
