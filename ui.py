
from domain import Movie
from domain import Client
import os

class Console:
    def __init__(self, mctr,cctr,rctr):
        self.__mctr = mctr
        self.__cctr = cctr
        self.__rctr = rctr

    def __readUserCommand(self):
        input_string=input(">>>")
        commands=input_string.split(";") 
        for comms in commands:
            comms=comms.strip()
            elem=comms.split(" ",1)
            comm_desc=elem[0].split("_")
            comm=comm_desc[0].strip()
            elem.append("")
            try:
                desc=comm_desc[1].strip()
            except:
                desc=[]
            args=elem[1].split(",")
            return (comm,desc,args)
        
    def __createdMovie(self,a):
        name = a[0].strip()
        description = a[1].strip()
        genre = a[2].strip()
        try:
            self.__mctr.create(name,description,genre)
        except Exception as ex:
            print (ex)

    def __createdRent(self,a):
        propc={'property':a[0],'value':a[1]}
        propm={'property':a[2],'value':a[3]}
        movies=self.__mctr.search(propm)
        clients=self.__cctr.search(propc)
        print("The following client:",clients[0],"will recive the following movie:",movies[0])
        if(self.__get_confirm()):
            self.__rctr.create(clients[0],movies[0])
    
    def __createdClient(self,a):
        name = a[0].strip()
        pid = a[1].strip()
        try:
            self.__cctr.create(name,pid)
        except Exception as ex:
            print (ex)

    def __createrClient(self,a):
        try:
            self.__cctr.creater(int(a))
        except Exception as ex:
            print (ex)
            
    def __printMovies(self,movies):
        for movie in movies:
            print(movie)
    
    def __printClients(self,clients):
        for client in clients:
            print(client)

    def __printRents(self,rents):
        for rent in rents:
            rent=self.__rctr.get_rent_dto(rent)
            print(rent["client"]["name"],"has",rent["movie"]["name"])
    
    def __get_confirm(self):
        input_string=input("Type confirm to confirm the operation:")
        if(input_string=="confirm"):
            return 1
        return 0

    def __rep1(self):
        clients=self.__cctr.get_r1()
        self.__printClients(clients)

    def __rep2(self):
        movies=self.__mctr.get_r2()
        self.__printMovies(movies)

    def __rep3(self):
        clients=self.__cctr.get_r3()
        self.__printClients(clients)

    def startUI(self):
        while True:
            try:
                (c,d,a) = self.__readUserCommand()
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
                                    prop={'property':a[0],'value':a[1]}
                                    clients=self.__cctr.search(prop)
                                    self.__printClients(clients)
                                case "m":
                                    prop={'property':a[0],'value':a[1]}
                                    movies=self.__mctr.search(prop)
                                    self.__printMovies(movies)
                                case "r":
                                    rents=self.__rctr.get_all()
                                    propc={'property':a[0],'value':a[1]}
                                    propm={'property':a[2],'value':a[3]}
                                    movies=self.__mctr.search(propm)
                                    clients=self.__cctr.search(propc)
                                    for rent in rents:
                                        if rent.get_movie() in movies or rent.get_client() in clients:
                                            print(rent)
                                case _:
                                    print("Invalid descriptor!")
                        case "del":
                            match d:
                                case "c":
                                    prop={'property':a[0],'value':a[1]}
                                    clients=self.__cctr.search(prop)
                                    print("Folowing entries will be deleted:")
                                    self.__printClients(clients)
                                    if(self.__get_confirm()):
                                        self.__cctr.delete(clients)
                                case "m":
                                    prop={'property':a[0],'value':a[1]}
                                    movies=self.__cctr.search(prop)
                                    print("Folowing entries will be deleted:")
                                    self.__printMovies(movies)
                                    if(self.__get_confirm()):
                                        self.__mctr.delete(movies)
                                case "r":
                                    self.__returnRents(a)
                                case _:
                                    print("Invalid descriptor!")
                        case "view":
                            match d:
                                case "c":
                                    clients=self.__cctr.get_all()
                                    self.__printClients(clients)
                                case "m":
                                    movies=self.__mctr.get_all()
                                    self.__printMovies(movies)
                                case "r":
                                    rents=self.__rctr.get_all()
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
                            print("Command:",c,"\nDescriptor:",d,"\nArgs:",a) 
            except Exception as ex:
                print(ex)

