from typing import List
from fastapi import APIRouter

from app.db import models, schemas
from app.db.database import service_session

router = APIRouter()


@router.get('/teachers', response_model=List[schemas.ProfessorResponse])
async def get_teachers():
    with service_session() as session:
        objs = session.query(models.Professor).all()
        return [schemas.ProfessorResponse(**professor.__dict__) for professor in objs]
