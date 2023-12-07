from domain import Movie
from domain import Client
from domain import Rent
import json
#movies=[{'id':id_value,'name':name_of_movie,'description':description_of_movie,'genre':genre_of_movie}]

class MovieRepository:
    def __init__(self):
        '''
        Description:
            Initializes a new MovieRepository object with an empty list of movies.
        '''
        self.__movies=[]

    def add(self,movie):
        '''
        Parameters:
            movie (Movie): The Movie object to be added to the repository.
        Description:
            Adds the provided Movie object to the repository.
        '''
        self.__movies.append(movie)

    def remove(self,movie_id): 
        '''
        Parameters:
            movie_id (int): The unique identifier of the movie to be removed.
        Returns:
            Movie: The removed Movie object.
        '''
        for movie in self.__movies:
            if movie.get_id() == movie_id:
                self.__movies.remove(movie)
                return movie

    def mod(self,id,movie):
        '''
        Parameters:
            id (int): The unique identifier of the movie to be modified.
            movie (Movie): The modified Movie object.
        Description:
            Removes the movie with the specified id and adds the modified Movie object to the repository.
        '''
        self.remove(id)
        self.add(movie)

    def find(self, id):
        '''
        Parameters:
            id (int): The unique identifier of the movie to be found.
        Returns:
            Movie or None: The Movie object with the specified id, or None if not found.
        '''
        for movie in self.__movies:
            if movie.get_id() == id:
                return movie
        return None
    
    def size(self):
        '''
        Returns:
            int: The number of movies in the repository.
        '''
        return len(self.__movies)
    
    def get_all(self):
        '''
        Returns:
            list: A list containing all Movie objects in the repository.
        '''
        return self.__movies
    
    def load_from_file(self, filename):
        '''
        Parameters:
            filename (str): The name of the file from which to load movie data.
        Description:
            Loads movie data from the specified file and adds Movie objects to the repository.
        '''
        try:
            with open(filename, 'r') as file:
                jdata = json.load(file)
            print(f'Data successfully loaded from {filename}')
            for item in jdata:
                movie = Movie(item['id'], item['name'], item['description'], item['genre'],item['rents'],item['avb'])
                self.add(movie)
        except Exception as e:
            print(f'Error loading data from {filename}: {e}')
    
    def save_to_file(self, filename):
        '''
        Parameters:
            filename (str): The name of the file to which to save movie data.
        Description:
            Saves movie data to the specified file.
        '''
        movie_data = []
        for movie in self.__movies:
            movie_data.append({
                "id": movie.get_id(),
                "name": movie.get_name(),
                "description": movie.get_description(),
                "genre": movie.get_genre(),
                "rents":movie.get_rents(),
                "avb":movie.get_avb()
            })

        try:
            with open(filename, 'w') as file:
                json.dump(movie_data, file, indent=2)
            print(f'Data successfully saved to {filename}')
        except Exception as e:
            print(f'Error saving data to {filename}: {e}')

