from domain import ValidateClient,ValidateMovie,ValidateRent
from repository import MovieRepository,ClientRepository,RentRepository
from controller import MovieController,ClientController,RentController
from testing import TestContainer
from ui import Console

class DependencyContainer:
    def __init__(self):
        '''
        Description:
            Initializes a new DependencyContainer object with MovieController, ClientController, RentController, and Console instances.
        '''
        self.mrep = MovieRepository()
        self.mval = ValidateMovie()
        self.mctr = MovieController(self.mval, self.mrep)

        self.crep = ClientRepository()
        self.cval = ValidateClient()
        self.cctr = ClientController(self.cval, self.crep)
        self.rrep = RentRepository()
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
test_container=TestContainer()
test_container.run_tests()
dependency_container = DependencyContainer()
dependency_container.start_application()