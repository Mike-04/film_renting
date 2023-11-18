import json
import domain as d
def load_movies_from_file(filename):
    movies=[]
    try:
        with open(filename, 'r') as file:
            jdata = json.load(file)
        print(f'Data successfully loaded from {filename}')
        for item in jdata:
            movie = d.Movie(item['id'], item['name'], item['description'], item['genre'])
            movies.append(movie)
        return movies
    except Exception as e:
        print(f'Error loading data from {filename}: {e}')
        return None
def load_clients_from_file(filename):
    clients=[]
    try:
        with open(filename, 'r') as file:
            jdata = json.load(file)
        print(f'Data successfully loaded from {filename}')
        for item in jdata:
            client = d.Client(item['id'], item['name'], item['pid'])
            clients.append(client)
        return clients
    except Exception as e:
        print(f'Error loading data from {filename}: {e}')
        return None
     
def save_data_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
        print(f'Data successfully saved to {filename}')
    except Exception as e:
        print(f'Error saving data to {filename}: {e}')