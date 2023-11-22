from domain import Movie,Client,Rent

#movie={'id':int,'name':string,'description':string,'genre':genre}
#client={'id':int,'name':string,'pid':string}


class MovieController:
    
    def __init__(self,val,repo,rrctr):
        self.__val = val
        self.__repo = repo
        self.__rc=rrctr

    def create(self,name,description,genre):
        id=self.get_next_id()
        rents=0
        avb=True
        movie=Movie(id,name,description,genre,rents,avb)
        self.__val.validate(movie)
        self.__repo.add(movie)

    def get_next_id(self):
        existing_ids = {movie.get_id() for movie in self.__repo.get_all()}
        next_id = 1
        while next_id in existing_ids:
            next_id += 1
        return next_id
    
    def delete(self, movies):
        for movie in movies:
            movie_id=movie.get_id()
            associated_rents = [rent for rent in self.__rc.get_all() if rent.get_movie().get_id() == movie_id]
            self.__repo.remove(movie_id)
            self.__rc.delete(associated_rents)

    def modify(self, id, name, description, genre):
        movie = Movie(id,name,description,genre)
        self.__repo.mod(id, movie)

    def get_all(self):
        return self.__repo.get_all()

    def search(self, prop):
        movies = self.__repo.get_all()
        matching_movies = []
        for movie in movies:
            movie_id = movie.get_id()
            if prop['property'] == 'id':
                if movie_id == int(prop['value']):
                    matching_movies.append(movie)
            elif prop['property'] == 'name':
                if prop['value'] in movie.get_name():
                    matching_movies.append(movie)
            elif prop['property'] == 'description':
                if prop['value'] in movie.get_description():
                    matching_movies.append(movie)
            elif prop['property'] == 'genre':
                if prop['value'] in movie.get_genre():
                    matching_movies.append(movie)
        return matching_movies
    
    def load(self):
        self.__repo.load_from_file("movies.json")
    
    def save(self):
        self.__repo.save_to_file("movies.json")


class ClientController:
    def __init__(self,val,repo,rrctr):
        self.__val = val
        self.__repo = repo
        self.__rc=rrctr

    def create(self,name,pid):
        id=self.get_next_id()
        rents=0
        client=Client(id,name,pid,rents)
        self.__val.validate(client)
        self.__repo.add(client)

    def get_next_id(self):
        existing_ids = {client.get_id() for client in self.__repo.get_all()}
        next_id = 1
        while next_id in existing_ids:
            next_id += 1
        return next_id
    
    def delete(self, clients):
        for client in clients:
            client_id=client.get_id()
            associated_rents = [rent for rent in self.__rc.get_all() if rent.get_client().get_id() == client_id]
            self.__repo.remove(client_id)
            self.__rc.delete(associated_rents)

    def modify(self,name,pid):
        client = Client(id,name,pid)
        self.__repo.mod(id, client)

    def get_all(self):
        return self.__repo.get_all()

    def search(self, prop):
        clients = self.__repo.get_all()
        matching_clients = []

        for client in clients:
            client_id = client.get_id()

            if prop['property'] == 'id':
                if client_id == int(prop['value']):
                    matching_clients.append(client)
            elif prop['property'] == 'name':
                if prop['value'] in client.get_name(): 
                    matching_clients.append(client)
            elif prop['property'] == 'pid':
                if client.get_pid() == prop['value']:
                    matching_clients.append(client)

        return matching_clients

    def load(self):
        self.__repo.load_from_file("clients.json")
    
    def save(self):
        self.__repo.save_to_file("clients.json")

class RentController:
    def __init__(self,val,repo):
        self.__val = val
        self.__repo = repo

    def create(self,client,movie):
        id=self.get_next_id()
        rent=Rent(id,client,movie)
        self.__repo.add(rent)

    def get_next_id(self):
        existing_ids = {rent.get_id() for rent in self.__repo.get_all()}
        next_id = 1
        while next_id in existing_ids:
            next_id += 1
        return next_id
    
    def delete(self, rents):
        for rent in rents:
            rent_id=rent.get_id()
            self.__repo.remove(rent_id)

    def modify(self,client,movie):
        rent = rent(id,client,movie)
        self.__repo.mod(id, rent)

    def get_all(self):
        return self.__repo.get_all()

    def load(self):
        self.__repo.load_from_file("rents.json")
    
    def save(self):
        self.__repo.save_to_file("rents.json")
