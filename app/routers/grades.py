from fastapi import APIRouter

from app.db import models, pydantic_models as pd
from app.db.database import service_session

router = APIRouter()


@router.post('/grades')
async def create_grade(data: pd.CreateGrade) -> pd.GradeResponse:
    with service_session() as session:
        obj = models.Grades(student_id=data.student_id, exam_id=data.exam_id, score=data.score)
        session.add(obj)
        session.commit()
        session.refresh(obj)

        return pd.GradeResponse(**obj.__dict__)


@router.put('/grades{grade_id}')
async def update_grade(data: pd.UpdateGrade) -> pd.GradeResponse:
    with service_session() as session:
        obj = session.query(models.Grades).filter(models.Grades.id == data.grade_id).first()
        obj.score = data.score
        session.commit()
        session.refresh(obj)

        return pd.GradeResponse(**obj.__dict__)
