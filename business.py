from domain import Movie
from domain import Client
from domain import Rent
import json
#movies=[{'id':id_value,'name':name_of_movie,'description':description_of_movie,'genre':genre_of_movie}]

class MovieRepository:
    def __init__(self):
        self.__movies=[]

    def add(self,movie):
        self.__movies.append(movie)

    def remove(self,movie_id): 
        for movie in self.__movies:
            if movie.get_id() == movie_id:
                self.__movies.remove(movie)
                return movie

    def mod(self,id,movie):
        self.remove(id)
        self.add(movie)

    def find(self, id):
        for movie in self.__movies:
            if movie.get_id() == id:
                return movie
        return None
    
    def size(self):
        return len(self.__movies)
    
    def get_all(self):
        return self.__movies
    
    def load_from_file(self, filename):
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
        self.__clients=[]

    def add(self,client):
        self.__clients.append(client)

    def remove(self,client_id):
        for client in self.__clients:
            if client.get_id() == client_id:
                self.__clients.remove(client)
                return client

    def mod(self,id,client):
        self.remove(id)
        self.add(client)

    def find(self, id):
        for client in self.__clients:
            if client.get_id() == id:
                return client
        return None
    
    def size(self):
        return len(self.__clients)
    
    def get_all(self):
        return self.__clients

    def load_from_file(self, filename):
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
        self.__rents=[]

    def add(self,rent):
        self.__rents.append(rent)

    def remove(self,rent_id):
        for rent in self.__rents:
            if rent.get_id() == rent_id:
                self.__rents.remove(rent)
                return rent

    def mod(self,id,rent):
        self.remove(id)
        self.add(rent)

    def find(self, id):
        for rent in self.__rents:
            if rent.get_id() == id:
                return rent
        return None
    
    def size(self):
        return len(self.__rents)
    
    def get_all(self):
        return self.__rents

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                jdata = json.load(file)
            print(f'Data successfully loaded from {filename}')
            for item in jdata:
                rent = rent(item['id'], item['client'], item['movie'])
                self.add(rent)
        except Exception as e:
            print(f'Error loading data from {filename}: {e}')

    def save_to_file(self, filename):
        client_data = []
        for rent in self.__rents:
            client_data.append({
                "id": rent.get_id(),
                "client": rent.get_client(),
                "movie": rent.get_movie()
            })

        try:
            with open(filename, 'w') as file:
                json.dump(client_data, file, indent=2)
            print(f'Data successfully saved to {filename}')
        except Exception as e:
            print(f'Error saving data to {filename}: {e}')
