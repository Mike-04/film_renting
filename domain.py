class Client:
    def __init__(self,id,name,pid,rents):
        '''
        Parameters:
            id (int): The unique identifier for the client.
            name (str): The name of the client.
            pid (str): The personal identification number of the client.
            rents (int): The number of rents associated with the client.
        Description: 
            Initializes a new Client object with the provided parameters.
        '''
        self.__id=id
        self.__name=name
        self.__pid=pid
        self.__rents=rents

    def set_id(self,id):
        '''
        Parameters:
            id (int): The new unique identifier for the client.
        Description: 
            Sets the unique identifier for the client to the specified value.
        '''
        self.__id=id

    def set_name(self,name):
        '''
        Parameters:
            name (str): The new name for the client.
        Description: 
            Sets the name of the client to the specified value.
        '''
        self.__name=name

    def set_pid(self,pid):
        '''
        Parameters:
            pid (str): The new personal identification number for the client.
        Description: 
            Sets the personal identification number of the client to the specified value.
        '''
        self.__pid=pid

    def set_rents(self,rents):
        ''''
        Parameters:
            rents (int): The new number of rents associated with the client.
        Description: 
            Sets the number of rents associated with the client to the specified value.
        '''
        self.__rents=rents

    def get_id(self):
        '''
        Returns:
            int: The unique identifier for the client.
        '''
        return self.__id

    def get_name(self):
        '''
        Returns:
            str: The name of the client.
        '''
        return self.__name

    def get_pid(self):
        '''
        Returns:
            str: The personal identification number of the client.
        '''
        return self.__pid
    
    def get_rents(self):
        '''
        Returns:
            int: The number of rents associated with the client.
        '''
        return self.__rents

    def __str__(self):
        '''
        Returns:
            str: A string representation of the Client object.
        '''
        return str(self.__id)+" "+self.__name+" "+self.__pid+" "+str(self.__rents)

    def __eq__(self, other):
        '''
        Parameters:
            other (Client): Another Client object for comparison.
        Returns:
            bool: True if the two Client objects have the same unique identifier, False otherwise.
        '''
        return self.__id == other.__id


class Movie:
    def __init__(self,id,name,description,genre,rents,avb):
        '''
        Parameters:
            id (int): The unique identifier for the movie.
            name (str): The name of the movie.
            description (str): The description of the movie.
            genre (str): The genre of the movie.
            rents (int): The number of rents associated with the movie.
            avb (bool): The availability status of the movie.
        Description:
            Initializes a new Movie object with the provided parameters.
        '''
        self.__id=id
        self.__name=name
        self.__description=description
        self.__genre=genre
        self.__rents=rents
        self.__avb=avb

    def set_id(self,id):
        '''
        Parameters:
            id (int): The new unique identifier for the movie.
        Description:
            Sets the unique identifier for the movie to the specified value.
        '''
        self.__id=id

    def set_name(self,name):
        '''
        Parameters:
            name (str): The new name for the movie.
        Description:
            Sets the name of the movie to the specified value.
        '''
        self.__name=name

    def set_description(self,description):
        '''
        Parameters:
            description (str): The new description for the movie.
        Description:
            Sets the description of the movie to the specified value.
        '''
        self.__description=description

    def set_genre(self,genre):
        '''
        Parameters:
            genre (str): The new genre for the movie.
        Description:
            Sets the genre of the movie to the specified value.
        '''
        self.__genre=genre

    def set_rents(self,rents):
        '''
        Parameters:
            rents (int): The new number of rents associated with the movie.
        Description:
            Sets the number of rents associated with the movie to the specified value.
        '''
        self.__rents=rents

    def set_avb(self,avb):
        '''
        Parameters:
            avb (bool): The new availability status for the movie.
        Description:
            Sets the availability status of the movie to the specified value.
        '''
        self.__avb=avb

    def get_id(self):
        '''
        Returns:
            int: The unique identifier for the movie.
        '''
        return self.__id

    def get_name(self):
        '''
        Returns:
            str: The name of the movie.
        '''
        return self.__name

    def get_description(self):
        '''
        Returns:
            str: The description of the movie.
        '''
        return self.__description

    def get_genre(self):
        '''
        Returns:
            str: The genre of the movie.
        '''
        return self.__genre
    
    def get_rents(self):
        '''
        Returns:
            int: The number of rents associated with the movie.
        '''
        return self.__rents
    
    def get_avb(self):
        '''
        Returns:
            bool: The availability status of the movie.
        '''
        return self.__avb

    def __str__(self):
        '''
        Returns:
            str: A formatted string representation of the Movie object.
        '''
        return str(self.__id)+" "+self.__name+" "+self.__genre+" "+str(+self.__rents)+" "+str(self.__avb)+"\n"+self.__description
    
    def __eq__(self, other):
        '''
        Parameters:
            other (Movie): Another Movie object for comparison.
        Returns:
            bool: True if the two Movie objects have the same unique identifier, False otherwise.
        '''
        return self.__id == other.__id


