from domain import ValidateClient,ValidateMovie,ValidateRent
from repository import MovieRepository,ClientRepository,RentRepository,MovieFileRepository,ClientFileRepository,RentFileRepository
from controller import MovieController,ClientController,RentController
from ui import Console
import configparser

def load_config():
    config = configparser.ConfigParser()
    config.read('settings.properties')
    return config

class DependencyContainer:
    def __init__(self):
        '''
        Description:
            Initializes a new DependencyContainer object with MovieController, ClientController, RentController, and Console instances.
        '''
        config=load_config()
        repository_type = config.get('Repository', 'repository')
        clients_file=config.get('Repository', 'clients')
        rents_file=config.get('Repository', 'rents')
        movies_file=config.get('Repository', 'movies')
        
        match repository_type:
            case "memo":
                self.mrep = MovieRepository()
                self.crep = ClientRepository()
                self.rrep = RentRepository()
            case "json":
                self.mrep = MovieFileRepository(movies_file)
                self.crep = ClientFileRepository(clients_file)
                self.rrep = RentFileRepository(rents_file)


        self.mval = ValidateMovie()
        self.mctr = MovieController(self.mval, self.mrep)
 
        self.cval = ValidateClient()
        self.cctr = ClientController(self.cval, self.crep)
        
        self.rval = ValidateRent()
        self.rctr = RentController(self.rval, self.rrep, self.mctr, self.cctr)

        self.mctr.set_other_controllers(self.rctr)
        self.cctr.set_other_controllers(self.rctr)

        self.ui = Console(self.mctr, self.cctr, self.rctr)

    def start_application(self):
        '''
        Description:
            Starts the application by invoking the startUI method of the Console instance.
        '''
        self.ui.startUI()

# Usage
dependency_container = DependencyContainer()
dependency_container.start_application()