
from domain import Movie
from domain import Client
import os

import os

class Console:
    def __init__(self, mctr, cctr, rctr):
        '''
        Parameters:
            mctr (MovieController): The MovieController associated with this Console.
            cctr (ClientController): The ClientController associated with this Console.
            rctr (RentController): The RentController associated with this Console.
        Description:
            Initializes a new Console object with the provided MovieController, ClientController, and RentController.
        '''
        self.__mctr = mctr
        self.__cctr = cctr
        self.__rctr = rctr

    def __readUserCommand(self):
        '''
        Returns:
            tuple: A tuple containing the command, descriptor, and arguments entered by the user.
        Description:
            Reads and processes user commands, returning a tuple with the command, descriptor, and arguments.
        '''
        input_string = input(">>>")
        commands = input_string.split(";")
        for comms in commands:
            comms = comms.strip()
            elem = comms.split(" ", 1)
            comm_desc = elem[0].split("_")
            comm = comm_desc[0].strip()
            elem.append("")
            try:
                desc = comm_desc[1].strip()
            except:
                desc = []
            args = elem[1].split(",")
            return (comm, desc, args)

    def __createdMovie(self, a):
        '''
        Parameters:
            a (list): A list containing arguments for creating a movie.
        Description:
            Creates a new movie using the provided arguments and catches exceptions if any.
        '''
        name = a[0].strip()
        description = a[1].strip()
        genre = a[2].strip()
        try:
            self.__mctr.create(name, description, genre)
        except Exception as ex:
            print(ex)

    def __createdRent(self, a):
        '''
        Parameters:
            a (list): A list containing arguments for creating a rent.
        Description:
            Creates a new rent using the provided arguments, searches for clients and movies, and catches exceptions if any.
        '''
        propc = {'property': a[0], 'value': a[1]}
        propm = {'property': a[2], 'value': a[3]}
        movies = self.__mctr.search(propm)
        clients = self.__cctr.search(propc)
        print("The following client:", clients[0], "will receive the following movie:", movies[0])
        if self.__get_confirm():
            try:
                self.__rctr.create(clients[0], movies[0])
            except Exception as ex:
                print(ex)

    def __returnRents(self, a):
        if self.__get_confirm():
            try:
                id=int(a[0])
                self.__rctr.finish(id)
            except Exception as ex:
                print(ex)

    def __createdClient(self, a):
        '''
        Parameters:
            a (list): A list containing arguments for creating a client.
        Description:
            Creates a new client using the provided arguments and catches exceptions if any.
        '''
        name = a[0].strip()
        pid = a[1].strip()
        try:
            self.__cctr.create(name, pid)
        except Exception as ex:
            print(ex)

    def __createrClient(self, a):
        '''
        Parameters:
            a (list): A list containing the number of clients to create.
        Description:
            Creates a specified number of clients and catches exceptions if any.
        '''
        try:
            self.__cctr.creater(int(a))
        except Exception as ex:
            print(ex)

    def __printMovies(self, movies):
        '''
        Parameters:
            movies (list): A list of movies to be printed.
        Description:
            Prints the details of each movie in the provided list.
        '''
        for movie in movies:
            print(movie)

    def __printClients(self, clients):
        '''
        Parameters:
            clients (list): A list of clients to be printed.
        Description:
            Prints the details of each client in the provided list.
        '''
        for client in clients:
            print(client)

    def __printRents(self, rents):
        '''
        Parameters:
            rents (list): A list of rents to be printed.
        Description:
            Prints the details of each rent in the provided list.
        '''
        for rent in rents:
            rent = self.__rctr.get_rent_dto(rent)
            if(rent["comp"]==False):
                print(rent["rent_id"],rent["client"]["name"], "has", rent["movie"]["name"])

    def __get_confirm(self):
        '''
        Returns:
            int: 1 if the user types 'confirm,' 0 otherwise.
        Description:
            Reads user input and returns 1 if it matches 'confirm,' otherwise returns 0.
        '''
        input_string = input("Type confirm to confirm the operation:")
        if input_string == "confirm":
            return 1
        return 0

    def __rep1(self):
        '''
        Description:
            Prints a report of clients with rents.
        '''
        clients = self.__cctr.get_r1()
        self.__printClients(clients)

    def __rep2(self):
        '''
        Description:
            Prints a report of movies with rents.
        '''
        movies = self.__mctr.get_r2()
        self.__printMovies(movies)

    def __rep3(self):
        '''
        Description:
            Prints a report of clients with rents, limited to 30%.
        '''
        clients = self.__cctr.get_r3()
        self.__printClients(clients)
    
    def __rep4(self):
        '''
        Description:
            Prints a report of clients with rents, limited to 30%.
        '''
        movies = self.__rctr.get_r4()
        self.__printMovies(movies)

    def startUI(self):
        '''
        Description:
            Initiates the user interface, processes user commands, and performs corresponding actions until the user exits.
        '''
        while True:
            try:
                (c, d, a) = self.__readUserCommand()
                match c:
                    case "add":
                        match d:
                            case "c":
                                self.__createdClient(a)
                            case "m":
                                self.__createdMovie(a)
                            case "r":
                                self.__createdRent(a)
                            case "rc":
                                self.__createrClient(a[0])
                            case _:
                                print("Invalid descriptor!")
                    case "src":
                        match d:
                            case "c":
                                prop = {'property': a[0], 'value': a[1]}
                                clients = self.__cctr.search(prop)
                                self.__printClients(clients)
                            case "m":
                                prop = {'property': a[0], 'value': a[1]}
                                movies = self.__mctr.search(prop)
                                self.__printMovies(movies)
                            case "r":
                                rents = self.__rctr.get_all()
                                propc = {'property': a[0], 'value': a[1]}
                                propm = {'property': a[2], 'value': a[3]}
                                movies = self.__mctr.search(propm)
                                clients = self.__cctr.search(propc)
                                for rent in rents:
                                    if rent.get_movie() in movies or rent.get_client() in clients:
                                        print(rent)
                            case _:
                                print("Invalid descriptor!")
                    case "del":
                        match d:
                            case "c":
                                prop = {'property': a[0], 'value': a[1]}
                                clients = self.__cctr.search(prop)
                                print("Following entries will be deleted:")
                                self.__printClients(clients)
                                if self.__get_confirm():
                                    self.__cctr.delete(clients)
                            case "m":
                                prop = {'property': a[0], 'value': a[1]}
                                movies = self.__cctr.search(prop)
                                print("Following entries will be deleted:")
                                self.__printMovies(movies)
                                if self.__get_confirm():
                                    self.__mctr.delete(movies)
                            case "r":
                                self.__returnRents(a)
                            case _:
                                print("Invalid descriptor!")
                    case "view":
                        match d:
                            case "c":
                                clients = self.__cctr.get_all()
                                self.__printClients(clients)
                            case "m":
                                movies = self.__mctr.get_all()
                                self.__printMovies(movies)
                            case "r":
                                rents = self.__rctr.get_all()
                                self.__printRents(rents)
                            case _:
                                print("Invalid descriptor!")
                    case "rep":
                        match d:
                            case "1":
                                self.__rep1()
                            case "2":
                                self.__rep2()
                            case "3":
                                self.__rep3()
                            case "4":
                                self.__rep4()
                            case _:
                                print("Invalid descriptor!")
                    case "save":
                        self.__mctr.save()
                        self.__cctr.save()
                        self.__rctr.save()
                    case "load":
                        self.__mctr.load()
                        self.__cctr.load()
                        self.__rctr.load()
                    case "exit":
                        break
                    case "clearc":
                        os.system("cls")
                    case _:
                        print("Function error")
                        print("Command:", c, "\nDescriptor:", d, "\nArgs:", a)
            except Exception as ex:
                print(ex)
