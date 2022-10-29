from typing import Union
from unittest import result
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import requests
import json
import sys

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

origins = [
    "http://localhost:3000",
    "http://localhost:3000/apitest",
    "http://localhost:81",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_home(request: Request):   
    return templates.TemplateResponse('home.html', context={'request': request, 'result': ""})

@app.get("/login", response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse("login.html", {'request': request, 'result': ""})

@app.get("/test_id/{id}")
def get_id(id: str):   
    return {"id":id}
