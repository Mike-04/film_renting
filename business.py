import domain as d
movies=[]
clients=[]



def ADD_movie(movie):
    movies.append(movie)

def DEL_movie(id):
    global  movies
    movies = [movie for movie in movies if d.get_movie_id != id]

def MOD_movie(id,movie):
    for old_movie in movies:
        if d.get_movie_id == id:
            old_movie.update(movie)
            return
    raise "id_error"

def ADD_client(client):
    clients.append(client)

def DEL_client(id):
    global clients
    clients = [client for client in clients if d.get_client_id(client) != id]

def MOD_client(id,client):
    for old_client in clients:
        if d.get_client_id == id:
            old_client.update(client)
            return
    raise "id_error"

def get_movies():
    cmovies=movies
    return cmovies

def get_clients():
    cclients=clients
    return cclients