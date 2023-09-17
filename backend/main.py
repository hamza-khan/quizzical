from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, schemas, models
from database import sessionLocal1, engine

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal1()
    try:
        yield db
    finally:
        db.close()


# SESSIONS
@app.get('/sessions/', tags=['sessions'], response_model=list[schemas.PlaySessions])
def get_sessions(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    return crud.get_all_sessions(skip=skip, limit=limit, db=db)

@app.get('/session/{session_id}', tags=['sessions'], response_model=schemas.PlaySessions)
def get_sessoin(session_id: int, db: Session = Depends(get_db)):
    session = crud.get_one_session(db=db, session_id=session_id)
    if session is None:
        return HTTPException(status_code=404, detail=f"could not find session of session_id={session_id}")
    return session

@app.post('/sessions/', tags=['sessions'], response_model=schemas.PlaySessions)
def post_session(session: schemas.CreatePlaySession, mydb: Session = Depends(get_db)):
    print("*******main********")
    print(mydb)
    print("*******main********")
    return crud.add_a_session(db=mydb, session=session)

@app.patch('/session/{session_id}', tags=['sessions'], response_model=schemas.PlaySessions)
def update_session(session_id: int, session: schemas.CreatePlaySession, db: Session = Depends(get_db)):
    return crud.update_a_sesion(db=db, session_id=session_id, session=session)

@app.delete('/session/{session_id}', tags=['sessions'])
def delete_session(session_id:int, db: Session = Depends(get_db)):
    return crud.delete_a_session(session_id=session_id, db=db)

# QUESTIONS
@app.get('/questions/', tags=['questions'], response_model=list[schemas.Questions])
def get_questions(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    return crud.get_all_questions(skip=skip, limit=limit, db=db)

@app.get('/question/{question_id}', tags=['questions'], response_model=schemas.Questions)
def get_question(question_id: int, db: Session = Depends(get_db)):
    question = crud.get_one_question(db=db, question_id=question_id)
    if question is None:
        return HTTPException(status_code=404, detail=f"could not find session of question_id={question_id}")
    return question

@app.post('/questions/', tags=['questions'], response_model=schemas.Questions)
def post_question(question: schemas.CreateQuestions, db: Session = Depends(get_db)):
    return crud.add_a_question(db=db, question=question)

@app.patch('/question/{question_id}', tags=['questions'], response_model=schemas.Questions)
def update_question(question_id: int, question: schemas.CreateQuestions, db: Session = Depends(get_db)):
    return crud.update_aquestion(db=db, question_id=question_id, question=question)

@app.delete('/question/{question_id}', tags=['questions'])
def delete_question(question_id:int, db: Session = Depends(get_db)):
    return crud.delete_a_question(question_id=question_id, db=db)


# OPTIONS
@app.get('/options/', tags=['options'], response_model=list[schemas.Options])
def get_options(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    return crud.get_all_options(skip=skip, limit=limit, db=db)

@app.get('/option/{option_id}', tags=['options'], response_model=schemas.Options)
def get_option(option_id: int, db: Session = Depends(get_db)):
    option = crud.get_one_option(db=db, option_id=option_id)
    if option is None:
        return HTTPException(status_code=404, detail=f"could not find session of question_id={option_id}")
    return option

@app.post('/options/', tags=['options'], response_model=schemas.Options)
def post_question(option: schemas.CreateOptions, db: Session = Depends(get_db)):
    return crud.add_an_option(db=db, question=option)

@app.patch('/option/{option_id}', tags=['options'], response_model=schemas.Options)
def update_option(option_id: int, option: schemas.CreateOptions, db: Session = Depends(get_db)):
    return crud.update_aoption(db=db, option_id=option_id, option=option)

@app.delete('/option/{option_id}', tags=['options'])
def delete_option(option_id:int, db: Session = Depends(get_db)):
    return crud.delete_an_option(option_id=option_id, db=db)
