from fastapi import APIRouter

from app.db import models, pydantic_models as pd
from app.db.database import service_session

router = APIRouter()


@router.post('/grades')
async def create_grade(data: pd.CreateGrade):
    with service_session() as session:
        grade = models.Grades(student_id=data.student_id, exam_id=data.exam_id, score=data.score)
        session.add(grade)
        session.commit()
        session.refresh(grade)

        return grade


@router.put('/grades{grade_id}')
async def update_grade(data: pd.UpdateGrade):
    with service_session() as session:
        obj = session.query(models.Grades).filter(models.Grades.id == data.grade_id).first()
        obj.score = data.score
        session.commit()
        session.refresh(obj)

        return obj.__dict__
