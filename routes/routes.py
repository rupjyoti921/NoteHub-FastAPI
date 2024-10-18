from fastapi import FastAPI, Request, APIRouter,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from config.db import conn
from bson import ObjectId
from schemas.schema import Note
from fastapi.responses import RedirectResponse
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
    


@note.post("/create")
async def create_note(title: str = Form(...), desc: str = Form(...), isImp: str = Form(...)):
    note = Note(title=title, desc=desc, isImp=isImp)
    note_dict = note.dict()
    result = conn.NoteHub.notes.insert_one(note_dict)
    if result:
        return RedirectResponse(url='/', status_code=302)
    else:
        return RedirectResponse(url='/', status_code=302)
    

@note.post("/update")
async def update_note(edit_title: str = Form(...), edit_desc: str = Form(...), edit_isImp: str = Form(...), edit_id: str = Form(...)):
    id=edit_id
    note = Note(title=edit_title, desc=edit_desc, isImp=edit_isImp)
    note_dict = note.dict()
    result=conn.NoteHub.notes.find_one_and_update({"_id":ObjectId(id)},{"$set":note_dict})
    if result:
        return RedirectResponse(url='/', status_code=302)
    else:
        return RedirectResponse(url='/', status_code=302)
    