class Rent:
    def __init__(self,id,cid,mid,comp):
        '''
        Parameters:
            id (int): The unique identifier for the rent.
            cid (int): The unique identifier of the client associated with the rent.
            mid (int): The unique identifier of the movie associated with the rent.
        Description:
            Initializes a new Rent object with the provided parameters.
        '''
        self.__id=id
        self.__cid=cid
        self.__mid=mid
        self.__comp=comp
    
    def get_id(self):
        '''
        Returns:
            int: The unique identifier for the rent.
        '''
        return self.__id

    def get_mid(self):
        '''
        Returns:
            int: The unique identifier of the movie associated with the rent.
        '''
        return self.__mid

    def get_cid(self):
        '''
        Returns:
            int: The unique identifier of the client associated with the rent.
        '''
        return self.__cid
    
    def get_comp(self):
        '''
        Returns:
            int: The unique identifier of the client associated with the rent.
        '''
        return self.__comp
    
    def set_id(self,id):
        '''
        Parameters:
            id (int): The new unique identifier for the rent.
        Description:
            Sets the unique identifier for the rent to the specified value.
        '''
        self.__id=id

    def set_mid(self,mid):
        '''
        Parameters:
            mid (int): The new unique identifier of the movie associated with the rent.
        Description:
            Sets the unique identifier of the movie associated with the rent to the specified value.
        '''
        self.__mid=mid

    def set_cid(self,cid):
        '''
        Parameters:
            cid (int): The new unique identifier of the client associated with the rent.
        Description:
            Sets the unique identifier of the client associated with the rent to the specified value.
        '''
        self.__cid=cid

    def set_comp(self,comp):
        '''
        Parameters:
            cid (int): The new unique identifier of the client associated with the rent.
        Description:
            Sets the unique identifier of the client associated with the rent to the specified value.
        '''
        self.__comp=comp

    def __str__(self):
        '''
        Returns:
            str: A formatted string representation of the Rent object.
        '''
        return str(self.__id)+" "+str(self.__cid)+" "+str(self.__mid)+" "+str(self.__comp)

    def __eq__(self, other):
        '''
        Parameters:
            other (Rent): Another Rent object for comparison.
        Returns:
            bool: True if the two Rent objects have the same unique identifier, False otherwise.
        '''
        return self.__id == other.__id


class ValidateMovie:
    def validate(self, movie):
        '''
        Parameters:
            movie (Movie): The Movie object to be validated.
        Raises:
            Exception: If any validation errors are found.
        '''
        errors = []
        if (movie.get_id()==""): errors.append("Id can not be empty!")
        if (movie.get_name()==""): errors.append("Name can not be empty!")
        if (movie.get_description()==""): errors.append("Description can not be empty!")
        if (movie.get_genre()==""): errors.append("Genre can not be empty!")
        if len(errors)>0:
            raise Exception(errors)

class ValidateClient:
    def validate(self, client):
        '''
        Parameters:
            client (Client): The Client object to be validated.
        Raises:
            Exception: If any validation errors are found.
        '''
        errors = []
        if (client.get_id()==""): errors.append("Id can not be empty!")
        if (client.get_name()==""): errors.append("Name can not be empty!")
        if (client.get_pid()==""): errors.append("Pid can not be empty!")
        if len(errors)>0:
            raise Exception(errors)
    
class ValidateRent:
    def validate(self, rent,movie):
        '''
        Parameters:
            rent (Rent): The Rent object to be validated.
            movie (Movie): The associated Movie object to be checked for availability.
        Raises:
            Exception: If any validation errors are found.
        '''
        errors = []
        if (rent.get_id()==""): errors.append("Id can not be empty!")
        if (movie.get_avb()==False): errors.append("Movie must be available")
        if len(errors)>0:
            raise Exception(errors)