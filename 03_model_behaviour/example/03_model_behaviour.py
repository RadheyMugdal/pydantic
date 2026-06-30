from pydantic import BaseModel,field_validator,model_validator,computed_field

class User(BaseModel):
    username:str

    @field_validator('username')
    def username_length(cls,v):
        if len(v)<4:
            raise ValueError("Username must be at least 4 charactors")
        return v


class SignUpData(BaseModel):
    password:str
    confirm_password:str

    @model_validator(mode="after")
    def match_paass(cls,v):
        if v.password!=v.confirm_passsword:
            raise ValueError("Password do not match")
        return v