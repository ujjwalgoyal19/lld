from dataclasses import dataclass
from typing import Dict, List

from book_my_show.enums.city import City
from book_my_show.models.movie import Movie
from book_my_show.models.show import Show
from book_my_show.models.theatre import Theatre


@dataclass
class TheatreController:
    __city_vs_theatre: Dict[City, List[Theatre]]
    __all_theatres: List[Theatre]

    def add_theatre(self, theatre: Theatre, city: City):
        self.__all_theatres.append(theatre)

        theatres: List[Theatre] = self.__city_vs_theatre.get(city, List())
        theatres.append(theatre)
        self.__city_vs_theatre[city] = theatres

    def get_theatre_by_city(self, city: City) -> List[Theatre]:
        return self.__city_vs_theatre.get(city, List())

    def get_all_shows(self, movie: Movie, city: City) -> Dict[Theatre, List[Show]]:
        theatre_vs_shows: Dict[Theatre, List[Show]] = Dict()
        theatre_in_current_city: List[Theatre] = self.__city_vs_theatre.get(
            city, List()
        )

        for theatre in theatre_in_current_city:
            given_movie_shows: List[Show] = List()
            shows: List[Show] = theatre.get_theatre_shows()

            for show in shows:
                if show.is_show_for_movie(movie):
                    given_movie_shows[theatre].append(show)

            if len(given_movie_shows) != 0:
                theatre_vs_shows[theatre] = given_movie_shows

        return theatre_vs_shows
