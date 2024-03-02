import os
import sys

from fastapi import FastAPI

from .routes import provider

app = FastAPI()

app.include_router(provider.router)


@app.on_event("startup")
async def verify_api_key_set():
    if not os.getenv("API_KEY"):
        sys.exit("API_KEY not set")

