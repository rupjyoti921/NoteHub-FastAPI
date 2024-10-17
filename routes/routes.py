from fastapi import FastAPI, Request, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

note=APIRouter()
#note.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@note.get('/')
async def home_page(request: Request):
    # return templates.TemplateResponse("index.html",{"request": request})
    # return templates.TemplateResponse("index.html",{"request":request})
    return {"name":"rup"}
