import unittest
from domain import Movie, Client, Rent, ValidateClient, ValidateMovie, ValidateRent
from controller import MovieController, ClientController, RentController
from repository import MovieRepository, ClientRepository, RentRepository
from rent_dto import RentDTO
import coverage

class WhiteBoxTests(unittest.TestCase):
    def setUp(self):
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

    def test_movie_controller_create(self):
        self.mctr.create("Movie1", "Description1", "Genre1")
        movies = self.mctr.get_all()
        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0].get_name(), "Movie1")
        self.assertEqual(movies[0].get_description(), "Description1")
        self.assertEqual(movies[0].get_genre(), "Genre1")

    def test_movie_controller_delete(self):
        self.mctr.create("Movie1", "Description1", "Genre1")
        movies_to_delete = self.mctr.get_all()
        self.mctr.delete(movies_to_delete)
        self.assertEqual(len(self.mctr.get_all()), 0)

    def test_client_controller_create(self):
        self.cctr.create("Client1", "PID1")
        clients = self.cctr.get_all()
        self.assertEqual(len(clients), 1)
        self.assertEqual(clients[0].get_name(), "Client1")
        self.assertEqual(clients[0].get_pid(), "PID1")

    def test_client_controller_delete(self):
        self.cctr.create("Client1", "PID1")
        clients_to_delete = self.cctr.get_all()
        self.cctr.delete(clients_to_delete)
        self.assertEqual(len(self.cctr.get_all()), 0)

    def test_rent_controller_create(self):
        self.cctr.create("Client1", "PID1")
        self.mctr.create("Movie1", "Description1", "Genre1")

        client = self.cctr.get_all()[0]
        movie = self.mctr.get_all()[0]

        self.rctr.create(client, movie)
        rents = self.rctr.get_all()
        self.assertEqual(len(rents), 1)
        self.assertEqual(rents[0].get_cid(), client.get_id())
        self.assertEqual(rents[0].get_mid(), movie.get_id())

    def test_rent_controller_finish(self):
        self.cctr.create("Client1", "PID1")
        self.mctr.create("Movie1", "Description1", "Genre1")

        client = self.cctr.get_all()[0]
        movie = self.mctr.get_all()[0]

        self.rctr.create(client, movie)
        rent = self.rctr.get_all()[0]
        rent_id = rent.get_id()

        self.rctr.finish(rent_id)
        self.assertTrue(rent.get_comp())
        self.assertTrue(movie.get_avb())

    def test_white_box(self):
        # Additional white-box test cases go here
        pass

if __name__ == '__main__':
    # Run the tests with coverage
    cov = coverage.Coverage(source=["controller", "domain", "repository", "rent_dto"])
    cov.start()

    unittest.main()

    # Stop coverage and generate a report
    cov.stop()
    cov.save()
    cov.report()