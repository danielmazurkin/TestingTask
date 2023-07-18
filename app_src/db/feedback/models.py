from db.config import Base
from sqlalchemy import Column, Integer, String


class FeedbackModel(Base):
    """Модель c Feedback."""
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True)
    fio = Column(String(60))
    message = Column(String(512))
    contact_data = Column(String(200))

    def __repr__(self):
        return "<User(fio='%s', message='%s', contact_data='%s')>" % (
            self.fio, self.message, self.contact_data,
        )
