from dataclasses import dataclass


@dataclass
class Movie:
    __movie_id: int
    __movie_name: str
    __movie_duration_in_minutes: int

    @property
    def get_movie_id(self):
        return self.__movie_id

    @__movie_id.setter
    def set_movie_id(self, movie_id):
        self.__movie_id = movie_id

    @property
    def get_movie_name(self):
        return self.__movie_name

    @__movie_name.setter
    def set_movie_name(self, movie_name):
        self.__movie_name = movie_name

    @property
    def get_movie_duration_in_minutes(self):
        return self.__movie_duration_in_minutes

    @__movie_duration_in_minutes.setter
    def set_movie_duration_in_minutes(self, movie_duration_in_minutes):
        self.__movie_duration_in_minutes = movie_duration_in_minutes
