import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from qp import generate_password

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DIR = os.path.dirname(os.path.abspath(__file__))


class GenerateRequest(BaseModel):
    length: int = Field(default=32, ge=8, le=128)
    include_symbols: bool = True
    include_numbers: bool = True


@app.post("/generate")
async def generate(req: GenerateRequest):
    password = generate_password(req.length, req.include_symbols, req.include_numbers)
    return {"password": password}


@app.get("/")
def index():
    return FileResponse(os.path.join(DIR, "index.html"))
