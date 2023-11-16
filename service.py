import business as b
import domain as d
#movie={'id':int,'name':string,'description':string,'genre':genre}
#client={'id':int,'name':string,'pid':string}
def create_movie(id,name,description,genre):
    movie={'id':'NaN','name':'NaN','description':'NaN','genre':'NaN'}
    d.set_movie_id(movie,id)
    d.set_movie_name(movie,name)
    d.set_movie_description(movie,description)
    d.set_movie_genre(movie,genre)
    return movie

def create_client(id,name,pid):
    client={'id':'NaN','name':'NaN','pid':'NaN'}
    d.set_client_id(client,id)
    d.set_client_name(client,name)
    d.set_client_pid(client,pid)
    return client

def add_movie(name,description,genre):
    id=get_next_movie_id()
    movie=create_movie(id,name,description,genre)
    b.ADD_movie(movie)

def del_movie(ids):
    for id in ids:
        b.DEL_movie(id)

def mod_movie(id,name,description,genre):
    movie=create_movie(id,name,description,genre)
    b.MOD_movie(id,movie)
    
def add_client(name,pid):
    id=get_next_client_id()
    client=create_client(id,name,pid)
    b.ADD_client(client)

def del_client(ids):
    for id in ids:
        b.DEL_client(id)

def mod_client(id,name,pid):
    client=create_client(id,name,pid)
    b.MOD_client(id,client)

#prop={'property':'id,name,etc','value':'value'}
def get_next_client_id():
    clients = b.get_clients()
    client_ids = [int(d.get_client_id(client)) for client in clients]
    max_client_id = max(client_ids, default=-1) + 1
    available_ids = set(range(max_client_id + 1)) - set(client_ids)
    return min(available_ids)

def get_next_movie_id():
    movies = b.get_movies()
    movie_ids = [int(d.get_movie_id(movie)) for movie in movies]
    max_movie_id = max(movie_ids, default=-1) + 1
    available_ids = set(range(max_movie_id + 1)) - set(movie_ids)
    return min(available_ids)

def search_movie(prop):
    movies=b.get_movies()
    print(movies)
    ids=[]
    match prop['property']:
        case 'id':
            id=int(prop['value'])
            for movie in movies:
                if d.get_movie_id(movie)==id:
                    ids.append(d.get_movie_id(movie))
        case 'name':
            name=prop['value']
            for movie in movies:
                if d.get_movie_name(movie)==name:
                    ids.append(d.get_movie_id(movie))
        case 'description':
            description=prop['value']
            for movie in movies:
                if d.get_movie_description(movie)==description:
                    ids.append(d.get_movie_id(movie))
        case 'genre':
            genre=prop['value']
            for movie in movies:
                if d.get_movie_genre(movie)==genre:
                    ids.append(d.get_movie_id(movie))
    return ids

def search_client(prop):
    clients=b.get_clients()
    print(clients)
    ids=[]
    match prop['property']:
        case 'id':
            id=int(prop['value'])
            for client in clients:
                if d.get_client_id(client)==id:
                    ids.append(d.get_client_id(client))
        case 'name':
            name=prop['value']
            for client in clients:
                if d.get_client_name(client)==name:
                    ids.append(d.get_client_id(client))
        case 'pid':
            pid=prop['value']
            for client in clients:
                if d.get_client_pid(client)==pid:
                    ids.append(d.get_client_id(client))
    return ids
