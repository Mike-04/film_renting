class Client:
    def __init__(self,id,name,pid):
        self.__id=id
        self.__name=name
        self.__pid=pid

    def set_id(self,id):
        self.__id=id

    def set_name(self,name):
        self.__name=name

    def set_pid(self,pid):
        self.__pid=pid

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_pid(self):
        return self.__pid

    def __str__(self):
        return str(self.__id)+" "+self.__name+" "+self.__pid

class Movie:
    def __init__(self,id,name,description,genre):
        self.__id=id
        self.__name=name
        self.__description=description
        self.__genre=genre

    def set_id(self,id):
        self.__id=id

    def set_name(self,name):
        self.__name=name

    def set_description(self,description):
        self.__description=description

    def set_description(self,genre):
        self.__genre=genre

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_genre(self):
        return self.__genre

    def __str__(self):
        return str(self.__id)+" "+self.__name+" "+self.__description+" "+self.__genre
    
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
    