class ClientRepository:
    def __init__(self):
        '''
        Description:
            Initializes a new ClientRepository object with an empty list of clients.
        '''
        self.__clients=[]

    def add(self,client):
        '''
        Parameters:
            client (Client): The Client object to be added to the repository.
        Description:
            Adds the provided Client object to the repository.
        '''
        self.__clients.append(client)

    def remove(self,client_id):
        '''
        Parameters:
            client_id (int): The unique identifier of the client to be removed.
        Returns:
            Client: The removed Client object.
        '''
        for client in self.__clients:
            if client.get_id() == client_id:
                self.__clients.remove(client)
                return client

    def mod(self,id,client):
        '''
        Parameters:
            id (int): The unique identifier of the client to be modified.
            client (Client): The modified Client object.
        Description:
            Removes the client with the specified id and adds the modified Client object to the repository.
        '''
        self.remove(id)
        self.add(client)

    def find(self, id):
        '''
        Parameters:
            id (int): The unique identifier of the client to be found.
        Returns:
            Client or None: The Client object with the specified id, or None if not found.
        '''
        for client in self.__clients:
            if client.get_id() == id:
                return client
        return None
    
    def size(self):
        '''
        Returns:
            int: The number of clients in the repository.
        '''
        return len(self.__clients)
    
    def get_all(self):
        '''
        Returns:
            list: A list containing all Client objects in the repository.
        '''
        return self.__clients

    def load_from_file(self, filename):
        '''
        Parameters:
            filename (str): The name of the file from which to load client data.
        Description:
            Loads client data from the specified file and adds Client objects to the repository.
        '''
        try:
            with open(filename, 'r') as file:
                jdata = json.load(file)
            print(f'Data successfully loaded from {filename}')
            for item in jdata:
                client = Client(item['id'], item['name'], item['pid'],item['rents'])
                self.add(client)
        except Exception as e:
            print(f'Error loading data from {filename}: {e}')

    def save_to_file(self, filename):
        '''
        Parameters:
            filename (str): The name of the file to which to save client data.
        Description:
            Saves client data to the specified file.
        '''
        client_data = []
        for client in self.__clients:
            client_data.append({
                "id": client.get_id(),
                "name": client.get_name(),
                "pid": client.get_pid(),
                "rents": client.get_rents()
            })
        try:
            with open(filename, 'w') as file:
                json.dump(client_data, file, indent=2)
            print(f'Data successfully saved to {filename}')
        except Exception as e:
            print(f'Error saving data to {filename}: {e}')

class RentRepository:
    def __init__(self):
        '''
        Description:
            Initializes a new RentRepository object with an empty list of rents.
        '''
        self.__rents=[]

    def add(self,rent):
        '''
        Parameters:
            rent (Rent): The Rent object to be added to the repository.
        Description:
            Adds the provided Rent object to the repository.
        '''
        self.__rents.append(rent)

    def remove(self,rent_id):
        '''
        Parameters:
            rent_id (int): The unique identifier of the rent to be removed.
        Returns:
            Rent: The removed Rent object.
        '''
        for rent in self.__rents:
            if rent.get_id() == rent_id:
                self.__rents.remove(rent)
                return rent

    def mod(self,id,rent):
        '''
        Parameters:
            id (int): The unique identifier of the rent to be modified.
            rent (Rent): The modified Rent object.
        Description:
            Removes the rent with the specified id and adds the modified Rent object to the repository.
        '''
        self.remove(id)
        self.add(rent)

    def find(self, id):
        '''
        Parameters:
            id (int): The unique identifier of the rent to be found.
        Returns:
            Rent or None: The Rent object with the specified id, or None if not found.
        '''
        for rent in self.__rents:
            if rent.get_id() == id:
                return rent
        return None
    
    def size(self):
        '''
        Returns:
            int: The number of rents in the repository.
        '''
        return len(self.__rents)
    
    def get_all(self):
        '''
        Returns:
            list: A list containing all Rent objects in the repository.
        '''
        return self.__rents

    def load_from_file(self, filename):
        '''
        Parameters:
            filename (str): The name of the file from which to load rent data.
        Description:
            Loads rent data from the specified file and adds Rent objects to the repository.
        '''
        try:
            with open(filename, 'r') as file:
                jdata = json.load(file)
            print(f'Data successfully loaded from {filename}')
            for item in jdata:
                id=item['id']
                mid=item['mid']
                cid=item['cid']
                rent=Rent(id,cid,mid)
                self.add(rent)
        except Exception as e:
            print(f'Error loading data from {filename}: {e}')

    def save_to_file(self, filename):
        '''
        Parameters:
            filename (str): The name of the file to which to save rent data.
        Description:
            Saves rent data to the specified file.
        '''
        rent_data=[]
        for rent in self.__rents:
            rent_data.append({
                "id": rent.get_id(),
                "cid":rent.get_cid(),
                "mid":rent.get_mid()
                })
        try:
            with open(filename, 'w') as file:
                json.dump(rent_data, file, indent=2)
            print(f'Data successfully saved to {filename}')
        except Exception as e:
            print(f'Error saving data to {filename}: {e}')
