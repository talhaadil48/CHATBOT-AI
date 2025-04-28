from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .get_routes import GetRoutes
from .post_routes import PostRoutes

app = FastAPI(title="Custom Backend Server")

# CORS Configuration
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://oraclia.vercel.app"  # Added your deployed frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registering routes
app.include_router(GetRoutes().get_router())
app.include_router(PostRoutes().get_router())
