from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import ModelBase


class Person(ModelBase):
    __tablename__ = "persons"
    
    id = Column(Integer , primary_key = True , index = True)
    name = Column(String , unique = True,  index = True)


