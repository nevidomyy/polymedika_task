from fastapi import APIRouter, HTTPException, Depends

from app.db import models, schemas
from app.db.database import service_session

router = APIRouter()


@router.post('/course', response_model=schemas.CourseResponse)
async def create_course(course: schemas.CreateCourse) -> schemas.CourseResponse:
    """
    Create new course in database
    """
    with service_session() as session:
        try:
            obj = models.Course(**course.dict())
            session.add(obj)
            session.commit()
            session.refresh(obj)
        except Exception:
            raise HTTPException(status_code=500, detail="Failed to create course")

        return schemas.CourseResponse(**obj.__dict__)


@router.get('/course/{course_id}', response_model=schemas.CourseResponse)
async def get_course(course_id: int, params: schemas.GetCourse = Depends()) -> schemas.CourseResponse:
    """
    Get course information
    """
    with service_session() as session:
        obj = session.query(models.Course).filter(models.Course.id == course_id).first()
        return schemas.CourseResponse(**obj.__dict__)


@router.get('/course/{course_id}/students', response_model=list[schemas.StudentResponse])
async def get_course_students(course_id: int) -> list[schemas.StudentResponse]:
    """
    Get all students in a course
    """
    with service_session() as session:
        objs = session.query(models.Student).filter(models.Student.course_id == course_id)
        return [schemas.StudentResponse(**student.__dict__) for student in objs]
