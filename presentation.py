import business as b
import domain as d
import service as s

def load():
    b.load_data()

def save():
    b.save_data()

def print_movie(movie):
    name=movie.get_name()
    description=movie.get_description()
    genre=movie.get_genre()
    print("Name:",name,"\nDescription:",description,"\nGenre:",genre,"\n")

def print_client(client):
    name=client.get_name()
    pid=client.get_pid()
    print("Name:",name,"PID:",pid)

def print_clients(ids):
        clients=b.get_clients()
        if(ids!=[-1]):
            for client in clients:
                if client.get_id() in ids:
                    print_client(client)
        else:
            for client in clients:
                print_client(client)
             

def print_movies(ids):
        movies=b.get_movies()
        if(ids!=[-1]):
            for movie in movies:
                if movie.get_id() in ids:
                    print_movie(movie)
        else:
            for movie in movies:
                print_movie(movie)

def get_confirm():
    input_string=input("Type CONFIRM to confirm the operation:")
    if(input_string=="CONFIRM"):
        return 1
    return 0