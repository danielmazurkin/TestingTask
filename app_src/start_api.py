import logging
import uvicorn
from core.base import app
from db.config import Base, engine


def run_database():
    """Сделал без alembic потому что только одна модель."""
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    run_database()
    uvicorn.run(app, host="0.0.0.0", port=8000)
