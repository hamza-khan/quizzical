from pydantic import BaseModel
from datetime import datetime


class PlaySessions(BaseModel):
    id: int
    started_at: datetime

    class Config:
        orm_mode = True

class CreatePlaySession(BaseModel):
    started_at: datetime

class Questions(BaseModel):
    id: int
    question: str
    created_at: datetime

    class Config:
        orm_mode = True

class CreateQuestions(BaseModel):
    question: str

class Options(BaseModel):
    id: int
    option: str
    selected: bool
    correct: bool
    created_at: datetime

    class Config:
        orm_mode = True

class CreateOptions(BaseModel):
    option: str
    selected: bool
    correct: bool