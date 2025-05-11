from dataclasses import dataclass
from typing import Dict, List

from book_my_show.enums.city import City
from book_my_show.models.movie import Movie


@dataclass
class MovieController:
    __city_vs_movies: Dict[City, List[Movie]]
    __all_movies: List[Movie]

    def add_movie(self, movie: Movie, city: City):
        self.__all_movies.append(movie)

        movies: List[Movie] = self.__city_vs_movies.get(city, List())
        movies.append(movie)
        self.__city_vs_movies[city] = movies

    def get_movie_by_name(self, movie_name: str) -> Movie:
        for movie in self.__all_movies:
            if movie.get_movie_name() == movie_name:
                return movie
        return None

    def get_movie_by_city(self, city: City) -> Movie:
        return self.__city_vs_movies.get(city)
