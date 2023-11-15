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

def add_movie(id,name,description,genre):
    movie=create_movie(id,name,description,genre)
    b.ADD_movie(movie)

def del_movie(ids):
    for id in ids:
        b.DEL_movie(id)

def mod_movie(id,name,description,genre):
    movie=create_movie(id,name,description,genre)
    b.MOD_movie(id,movie)
    
def add_client(id,name,pid):
    client=create_client(id,name,pid)
    b.ADD_client(client)

def del_client(ids):
    for id in ids:
        b.DEL_client(id)

def mod_client(id,name,pid):
    client=create_client(id,name,pid)
    b.MOD_client(id,client)

#prop={'property':'id,name,etc','value':'value'}

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

add_client(1,'Mike','328956495')
add_client(3,'Mike','32833246495')
add_client(2,'George','45325451')
prop={'property':'name','value':'Mike'}
print(search_client(prop))