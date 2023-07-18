from pydantic import BaseModel
from typing import Optional


class FeedbackSerializer(BaseModel):
    """Сериализатор для Feedback. """
    id: Optional[int] = None
    fio: str
    message: str
    contact_data: str

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True
