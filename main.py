from fastapi import FastAPI
from routes.routes import note

app=FastAPI()

app.include_router(note)
