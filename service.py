import business as b
import domain as d
#movie={'id':int,'name':string,'description':string,'genre':genre}
#client={'id':int,'name':string,'pid':string}


def create_movie(id,name,description,genre):
    movie=d.Movie(id,name,description,genre)
    validator = d.ValidateMovie()
    try:
        validator.validate_movie(movie)
        return movie
    except Exception as ve:
        print("Validation errors:", ve)



def create_client(id,name,pid):
    client=d.Client(id,name,pid)
    validator = d.ValidateClient()
    try:
        validator.validate_client(client)
        return client
    except Exception as ve:
        print("Validation errors:", ve)


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
    client_ids = [int(client.get_client_id()) for client in clients]
    max_client_id = max(client_ids, default=-1) + 1
    available_ids = set(range(max_client_id + 1)) - set(client_ids)
    return min(available_ids)

def get_next_movie_id():
    movies = b.get_movies()
    movie_ids = [int(movie.get_movie_id()) for movie in movies]
    max_movie_id = max(movie_ids, default=-1) + 1
    available_ids = set(range(max_movie_id + 1)) - set(movie_ids)
    return min(available_ids)

def search_movie(prop):
    movies=b.get_movies()
    ids=[]
    match prop['property']:
        case 'id':
            id=int(prop['value'])
            for movie in movies:
                if movie.get_id()==id:
                    ids.append(movie.get_id())
        case 'name':
            name=prop['value']
            for movie in movies:
                if movie.get_name()==name:
                    ids.append(movie.get_id())
        case 'description':
            description=prop['value']
            for movie in movies:
                if movie.get_description()==description:
                    ids.append(movie.get_id())
        case 'genre':
            genre=prop['value']
            for movie in movies:
                if movie.get_genre()==genre:
                    ids.append(movie.get_id())
    return ids

def search_client(prop):
    clients=b.get_clients()
    ids=[]
    match prop['property']:
        case 'id':
            id=int(prop['value'])
            for client in clients:
                if client.get_id()==id:
                    ids.append(client.get_id())
        case 'name':
            name=prop['value']
            for client in clients:
                if client.get_name()==name:
                    ids.append(client.get_id())
        case 'pid':
            pid=prop['value']
            for client in clients:
                if client.get_pid()==pid:
                    ids.append(client.get_id())
    return ids
