import service as s
import business as b
import domain as d
import random as r
import string

def run_tests():
    for test in range (0,100):
        id=test
        name=''.join(r.choices(string.ascii_lowercase, k=5))
        description=''.join(r.choices(string.ascii_lowercase, k=5))
        genre=''.join(r.choices(string.ascii_lowercase, k=5))
        pid=''.join(r.choices(string.ascii_lowercase, k=5))
        print(id,name,description,genre,pid)
        client=s.create_client(id,name,pid)
        movie=s.create_movie(id,name,description,genre)
        assert(client.get_id()==id)
        assert(client.get_name()==name)
        assert(client.get_pid()==pid)
        assert(movie.get_id()==id)
        assert(movie.get_name()==name)
        assert(movie.get_description()==description)
        assert(movie.get_genre()==genre)
        movies_old=b.get_movies()
        clients_old=b.get_clients()
        b.ADD_client(client)
        b.ADD_movie(movie)
        movies=b.get_movies()
        clients=b.get_clients()
        movies_old.append(movie)
        clients_old.append(client)
        assert(movies==movies_old)
        assert(clients==clients_old)
        b.DEL_client(id)
        b.DEL_movie(id)
        movies=b.get_movies()
        clients=b.get_clients()
        assert(movies==[])
        assert(clients==[])

run_tests()
