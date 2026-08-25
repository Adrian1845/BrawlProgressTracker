from pathlib import Path
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

base_dir = Path(__file__).resolve().parent
if (base_dir / ".env").exists():
    load_dotenv(dotenv_path=base_dir / ".env")
elif (base_dir.parent / ".env").exists():
    load_dotenv(dotenv_path=base_dir.parent / ".env")

from adapters.driving.http_router import router as player_router

app = FastAPI(
    title="Brawl Progress Tracker API",
    description="Hexagonal Backend Core Engine proxying and evaluating accounts stats metrics.",
    version="1.0.0"
)

def _read_cors_origins() -> list[str]:
    raw_origins = os.getenv("CORS_ORIGINS", "")
    origins = [origin.strip() for origin in raw_origins.split(",") if origin.strip()]
    if origins:
        return origins
    return ["http://localhost:4321", "http://127.0.0.1:4321"]

# Enable CORS configurations
app.add_middleware(
    CORSMiddleware,
    allow_origins=_read_cors_origins(),
    allow_origin_regex=os.getenv("CORS_ORIGIN_REGEX", r"https://.*\.vercel\.app"),
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register sub-layer routers endpoints
app.include_router(player_router)

@app.get("/")
def read_root():
    return {"status": "Online", "engine": "FastAPI Hexagonal Architecture Core active"}
