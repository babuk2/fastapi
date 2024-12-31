from pydantic import BaseModel
from typing import Optional

class FrontPreferencesSchema(BaseModel):
    category: str
    public_type: str
    storage_type: str
    title: str
    end_point: str
    word_1: str
    word_2: str

    class Config:
        orm_mode = True
