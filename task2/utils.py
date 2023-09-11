from sqlalchemy.orm import Session
from fastapi import HTTPException
import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(root_path)

from models import Person
import schemas


def get_user(db: Session, user_id: int):
    return db.query(Person).filter(Person.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(Person).filter(Person.name == name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Person).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.PersonCreate):
    db_user = Person(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db : Session , user : schemas.PersonCreate , db_user):
    db_user.name = user.name
    db.commit()
    return db_user

def delete_user(db: Session , db_user):
    db.delete(db_user)
    db.commit()
    db.close()
    return f"{db_user.name} deleted"
    
    

