from domain import Movie
from domain import Client
from domain import Rent

class RentDTO:
    def __init__(self, rent_id, client, movie,comp):
        '''
        Parameters:
            rent_id (int): The unique identifier for the rent.
            client (Client): The Client object associated with the rent.
            movie (Movie): The Movie object associated with the rent.
        Description:
            Initializes a new RentDTO object with the provided parameters.
        '''
        self.rent_id = rent_id
        self.client = client
        self.movie = movie
        self.comp = comp

    def to_dict(self):
        '''
        Returns:
            dict: A dictionary representation of the RentDTO object.
                The dictionary includes rent_id, client information, and movie information.
        '''
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
            "comp":self.comp,
        }

    @classmethod
    def from_rent(cls, rent, client, movie,comp):
        '''
        Parameters:
            cls: The class itself.
            rent (Rent): The Rent object for which to create a RentDTO.
            client (Client): The Client object associated with the rent.
            movie (Movie): The Movie object associated with the rent.
        Returns:
            RentDTO: A new RentDTO object created from the provided Rent, Client, and Movie objects.
        Description:
            Creates a new RentDTO object using the specified Rent, Client, and Movie objects.
        '''
        return cls(rent.get_id(), client, movie, comp)