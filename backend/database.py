from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlalchemy_database_url = "postgresql://postgres:postgres@localhost:5432/quizzical"

engine = create_engine(sqlalchemy_database_url)

sessionLocal1 = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
