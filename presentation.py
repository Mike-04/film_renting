import business as b
import domain as d
import service as s

def load():
     b.load_data()

def save():
     b.save_data()

def print_movie(movie):
    name=d.get_movie_name(movie)
    description=d.get_movie_description(movie)
    genre=d.get_movie_genre(movie)
    print("Name:",name,"\nDescription:",description,"\nGenre:",genre,"\n")

def print_client(client):
    name=d.get_client_name(client)
    pid=d.get_client_pid(client)
    print("Name:",name,"PID:",pid)

def print_clients(ids):
        clients=b.get_clients()
        if(ids!=[-1]):
            for client in clients:
                if d.get_client_id(client) in ids:
                    print_client(client)
        else:
            for client in clients:
                print_client(client)
             

def print_movies(ids):
        movies=b.get_movies()
        if(ids!=[-1]):
            for movie in movies:
                if d.get_movie_id(movie) in ids:
                    print_movie(movie)
        else:
            for movie in movies:
                print_movie(movie)

def get_confirm():
    input_string=input("Type CONFIRM to confirm the operation:")
    if(input_string=="CONFIRM"):
        return 1
    return 0