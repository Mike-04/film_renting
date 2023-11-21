from domain import Movie
from domain import Client
import json
#movies=[{'id':id_value,'name':name_of_movie,'description':description_of_movie,'genre':genre_of_movie}]

class MovieRepository:
    def __init__(self):
        self.__movies=[]

    def add(self,movie):
        self.__movies.append(movie)

    def remove(self,id):
        movie = self.__movies[id]
        del self.__movies[id]
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
                movie = Movie(item['id'], item['name'], item['description'], item['genre'])
                self.add(movie)
        except Exception as e:
            print(f'Error loading data from {filename}: {e}')

class ClientRepository:
    def __init__(self):
        self.__clients=[]

    def add(self,client):
        self.__clients.append(client)

    def remove(self,id):
        client = self.__clients[id]
        del self.__clients[id]
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
                client = Client(item['id'], item['name'], item['pid'])
                self.add(client)
        except Exception as e:
            print(f'Error loading data from {filename}: {e}')

repository = MovieRepository()
repository.load_from_file('movies.json')

print(repository.find(10))

for movie in repository.get_all():
    print(movie)