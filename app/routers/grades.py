from fastapi import APIRouter

from app.db import models, schemas
from app.db.database import service_session

router = APIRouter()


@router.post('/grades', response_model=schemas.GradeResponse)
async def create_grade(data: schemas.CreateGrade) -> schemas.GradeResponse:
    """
    Create new grade in database
    """
    with service_session() as session:
        obj = models.Grades(student_id=data.student_id, exam_id=data.exam_id, score=data.score)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return schemas.GradeResponse(**obj.__dict__)


@router.put('/grades{grade_id}', response_model=schemas.GradeResponse)
async def update_grade(data: schemas.UpdateGrade) -> schemas.GradeResponse:
    """
    Update grade in database
    """
    with service_session() as session:
        obj = session.query(models.Grades).filter(models.Grades.id == data.grade_id).first()
        obj.score = data.score
        session.commit()
        session.refresh(obj)
        return schemas.GradeResponse(**obj.__dict__)
