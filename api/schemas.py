from pydantic import BaseModel, UUID4
from typing import List

class CrewBase(BaseModel):
    name: str
    ship: str
    uuid: UUID4
    
class CreateCrew(BaseModel):
    name: str
    ship: str

class ResponseCreateCrew(BaseModel):
    message: str
    crew: str
