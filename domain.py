class Client:
    def __init__(self,id,name,pid,rents):
        '''
        Parameters:
        id (int): The unique identifier for the client.
        name (str): The name of the client.
        pid (str): The personal identification number of the client.
        rents (int): The number of rents associated with the client.
        Description: Initializes a new Client object with the provided parameters.
        '''
        self.__id=id
        self.__name=name
        self.__pid=pid
        self.__rents=rents

    def set_id(self,id):
        '''
        Parameters:
        id (int): The new unique identifier for the client.
        Description: Sets the unique identifier for the client to the specified value.
        '''
        self.__id=id

    def set_name(self,name):
        '''
        Parameters:
        name (str): The new name for the client.
        Description: Sets the name of the client to the specified value.
        '''
        self.__name=name

    def set_pid(self,pid):
        '''
        Parameters:
        pid (str): The new personal identification number for the client.
        Description: Sets the personal identification number of the client to the specified value.
        '''
        self.__pid=pid

    def set_rents(self,rents):
        ''''
        Parameters:
        rents (int): The new number of rents associated with the client.
        Description: Sets the number of rents associated with the client to the specified value.
        '''
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

    def __eq__(self, other):
        return self.__id == other.__id


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
    
    def __eq__(self, other):
        return self.__id == other.__id


class Rent:
    def __init__(self,id,cid,mid):
        self.__id=id
        self.__cid=cid
        self.__mid=mid
    
    def get_id(self):
        return self.__id

    def get_mid(self):
        return self.__mid

    def get_cid(self):
        return self.__cid
    
    def set_id(self,id):
        self.__id=id

    def set_mid(self,mid):
        self.__mid=mid

    def set_cid(self,cid):
        self.__cid=cid

    def __str__(self):
        return str(self.__id)+" "+str(self.__cid)+" "+str(self.__mid)

    def __eq__(self, other):
        return self.__id == other.__id


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
    
class ValidateRent:
    def validate(self, rent):
        errors = []
        if (rent.get_id()==""): errors.append("Id can not be empty!")
        if (rent.get_movie().get_avb()==False): errors.append("Movie must be available")
        if len(errors)>0:
            raise ValueError