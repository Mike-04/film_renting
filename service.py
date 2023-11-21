from domain import Movie
from domain import Client

#movie={'id':int,'name':string,'description':string,'genre':genre}
#client={'id':int,'name':string,'pid':string}


class MovieController:
    
    def __init__(self,val,repo):
        self.__val = val
        self.__repo = repo

    def create(self,name,description,genre):
        id=self.get_next_id()
        movie=Movie(id,name,description,genre)
        self.__val.validate(movie)
        self.__repo.add(movie)

    def get_next_id(self):
        existing_ids = {movie.get_id() for movie in self.__repo.get_all()}
        next_id = 1
        while next_id in existing_ids:
            next_id += 1
        return next_id
    
    def delete(self, ids):
        for movie_id in ids:
            self.__repo.remove(movie_id)

    def modify(self, id, name, description, genre):
        movie = Movie(id,name,description,genre)
        self.__repo.mod(id, movie)

    def search(self, prop):
        movies = self.__repo.get_all()
        matching_ids = []

        for movie in movies:
            movie_id = movie.get_id()

            if prop['property'] == 'id':
                if movie_id == int(prop['value']):
                    matching_ids.append(movie_id)
            elif prop['property'] == 'name':
                if movie.get_name() == prop['value']:
                    matching_ids.append(movie_id)
            elif prop['property'] == 'description':
                if movie.get_description() == prop['value']:
                    matching_ids.append(movie_id)
            elif prop['property'] == 'genre':
                if movie.get_genre() == prop['value']:
                    matching_ids.append(movie_id)

        return matching_ids


class ClientController:
    def __init__(self,val,repo):
        self.__val = val
        self.__repo = repo

    def create(self,name,pid):
        id=self.get_next_id()
        client=Client(id,name,pid)
        self.__val.validate(client)
        self.__repo.add(client)

    def get_next_id(self):
        existing_ids = {client.get_id() for client in self.__repo.get_all()}
        next_id = 1
        while next_id in existing_ids:
            next_id += 1
        return next_id
    
    def delete(self, ids):
        for client_id in ids:
            self.__repo.remove(client_id)

    def modify(self,name,pid):
        client = Client(id,name,pid)
        self.__repo.mod(id, client)

    def search(self, prop):
        clients = self.__repo.get_all()
        matching_ids = []

        for client in clients:
            client_id = client.get_id()

            if prop['property'] == 'id':
                if client_id == int(prop['value']):
                    matching_ids.append(client_id)
            elif prop['property'] == 'name':
                if client.get_name() == prop['value']:
                    matching_ids.append(client_id)
            elif prop['property'] == 'pid':
                if client.get_pid() == prop['value']:
                    matching_ids.append(client_id)

        return matching_ids
