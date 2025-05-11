from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware  # ✅ Added CORS import

from Database import DB
from Boundary import *

from Boundary import *

app = FastAPI()

# ✅ Add CORS middleware to allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can change to ["http://localhost:5173"] for stricter config
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB
_ = DB()

# Register routers
app.include_router(login_boundary)
app.include_router(service_boundary)
app.include_router(user_boundary)
app.include_router(user_profile_boundary)
app.include_router(category_boundary)
app.include_router(Shortlist_boundary)
app.include_router(match_boundary)