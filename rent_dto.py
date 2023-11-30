from domain import Movie
from domain import Client
from domain import Rent

class RentDTO:
    def __init__(self, rent_id, client, movie):
        self.rent_id = rent_id
        self.client = client
        self.movie = movie

    def to_dict(self):
        return {
            "rent_id": self.rent_id,
            "client": {
                "id": self.client.get_id(),
                "name": self.client.get_name(),
                "pid": self.client.get_pid(),
                "rents": self.client.get_rents(),
            },
            "movie": {
                "id": self.movie.get_id(),
                "name": self.movie.get_name(),
                "description": self.movie.get_description(),
                "genre": self.movie.get_genre(),
                "rents": self.movie.get_rents(),
                "avb": self.movie.get_avb(),
            },
        }

    @classmethod
    def from_rent(cls, rent, client, movie):
        return cls(rent.get_id(), client, movie)