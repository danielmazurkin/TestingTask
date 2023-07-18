from start_api import app
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from db.config import get_db, Base
from fastapi.testclient import TestClient
from sqlalchemy.ext.declarative import declarative_base
import os


DB_NAME_TEST = os.getenv('DB_NAME_TEST', default='feedback_test.db')
DATABASE_URL_TEST = f"sqlite:///{DB_NAME_TEST}"

engine_test = create_engine(DATABASE_URL_TEST, echo=True)
SessionTest = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

def get_db_test():
    """Необходимо для того чтобы переопределить базу данных для теста."""

    # Удаление базы данных после выполнения тестов
    db = SessionTest()

    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = get_db_test
Base.metadata.create_all(bind=engine_test)
client = TestClient(app)


def pytest_unconfigure(config):
    """Код для завершающих операций или очистки ресурсов после всех тестов"""
    os.remove(f"{DB_NAME_TEST}")
