from domain import Movie,Client,Rent
import random
from rent_dto import RentDTO

#movie={'id':int,'name':string,'description':string,'genre':genre}
#client={'id':int,'name':string,'pid':string}

first_names = ["John", "Jane", "Michael", "Emily", "David", "Sophia", "Daniel", "Olivia", "Christopher", "Emma"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

def bubble_sort_by_two_keys(data, key1_func, key2_func):
    n = len(data)

    for i in range(n):
        for j in range(0, n-i-1):
            key1_j = key1_func(data[j])
            key2_j = key2_func(data[j])
            key1_j1 = key1_func(data[j+1])
            key2_j1 = key2_func(data[j+1])
            if (key1_j > key1_j1) or (key1_j == key1_j1 and key2_j > key2_j1):
                data[j], data[j+1] = data[j+1], data[j]

def merge_sort(arr, key=None):
    """
    Merge sort is a recursive algorithm that continuously splits the array in half until it cannot be further divided i.e.,
    the array has only one element left (an array with one element is always sorted). 
    Then the sorted subarrays are merged into one sorted array.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half, key)
    right_half = merge_sort(right_half, key)

    return merge(left_half, right_half, key)

def merge(left, right, key):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

def comb_sort(arr, key=None):
    """
    Comb Sort is mainly an improvement over Bubble Sort. Bubble sort always compares adjacent values. 
    So all inversions are removed one by one. Comb Sort improves on Bubble Sort by using a gap of the size of more than 1.
    The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1.
    Complexity:
    Best case: O(n log n)
    Worst case: O(n^2)
    Average case: O(n^2/2^p) where p is the number of gap modifications
    """
    gap = len(arr)
    shrink_factor = 1.3
    swapped = True

    while gap > 1 or swapped:
        # Update the gap with the shrink factor
        gap = max(1, int(gap / shrink_factor))
        swapped = False

        for i in range(len(arr) - gap):
            j = i + gap

            if key(arr[i]) > key(arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True


class MovieController:
    def __init__(self, val, repo):
        '''
        Parameters:
            val (ValidateMovie): The validator for Movie objects.
            repo (MovieRepository): The repository for Movie objects.
        Description:
            Initializes a new MovieController object with the provided validator and repository.
        '''
        self.__val = val
        self.__repo = repo

    def set_other_controllers(self, rctr):
        '''
        Parameters:
            rctr (RentController): The RentController to be associated with this MovieController.
        Description:
            Sets the RentController to be associated with this MovieController.
        '''
        self.__rctr = rctr

    def find(self, id):
        '''
        Parameters:
            id (int): The unique identifier of the movie to be found.
        Returns:
            Movie: The Movie object with the specified ID, or None if not found.
        Description:
            Finds and returns the Movie object with the specified ID.
        '''
        movie = self.__repo.find(id)
        return movie

    def create(self, name, description, genre):
        '''
        Parameters:
            name (str): The name of the new movie.
            description (str): The description of the new movie.
            genre (str): The genre of the new movie.
        Description:
            Creates a new Movie object with the provided parameters and adds it to the repository.
            Validates the new movie using the validator.
        '''
        id = self.get_next_id()
        rents = 0
        avb = True
        movie = Movie(id, name, description, genre, rents, avb)
        self.__val.validate(movie)
        self.__repo.add(movie)

    def get_next_id(self):
        '''
        Returns:
            int: The next available ID for a movie.
        Description:
            Calculates and returns the next available ID for a movie in the repository.
        '''
        existing_ids = {movie.get_id() for movie in self.__repo.get_all()}
        next_id = 1
        while next_id in existing_ids:
            next_id += 1
        return next_id

    def delete(self, movies):
        '''
        Parameters:
            movies (list): A list of Movie objects to be deleted.
        Description:
            Deletes the specified movies from the repository.
            Also deletes associated rents from the associated RentController.
        '''
        cmovies = movies.copy()
        for movie in cmovies:
            movie_id = movie.get_id()
            associated_rents = [rent for rent in self.__rctr.get_all() if rent.get_mid() == movie_id]
            self.__repo.remove(movie_id)
            self.__rctr.delete(associated_rents)

    def modify(self, id, name, description, genre):
        '''
        Parameters:
            id (int): The ID of the movie to be modified.
            name (str): The new name for the movie.
            description (str): The new description for the movie.
            genre (str): The new genre for the movie.
        Description:
            Modifies the specified movie in the repository with the new information.
        '''
        movie = Movie(id, name, description, genre)
        self.__repo.mod(id, movie)

    def get_all(self):
        '''
        Returns:
            list: A list of all Movie objects in the repository.
        Description:
            Returns a list containing all Movie objects in the repository.
        '''
        return self.__repo.get_all()

    def get_r2(self):
        '''
        Returns:
            list: A list of Movie objects with rents greater than 0, sorted by rents in ascending order.
        Description:
            Returns a list of Movie objects with rents greater than 0, sorted by rents in ascending order.
        '''
        movies = self.__repo.get_all()
        movies = [movie for movie in movies if movie.get_rents() > 0]
        movies.sort(key=lambda movie: movie.get_rents(),reverse=True)
        return movies

    def search(self, prop):
        '''
        Parameters:
            prop (dict): A dictionary specifying the property and value to search for.
                Example: {'property': 'id', 'value': 1}
        Returns:
            list: A list of Movie objects matching the search criteria.
        Description:
            Searches for Movie objects in the repository based on the specified property and value.
        '''
        movies = self.__repo.get_all()
        matching_movies = []
        for movie in movies:
            movie_id = movie.get_id()
            if prop['property'] == 'id':
                if movie_id == int(prop['value']):
                    matching_movies.append(movie)
            elif prop['property'] == 'name':
                if prop['value'] in movie.get_name():
                    matching_movies.append(movie)
            elif prop['property'] == 'description':
                if prop['value'] in movie.get_description():
                    matching_movies.append(movie)
            elif prop['property'] == 'genre':
                if prop['value'] in movie.get_genre():
                    matching_movies.append(movie)
        return matching_movies

    def load(self):
        '''
        Description:
            Loads movie data from a file ("movies.json") into the repository.
        '''
        self.__repo.load_from_file("movies.json")

    def save(self):
        '''
        Description:
            Saves movie data from the repository to a file ("movies.json").
        '''
        self.__repo.save_to_file("movies.json")



class ClientController:
    def __init__(self, val, repo):
        '''
        Parameters:
            val (ValidateClient): The validator for Client objects.
            repo (ClientRepository): The repository for Client objects.
        Description:
            Initializes a new ClientController object with the provided validator and repository.
        '''
        self.__val = val
        self.__repo = repo

    def set_other_controllers(self, rctr):
        '''
        Parameters:
            rctr (RentController): The RentController to be associated with this ClientController.
        Description:
            Sets the RentController to be associated with this ClientController.
        '''
        self.__rctr = rctr

    def find(self, id):
        '''
        Parameters:
            id (int): The unique identifier of the client to be found.
        Returns:
            Client: The Client object with the specified ID, or None if not found.
        Description:
            Finds and returns the Client object with the specified ID.
        '''
        client = self.__repo.find(id)
        return client

    def creater(self, nr):
        '''
        Parameters:
            nr (int): The number of clients to be randomly created.
        Description:
            Creates the specified number of clients with random names and PIDs and adds them to the repository.
        '''
        if nr > 0:
            name = random.choice(first_names) + " " + random.choice(first_names)
            pid = "".join(str(random.randint(0, 10)) for _ in range(10))
            self.create(name, pid)
            self.creater(nr - 1)

    def create(self, name, pid):
        '''
        Parameters:
            name (str): The name of the new client.
            pid (str): The personal identification number of the new client.
        Description:
            Creates a new Client object with the provided parameters and adds it to the repository.
            Validates the new client using the validator.
        '''
        id = self.get_next_id()
        rents = 0
        client = Client(id, name, pid, rents)
        self.__val.validate(client)
        self.__repo.add(client)

    def get_next_id(self,current_id=1):
        '''
        Returns:
            int: The next available ID for a client.
        Description:
            Calculates and returns the next available ID for a client in the repository.
        '''
        existing_ids = {client.get_id() for client in self.__repo.get_all()}
        
        if current_id not in existing_ids:
            return current_id
        else:
            return self.get_next_id(current_id + 1)

    def delete(self, clients):
        '''
        Parameters:
            clients (list): A list of Client objects to be deleted.
        Description:
            Deletes the specified clients from the repository.
            Also deletes associated rents from the associated RentController.
        '''
        cclients = clients.copy()
        for client in cclients:
            client_id = client.get_id()
            associated_rents = [rent for rent in self.__rctr.get_all() if rent.get_cid() == client_id]
            self.__repo.remove(client_id)
            self.__rctr.delete(associated_rents)

    def modify(self, name, pid):
        '''
        Parameters:
            name (str): The new name for the client.
            pid (str): The new personal identification number for the client.
        Description:
            Modifies the specified client in the repository with the new information.
        '''
        client = Client(id, name, pid)
        self.__repo.mod(id, client)

    def get_all(self):
        '''
        Returns:
            list: A list of all Client objects in the repository.
        Description:
            Returns a list containing all Client objects in the repository.
        '''
        return self.__repo.get_all()

    def get_r1(self):
        '''
        Returns:
            list: A list of Client objects with rents greater than 0, sorted by name and rents.
        Description:
            Returns a list of Client objects with rents greater than 0, sorted by name and rents.
        '''
        clients = self.__repo.get_all()
        clients = [client for client in clients if client.get_rents() > 0]
        clients.sort(key=lambda client: (client.get_rents()),reverse=True)
        return clients

    def get_r3(self):
        '''
        Returns:
            list: A list of Client objects with rents greater than 0, sorted by rents and limited to 30% of the list.
        Description:
            Returns a list of Client objects with rents greater than 0, sorted by rents and limited to 30% of the list.
        '''
        clients = self.__repo.get_all()
        list_length = len(clients)
        clients = [client for client in clients if client.get_rents() > 0]
        clients.sort(key=lambda client: (client.get_rents(), client.get_name()),reverse=True)
        percentage = 30
        elements_to_keep = int(list_length * (percentage / 100))

        return clients[:elements_to_keep]

    def search(self, prop):
        '''
        Parameters:
            prop (dict): A dictionary specifying the property and value to search for.
                Example: {'property': 'id', 'value': 1}
        Returns:
            list: A list of Client objects matching the search criteria.
        Description:
            Searches for and returns a list of Client objects that match the specified property and value.
        '''
        clients = self.__repo.get_all()
        matching_clients = []

        for client in clients:
            client_id = client.get_id()

            if prop['property'] == 'id':
                if client_id == int(prop['value']):
                    matching_clients.append(client)
            elif prop['property'] == 'name':
                if prop['value'] in client.get_name():
                    matching_clients.append(client)
            elif prop['property'] == 'pid':
                if client.get_pid() == prop['value']:
                    matching_clients.append(client)

        return matching_clients

    def load(self):
        '''
        Description:
            Loads client data from a file ("clients.json") into the repository.
        '''
        self.__repo.load_from_file("clients.json")

    def save(self):
        '''
        Description:
            Saves client data from the repository to a file ("clients.json").
        '''
        self.__repo.save_to_file("clients.json")


class RentController:
    def __init__(self, val, repo, mctr, cctr):
        '''
        Parameters:
            val (ValidateRent): The validator for Rent objects.
            repo (RentRepository): The repository for Rent objects.
            mctr (MovieController): The MovieController associated with this RentController.
            cctr (ClientController): The ClientController associated with this RentController.
        Description:
            Initializes a new RentController object with the provided validator, repository, MovieController, and ClientController.
        '''
        self.__val = val
        self.__repo = repo
        self.__mctr = mctr
        self.__cctr = cctr

    def find(self, id):
        '''
        Parameters:
            id (int): The unique identifier of the rent to be found.
        Returns:
            Rent: The Rent object with the specified ID, or None if not found.
        Description:
            Finds and returns the Rent object with the specified ID.
        '''
        rent = self.__repo.find(id)
        return rent

    def create(self, client, movie):
        '''
        Parameters:
            client (Client): The client associated with the new rent.
            movie (Movie): The movie associated with the new rent.
        Description:
            Creates a new Rent object with the provided client and movie, validates it, and adds it to the repository.
        '''
        id = self.get_next_id()
        cid = client.get_id()
        mid = movie.get_id()
        ncr=client.get_rents()
        nmr=movie.get_rents()
        comp = False
        rent = Rent(id, cid, mid,comp)
        self.__val.validate(rent, movie)
        movie.set_rents(nmr+1)
        movie.set_avb(False)
        client.set_rents(ncr+1)
        self.__repo.add(rent)

    def finish(self,id):
        '''
        Parameters:
            client (Client): The client associated with the new rent.
            movie (Movie): The movie associated with the new rent.
        Description:
            Creates a new Rent object with the provided client and movie, validates it, and adds it to the repository.
        '''
        rent=self.__repo.find(id)
        movie=self.__mctr.find(rent.get_mid())
        movie.set_avb(True)
        rent.set_comp(True)

    def get_rent_dto(self, rent):
        '''
        Parameters:
            rent (Rent): The Rent object for which to create a RentDTO.
        Returns:
            dict: A dictionary representing the RentDTO.
        Description:
            Creates a RentDTO from the provided Rent object and returns it as a dictionary.
        '''
        client = self.__cctr.find(rent.get_cid())
        movie = self.__mctr.find(rent.get_mid())
        comp=rent.get_comp()
        rent_dto = RentDTO.from_rent(rent, client, movie, comp)
        return rent_dto.to_dict()

    def get_r4(self):
        movies=[]
        max_m=self.__mctr.get_next_id()
        movie_ids=[]
        for i in range(0,max_m+1):
            movie_ids.append({i:0})
        rents = self.__repo.get_all()
        for rent in rents:
            rent = self.get_rent_dto(rent)
            movie_id = int(rent["movie"]["id"])
            if(int(rent["client"]["pid"][:1])%2==1):
                movie_ids[movie_id][movie_id]+=1
        sorted_movie_ids = sorted(movie_ids, key=lambda x: list(x.values())[0], reverse=True)
        print(sorted_movie_ids)
        first = [list(d.keys())[0] for d in sorted_movie_ids[:5]]
        for id in first:
            movies.append(self.__mctr.find(id))
        return movies
         

    def get_next_id(self):
        '''
        Returns:
            int: The next available ID for a rent.
        Description:
            Calculates and returns the next available ID for a rent in the repository.
        '''
        existing_ids = {rent.get_id() for rent in self.__repo.get_all()}
        next_id = 1
        while next_id in existing_ids:
            next_id += 1
        return next_id

    def delete(self, rents):
        '''
        Parameters:
            rents (list): A list of Rent objects to be deleted.
        Description:
            Deletes the specified rents from the repository.
        '''
        crents = rents.copy()
        for rent in crents:
            rent_id = rent.get_id()
            self.__repo.remove(rent_id)

    def modify(self, client, movie):
        '''
        Parameters:
            client (Client): The client associated with the rent to be modified.
            movie (Movie): The movie associated with the rent to be modified.
        Description:
            Modifies the specified rent in the repository with the new client and movie.
        '''
        rent = Rent(id, client, movie)
        self.__repo.mod(id, rent)

    def get_all(self):
        '''
        Returns:
            list: A list of all Rent objects in the repository.
        Description:
            Returns a list containing all Rent objects in the repository.
        '''
        return self.__repo.get_all()

    def load(self):
        '''
        Description:
            Loads rent data from a file ("rents.json") into the repository.
        '''
        self.__repo.load_from_file("rents.json")

    def save(self):
        '''
        Description:
            Saves rent data from the repository to a file ("rents.json").
        '''
        self.__repo.save_to_file("rents.json")

