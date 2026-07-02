from pydantic import BaseModel,ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street:str
    city:str
    zip_code:str

class User(BaseModel):
    id:int
    name:str
    email:str
    password:str
    is_active:bool=True
    createdAt:datetime
    address:Address
    tags:List[str]=[]
    model_config=ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )


# create user instance

user=User(
    id=1,
    name='radhey',
    email="radhey@gmail.com",
    password='new',
    address=Address(
        street='str',
        city='str',
        zip_code='str'
    ),
    createdAt=datetime(2024,3,15,14,30)
)

print(user)

# Using model_dump()=> dict 

user_dict=user.model_dump()
print(user_dict,type(dict))

# Using model_dump_json()

json_str=user.model_dump_json()

print(json_str,type(json_str))



# 