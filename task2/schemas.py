from pydantic import BaseModel



class PersonBase(BaseModel):
    name : str
    
class PersonCreate(PersonBase):
    pass

class Persons(PersonBase):
    id : int
    
    class Config:
        from_attributes = True
