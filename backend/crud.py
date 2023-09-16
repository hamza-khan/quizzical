from sqlalchemy.orm import Session
from fastapi import HTTPException

import models, schemas

# SESSIONS
def get_all_sessions(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.PlaySessions).offset(skip).limit(limit).all()

def get_one_session(db: Session, session_id: int):
    return db.query(models.PlaySessions).filter(models.PlaySessions.id==session_id).first()

def add_a_session(db:Session, session: schemas.CreatePlaySession):
    db_session = models.PlaySessions(
        started_at = session.started_at
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

def update_a_sesion(db:Session, session_id: int, session: schemas.CreatePlaySession):
    db_session = db.query(models.PlaySessions).filter(models.PlaySessions.id==session_id).first()

    if db_session in None:
        return HTTPException(status_code=404, detail=f"session_id={session_id} does not exist")
    
    session_data = session.model_dump(exclude_unset=True)

    for key, val in session_data.items():
        setattr(db_session, key, val)
    
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

def delete_a_session(db:Session, session_id:int):
    db_session = db.query(models.PlaySessions).filter(models.PlaySessions.id==session_id).first()

    if db_session in None:
        return HTTPException(status_code=404, detail=f"session_id={session_id} does not exist. Nothing to delete")
    
    db.delete(db_session)
    db.commit()
    return {"ok": True}

# QUESTIONS
def get_all_questions(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.Questions).offset(skip).limit(limit).all()

def get_one_question(db: Session, question_id: int):
    return db.query(models.Questions).filter(models.Questions.id==question_id).first()

def add_a_question(db:Session, question: schemas.CreateQuestions):
    db_question = models.Questions(
        started_at = question.started_at
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def update_a_question(db:Session, question_id: int, question: schemas.CreateQuestions):
    db_question = db.query(models.Questions).filter(models.Questions.id==question_id).first()

    if db_question in None:
        return HTTPException(status_code=404, detail=f"question_id={question_id} does not exist")
    
    question_data = question.model_dump(exclude_unset=True)

    for key, val in question_data.items():
        setattr(db_question, key, val)
    
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def delete_a_question(db:Session, question_id:int):
    db_question = db.query(models.Questions).filter(models.Questions.id==question_id).first()

    if db_question in None:
        return HTTPException(status_code=404, detail=f"question_id={question_id} does not exist. Nothing to delete")
    
    db.delete(db_question)
    db.commit()
    return {"ok": True}

# OPTIONS
def get_all_options(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.Options).offset(skip).limit(limit).all()

def get_one_option(db: Session, option_id: int):
    return db.query(models.Options).filter(models.Options.id==option_id).first()

def add_a_option(db:Session, option: schemas.CreateOptions):
    db_option = models.Options(
        started_at = option.started_at
    )
    db.add(db_option)
    db.commit()
    db.refresh(db_option)
    return db_option

def update_an_option(db:Session, option_id: int, option: schemas.CreateOptions):
    db_option = db.query(models.Options).filter(models.Options.id==option_id).first()

    if db_option in None:
        return HTTPException(status_code=404, detail=f"question_id={option_id} does not exist")
    
    option_data = option.model_dump(exclude_unset=True)

    for key, val in option_data.items():
        setattr(db_option, key, val)
    
    db.add(db_option)
    db.commit()
    db.refresh(db_option)
    return db_option

def delete_an_option(db:Session, option_id:int):
    db_option = db.query(models.Options).filter(models.Options.id==option_id).first()

    if db_option in None:
        return HTTPException(status_code=404, detail=f"option_id={option_id} does not exist. Nothing to delete")
    
    db.delete(db_option)
    db.commit()
    return {"ok": True}

