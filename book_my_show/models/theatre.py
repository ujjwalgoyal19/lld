from dataclasses import dataclass
from typing import List

from book_my_show.enums.city import City
from book_my_show.models.screen import Screen
from book_my_show.models.show import Show


@dataclass
class Theatre:
    __theatre_id: int
    __address: str
    __city: City
    __shows: List[Show]
    __screens: List[Screen]

    @property
    def get_theatre_id(self) -> int:
        return self.__theatre_id

    @__theatre_id.setter
    def set_theatre_id(self, theatre_id):
        self.__theatre_id = theatre_id

    @property
    def get_address(self) -> str:
        return self.__address

    @__address.setter
    def set_address(self, address: str):
        self.__address = address

    @property
    def get_city(self) -> City:
        return self.__city

    @__city.setter
    def set_city(self, city: City):
        self.__city = city

    @property
    def get_theatre_shows(self) -> List[Show]:
        return self.__shows

    @__shows.setter
    def set_theatre_shows(self, shows: List[Show]):
        self.__shows = shows

    @property
    def get_screens(self):
        return self.__screens

    @__screens.setter
    def set_screens(self, screens: List[Screen]):
        self.__screens = screens
