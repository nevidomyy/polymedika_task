from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import IntegrityError

from app.db import models, pydantic_models as pd
from app.db.database import service_session

router = APIRouter()


@router.post('/course', response_model=pd.CourseResponse)
async def create_course(course: pd.CreateCourse) -> pd.CourseResponse:
    with service_session() as session:
        try:
            obj = models.Course(**course.dict())
            session.add(obj)
            session.commit()
            session.refresh(obj)
        except Exception:
            raise HTTPException(status_code=500, detail="Failed to create course")

        return pd.CourseResponse(**obj.__dict__)


@router.get('/course/{course_id}', response_model=pd.CourseResponse)
async def get_course(course_id: int, params: pd.GetCourse = Depends()) -> pd.CourseResponse:
    with service_session() as session:
        obj = session.query(models.Course).filter(models.Course.id == course_id).first()
        return pd.CourseResponse(**obj.__dict__)


@router.get('/course/{course_id}/students', response_model=list[pd.StudentResponse])
async def get_course_students(course_id: int) -> list[pd.StudentResponse]:
    with service_session() as session:
        objs = session.query(models.Student).filter(models.Student.course_id == course_id)
        return [pd.StudentResponse(**student.__dict__) for student in objs]
