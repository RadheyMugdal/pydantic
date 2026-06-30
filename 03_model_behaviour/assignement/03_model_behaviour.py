from pydantic import BaseModel,field_validator,computed_field,Field

# TODO: Create Booking Model

# Fields:
# - user_id: int
# - room_id: int
# - nights: int(must be >=1)
# - rate_per_night: float
# Also, add computed feild: total_amount= nights * rate_per_night



class Booking(BaseModel):
    usre_id:int
    room_id:int
    nights:int= Field(...,ge=1)

    # @field_validator
    # def validate_night(cls,v):
    #     if(v<1):
    #         raise ValueError("nights must be greater than 0")
    #     return v
    
    rate_per_night:float

    @computed_field
    @property
    def total_amount(self)->float:
        return self.nights* self.rate_per_night
    
