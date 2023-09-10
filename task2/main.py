from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import schemas 
import utils
from db import SessionLocal, engine , ModelBase


ModelBase.metadata.create_all(bind=engine)

app= FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/", response_model=schemas.Persons)
def create_user(user: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_user = utils.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already used. User another name")
    return utils.create_user(db=db, user=user)

@app.get("/api/", response_model=list[schemas.Persons])
def read_all_users(db: Session = Depends(get_db)):
    db_user = utils.get_users(db)
    return db_user

@app.get("/api/{name}", response_model=schemas.Persons)
def read_users(user: schemas.PersonBase = None ,  db: Session = Depends(get_db) , name:str = None):
    if user:
        username = user.name
    elif name:
        username = name
    else:
        raise HTTPException(status_code = 400 , detail = "Specify user's name")
    db_user = utils.get_user_by_name(db, name=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/api/{name}" , response_model = schemas.Persons)
def updateItem(name:str, person:schemas.PersonBase, session: Session = Depends(get_db)):
    db_user = utils.get_user_by_name(session, name=name)
    if db_user:
        db_user = utils.update_user(session , person , db_user)
        return db_user
    raise HTTPException(status_code=404, detail="User not found")
    


@app.delete("/api/{name}")
def deleteItem(name:str, session: Session = Depends(get_db)):
    db_user = utils.get_user_by_name(session , name=name)
    if db_user:
        return utils.delete_user(session , db_user)
    raise HTTPException(status_code=404, detail="User not found")



    
