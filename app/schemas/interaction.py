from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InteractionBase(BaseModel):
    user_input: str

class InteractionCreate(InteractionBase):
    pass

class InteractionResponse(InteractionBase):
    id: int
    intent: str
    response: str
    timestamp: datetime

    class Config:
        from_attributes = True
