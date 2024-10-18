from fastapi import FastAPI, Request, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from config.db import conn
from bson import ObjectId

note=APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get('/')
async def home_page(request: Request):
    noteColl=[]
    docs=conn.NoteHub.notes.find()
    for doc in docs:

        noteColl.append({
            "id":str(doc['_id']),
            "title":doc['title'],
            "desc":doc['desc'],
            "isImp":doc['isImp']
        })
    return templates.TemplateResponse("index.html",{"noteColl":noteColl,"request":request})
   
   
@note.delete("/delete/{id}")
async def delete_note(id:str):
    result=conn.NoteHub.notes.find_one_and_delete({"_id":ObjectId(id)})
    if result:
        return {"msg":"Deletion Successfull!"}
    else:
        return {"msg":"Deletion Failed!"}