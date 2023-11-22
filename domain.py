class Client:
    def __init__(self,id,name,pid,rents):
        self.__id=id
        self.__name=name
        self.__pid=pid
        self.__rents=rents

    def set_id(self,id):
        self.__id=id

    def set_name(self,name):
        self.__name=name

    def set_pid(self,pid):
        self.__pid=pid

    def set_rents(self,rents):
        self.__rents=rents

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_pid(self):
        return self.__pid
    
    def get_rents(self):
        return self.__rents

    def __str__(self):
        return str(self.__id)+" "+self.__name+" "+self.__pid+" "+str(self.__rents)

class Movie:
    def __init__(self,id,name,description,genre,rents,avb):
        self.__id=id
        self.__name=name
        self.__description=description
        self.__genre=genre
        self.__rents=rents
        self.__avb=avb

    def set_id(self,id):
        self.__id=id

    def set_name(self,name):
        self.__name=name

    def set_description(self,description):
        self.__description=description

    def set_description(self,genre):
        self.__genre=genre

    def set_rents(self,rents):
        self.__rents=rents

    def set_avb(self,avb):
        self.__avb=avb

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_genre(self):
        return self.__genre
    
    def get_rents(self):
        return self.__rents
    
    def get_avb(self):
        return self.__avb

    def __str__(self):
        return str(self.__id)+" "+self.__name+" "+self.__description+" "+self.__genre+" "+str(+self.__rents)+" "+str(self.__avb)
    
class Rent:
    def __init__(self,id,client,movie):
        self.__id=id
        self.__client=client
        self.__movie=movie
    
    def get_id(self):
        return self.__id

    def get_movie(self):
        return self.__movie

    def get_client(self):
        return self.__client
    
    def set_id(self,id):
        self.__id=id

    def set_movie(self,movie):
        self.__movie=movie

    def set_client(self,client):
        self.__client=client
    
    def __str__(self):
        return str(self.__id)+" "+str(self.__client.get_name())+": "+str(self.__movie.get_name())

class ValidateMovie:
    def validate(self, movie):
        errors = []
        if (movie.get_id()==""): errors.append("Id can not be empty!")
        if (movie.get_name()==""): errors.append("Name can not be empty!")
        if (movie.get_description()==""): errors.append("Description can not be empty!")
        if (movie.get_genre()==""): errors.append("Genre can not be empty!")
        if len(errors)>0:
            raise errors

class ValidateClient:
    def validate(self, client):
        errors = []
        if (client.get_id()==""): errors.append("Id can not be empty!")
        if (client.get_name()==""): errors.append("Name can not be empty!")
        if (client.get_pid()==""): errors.append("Pid can not be empty!")
        if len(errors)>0:
            raise errors
    