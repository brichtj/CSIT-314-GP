from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from Database import DB
from  boundary import *

app = FastAPI()

# Force singleton to initialize and connect DB
_ = DB()


app.include_router(login_boundary)