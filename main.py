from domain import ValidateMovie
from domain import ValidateClient
from business import MovieRepository
from business import ClientRepository
from service import MovieController
from service import ClientController

from presentation import Console

mrep=MovieRepository()
mval=ValidateMovie()
mctr=MovieController(mval,mrep)

crep=ClientRepository()
cval=ValidateClient()
cctr=ClientController(cval,crep)

rctr=[]

ui=Console(mctr,cctr,rctr)
ui.startUI()