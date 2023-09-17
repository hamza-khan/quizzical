from sqlalchemy import Column, Integer, DateTime, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base

class PlaySessions(Base):
    __tablename__ = "play_sessions"

    id = Column(Integer, primary_key=True, index=True)
    started_at = Column(DateTime)

class Questions(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    options = relationship("Options")

class Options(Base):
    __tablename__ = "options"

    id = Column(Integer, primary_key=True, index=True)
    option = Column(String)
    selected = Column(Boolean, default=False)
    correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


