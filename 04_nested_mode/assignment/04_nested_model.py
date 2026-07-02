from pydantic import BaseModel
from typing import List

#TODO: Create Course Model
# Each course has modules 
# Each module has lessons


class Lesson(BaseModel):
    id: int
    topic: str

class Module(BaseModel):
    id:int
    name:str
    lessons:List[Lesson]

class Course(BaseModel):
    id:int
    title:str
    modules:List[Lesson]