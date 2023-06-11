from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import IntegrityError

from app.db import models, pydantic_models as pd
from app.db.database import service_session

router = APIRouter()


@router.post('/students')
async def create_student(student: pd.Student):
    with service_session() as session:
        try:
            obj = models.Student(**student.dict())
            session.add(obj)
            session.commit()
            session.refresh(obj)
            return obj.__dict__
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Invalid foreign key value.")


@router.get('/students/{student_id}', response_model=pd.Student)
async def get_student(student_id: int, param: pd.StudentId = Depends()) -> pd.Student:
    with service_session() as session:
        obj = session.query(models.Student).filter(models.Student.id == student_id).first()
        return pd.Student(**obj.__dict__)


@router.put('/students/{student_id}', response_model=pd.Student)
async def update_student(student_id: int, data: pd.Student, param: pd.StudentId = Depends()) -> pd.Student:
    with service_session() as session:
        obj = session.query(models.Student).filter(models.Student.id == student_id).first()
        try:
            for field, value in data.dict().items():
                setattr(obj, field, value)
            session.commit()
            session.refresh(obj)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Invalid foreign key value.")

        return pd.Student(**obj.__dict__)


@router.delete('/students/{student_id}')
async def delete_student(student_id: int, param: pd.StudentId = Depends()):
    with service_session() as session:
        student = session.query(models.Student).filter(models.Student.id == student_id).first()
        session.delete(student)
        session.commit()
        raise HTTPException(status_code=204)
