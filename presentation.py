
from domain import Movie
from domain import Client
import os

class Console:
    def __init__(self, mctr,cctr,rctr):
        """
          Initialise UI
          ctr StudentControler
          ctrgr GradeController
        """
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
    
    def __createdRent(self,a):
        propc={'property':a[0],'value':a[1]}
        propm={'property':a[2],'value':a[3]}
        clients=self.__cctr.search(propc)
        print("Selected client is",clients[0])
        movies=self.__mctr.search(propm)
        print("Selected movie is",movies[0])
        if(self.__get_confirm()):
            try:
                self.__rctr.create(clients[0],movies[0])
                movies[0].set_rents(movies[0].get_rents()+1)
                clients[0].set_rents(clients[0].get_rents()+1)
                movies[0].set_avb(False)
            except Exception as ex:
                print (ex)
    
    def __returnRents(self,a):
        rents=self.__rctr.get_all()
        rents_del=[]
        if len(a)==4:
            propc={'property':a[0],'value':a[1]}
            propm={'property':a[2],'value':a[3]}
            clients=[]
            movies=[]
            rent_movies=[]
            movies=self.__mctr.search(propm)
            clients=self.__cctr.search(propc)
            print("The following rents will be returned:")
            for rent in rents:
                if rent.get_movie() in movies or rent.get_client() in clients:
                    print(rent)
            if(self.__get_confirm()):
                for rent in rents:
                    if rent.get_movie() in movies or rent.get_client() in clients:
                        rents_del.append(rent)
                        rent_movies.append(rent.get_movie())
                for movie in movies:
                    if movie in rent_movies:
                        movie.set_avb(True)
                self.__rctr.delete(rents_del) 
        elif len(a)==1:
            id=int(a[0])
            print("The following rents will be returned:")
            for rent in rents:
                if rent.get_id() == id:
                    print(rent)
            if(self.__get_confirm()):
                for rent in rents:
                    if rent.get_id() == id:
                        rents_del.append(rent)
                        rent.get_movie().set_avb(True)
                    self.__rctr.delete(rents_del)    

    def __printMovies(self,movies):
        for movie in movies:
            print(movie)
    
    def __printClients(self,clients):
        for client in clients:
            print(client)

    def __printRents(self,rents):
        for rent in rents:
            print(rent)
    
    def __get_confirm(self):
        input_string=input("Type CONFIRM to confirm the operation:")
        if(input_string=="CONFIRM"):
            return 1
        return 0

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
                                    self.__printClients(movies)
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
                                    self.__printClients(movies)
                                case "r":
                                    rents=self.__rctr.get_all()
                                    self.__printRents(rents)
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
            except:
                print("error")

