from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from Database import DB
from  Boundary import *

app = FastAPI()

# Force singleton to initialize and connect DB
_ = DB()


app.include_router(login_boundary)
app.include_router(cleaner_boundary)
app.include_router(home_owner_boundary)