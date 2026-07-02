from typing import List,Optional
from pydantic import BaseModel


class Address(BaseModel):
    street:str
    city:str
    postal_code:str

class User(BaseModel):
    id: int
    name:str
    address :Address

class Comment(BaseModel):
    id:int
    content: str
    replies: Optional[List['Comment']]= None


Comment.model_rebuild()


addr=Address(
    street="2344 new",
    city="Vadodara",
    postal_code="390001"
)

usr=User(
    id=1,
    name="Radhey",
    address=addr,
)

cmt=Comment(
    id=1,
    content="nice pic",
    replies= [
        Comment(
        id=2,
        content="Thank you"
    )
    ]
)