from domain import ValidateClient,ValidateMovie
from business import MovieRepository,ClientRepository,RentRepository
from service import MovieController,ClientController,RentController

from presentation import Console

rrep=RentRepository()
rval=[]
rctr=RentController(rval,rrep)

mrep=MovieRepository()
mval=ValidateMovie()
mctr=MovieController(mval,mrep,rctr)

crep=ClientRepository()
cval=ValidateClient()
cctr=ClientController(cval,crep,rctr)

ui=Console(mctr,cctr,rctr)
ui.startUI()