from fastapi import FastAPI
from boundary.loginBoundary import login_boundary

app = FastAPI()

app.include_router(login_boundary)
