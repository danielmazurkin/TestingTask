from fastapi import APIRouter
from api.v1.feedback.serializer import FeedbackSerializer
from db.feedback.models import FeedbackModel
from typing import Any
from db.config import get_db
from fastapi import Depends
from db.config import get_db
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
from typing import List


router = APIRouter(
    prefix="/feedback",
    tags=["Operation"]
)


@router.get("/list/", status_code=status.HTTP_200_OK)
async def get_feedbacks_list(db: Session = Depends(get_db)) -> List[FeedbackSerializer]:
    """Эндпоинт для получения списка моделей Feedback."""
    feedbacks = db.query(FeedbackModel).all()
    return feedbacks


@router.get("/{feedback_id}/", status_code=status.HTTP_200_OK)
async def get_feedback(feedback_id: int, db: Session = Depends(get_db)) -> FeedbackSerializer:
    """Эндпоинт для получения feedback по заданному ID."""

    feedback = db.query(FeedbackModel).filter(FeedbackModel.id==feedback_id).first()

    if not feedback:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Запись с данным feedback не существует.')

    return feedback


@router.post("/create/", status_code=status.HTTP_201_CREATED)
async def create_feedback(payload: FeedbackSerializer, db: Session = Depends(get_db)) -> FeedbackSerializer:
    """Эндпоинт для создания модели фидбек."""

    new_feedback = FeedbackModel(**payload.dict())
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    return new_feedback


@router.put("/{feedback_id}/update/", status_code=status.HTTP_204_NO_CONTENT)
async def update_feedback(feedback_id: int, payload: FeedbackSerializer, db: Session = Depends(get_db)):
    """Эндпоинт для обновление модели с фидбеком."""

    feedback_query = db.query(FeedbackModel).filter(FeedbackModel.id == feedback_id)
    db_feedback = feedback_query.first()

    if not db_feedback:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Не найдена запись feedback c {feedback_id}')

    update_data = payload.dict(exclude_unset=True)
    feedback_query.filter(FeedbackModel.id == feedback_id).update(update_data,
                                                                  synchronize_session=False)
    db.commit()
    db.refresh(db_feedback)


@router.delete("/{feedback_id}/delete/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    """Модель для удаления feedback."""

    db_feedback = db.query(FeedbackModel).filter(FeedbackModel.id == feedback_id).first()

    if not db_feedback:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Запись для удаления не найдена.')

    db.delete(db_feedback)
    db.commit()
