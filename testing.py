from controller import MovieController, ClientController, RentController
from repository import MovieRepository, ClientRepository, RentRepository
from domain import ValidateMovie, ValidateClient, ValidateRent

class TestContainer:
    def __init__(self):
        '''
        Description:
            Initializes a new TestContainer object with MovieController, ClientController, and RentController instances.
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

    def test_movie_controller(self):
        '''
        Description:
            Performs tests for the MovieController.
        '''
        # Test creating movies
        for i in range(5):
            self.mctr.create(f"Movie{i}", f"Description{i}", f"Genre{i}")
            movies = self.mrep.get_all()
            name = movies[i].get_name()
            desc = movies[i].get_description()
            genre = movies[i].get_genre()
            assert(name == f"Movie{i}" and desc == f"Description{i}" and genre == f"Genre{i}")

        # Test deleting movies
        movies_to_delete = self.mrep.get_all()
        self.mctr.delete(movies_to_delete)
        assert len(self.mrep.get_all()) == 0

    def test_client_controller(self):
        '''
        Description:
            Performs tests for the ClientController.
        '''
        # Test creating clients
        for i in range(5):
            self.cctr.create(f"Client{i}", f"PID{i}")
            clients = self.crep.get_all()
            name = clients[i].get_name()
            pid = clients[i].get_pid()
            assert(name == f"Client{i}" and pid == f"PID{i}")

        # Test deleting clients
        clients_to_delete = self.crep.get_all()
        self.cctr.delete(clients_to_delete)
        clients = self.crep.get_all()
        assert len(clients) == 0

    def test_rent_controller(self):
        '''
        Description:
            Performs tests for the RentController.
        '''
        # Test creating rents
        for i in range(5):
            self.cctr.create(f"Client{i}", f"PID{i}")

        for i in range(5):
            self.mctr.create(f"Movie{i}", f"Description{i}", f"Genre{i}")

        for i in range(5):
            movie = self.mrep.get_all()[i]  # Assuming at least one movie is available
            client = self.crep.get_all()[i]  # Assuming at least one client exists
            self.rctr.create(client, movie)
            rents = self.rrep.get_all()

        # Test deleting rents
        rents_to_delete = self.rrep.get_all()
        self.rctr.delete(rents_to_delete)
        assert len(self.rrep.get_all()) == 0

    def run_tests(self):
        '''
        Description:
            Runs all the test methods in the TestContainer.
        '''
        self.test_movie_controller()
        self.test_client_controller()
        self.test_rent_controller()
