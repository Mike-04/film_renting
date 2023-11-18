import domain as d
import persistence as loaders
movies=[]
#movies=[{'id':id_value,'name':name_of_movie,'description':description_of_movie,'genre':genre_of_movie}]
clients=[]

def load_data():
    global movies,clients
    movies=loaders.load_movies_from_file('movies.json')
    clients=loaders.load_clients_from_file('clients.json')

def save_data():
    loaders.save_data_to_file(movies,'movies.json')
    loaders.save_data_to_file(clients,'clients.json')

def ADD_movie(movie):
    movies.append(movie)

def DEL_movie(id):
    global  movies
    movies = [movie for movie in movies if movie.get_id != id]

def MOD_movie(id,movie):
    for old_movie in movies:
        if movie.get_id == id:
            old_movie.update(movie)
            return
    raise "id_error"

def ADD_client(client):
    clients.append(client)

def DEL_client(id):
    global clients
    clients = [client for client in clients if client.get_id() != id]

def MOD_client(id,client):
    for old_client in clients:
        if client.get_id == id:
            old_client.update(client)
            return
    raise "id_error"

def get_movies():
    cmovies=movies
    return cmovies

def get_clients():
    cclients=clients
    return cclients
    