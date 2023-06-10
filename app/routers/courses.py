from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import IntegrityError

from app.db import models, pydantic_models as pd
from app.db.database import service_session

router = APIRouter()


@router.post('/course')
async def create_course(course: pd.Course):
    with service_session() as session:
        try:
            obj = models.Course(**course.dict())
            session.add(obj)
            session.commit()
            session.refresh(obj)
        except IntegrityError:
            raise HTTPException(status_code=403, detail='Already Exists')
        return obj.__dict__


@router.get('/course/{course_id}', response_model=pd.Course)
async def get_course(course_id: int, params: pd.GetCourse = Depends()):
    with service_session() as session:
        obj = session.query(models.Course).filter(models.Course.id == course_id).first()

        return pd.Course(**obj.__dict__)


@router.get('/course/{course_id}/students')
async def get_course_students(course_id: int):
    with service_session() as session:
        objs = session.query(models.Student).filter(models.Student.course_id == course_id)
        return [pd.Student(**student.__dict__) for student in objs]
