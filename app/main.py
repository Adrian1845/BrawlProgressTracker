import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Absolute path configurations to safely pick up the local environment profile configuration
base_dir = Path(__file__).resolve().parent
if (base_dir / ".env").exists():
    load_dotenv(dotenv_path=base_dir / ".env")
elif (base_dir.parent / ".env").exists():
    load_dotenv(dotenv_path=base_dir.parent / ".env")

# Import our driving HTTP router controller
from app.adapters.driving.http_router import router as player_router

app = FastAPI(
    title="Brawl Progress Tracker API",
    description="Hexagonal Backend Core Engine proxying and evaluating accounts stats metrics.",
    version="1.0.0"
)

# Enable CORS configurations so your Astro UI can securely fetch data later from its own port
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Can be locked down to localhost:4321 later for Astro production deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register our sub-layer routers endpoints
app.include_router(player_router)

@app.get("/")
def read_root():
    return {"status": "Online", "engine": "FastAPI Hexagonal Architecture Core active"}