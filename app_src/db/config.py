import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


DB_NAME = os.getenv('DB_NAME', default='feedback.db')
PATH_TO_DB = f"sqlite:///{DB_NAME}"

engine = create_engine(PATH_TO_DB, echo=True)
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
