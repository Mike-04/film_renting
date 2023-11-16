import business as b
import domain as d
import service as s
def print_movie(movie):
    id=d.get_movie_id(movie)
    name=d.get_movie_name(movie)
    description=d.get_movie_description(movie)
    genre=d.get_movie_genre(movie)
    print("ID:",id,"Name:",name,"Description:",description,"Genre:",genre)

def print_client(client):
    id=d.get_client_id(client)
    name=d.get_client_name(client)
    pid=d.get_client_pid(client)
    print("ID:",id,"Name:",name,"PID:",pid)

def print_clients(ids):
        clients=b.get_clients()
        for client in clients:
            if d.get_client_id(client) in ids:
                print_client(client)

def print_movies(ids):
        movies=b.get_movies()
        for movie in movies:
            if d.get_movie_id(movie) in ids:
                print_movie(movie)

print_clients([0,1])