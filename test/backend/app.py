from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware  # ✅ Added CORS import

from Database import DB
from boundary import *

from boundary.Cleaner.CreateCleanerBoundary import router as cleaner_boundary
from boundary.HomeOwner.CreateHomeOwnerBoundary import router as homeowner_boundary

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
app.include_router(cleaner_boundary)
app.include_router(user_admin_boundary)
app.include_router(home_owner_boundary)