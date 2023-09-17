from pydantic import BaseModel
from datetime import datetime
from typing import List


class PlaySessions(BaseModel):
    id: int
    started_at: datetime

    class Config:
        from_attributes = True

class CreatePlaySession(BaseModel):
    started_at: datetime

class Options(BaseModel):
    id: int
    option: str
    selected: bool
    correct: bool
    created_at: datetime
    question_id: int

    class Config:
        from_attributes = True

class CreateOptions(BaseModel):
    option: str
    selected: bool
    correct: bool
    question_id: int

class Questions(BaseModel):
    id: int
    question: str
    created_at: datetime
    options: List[Options]

    class Config:
        from_attributes = True

class CreateQuestions(BaseModel):
    question: str

