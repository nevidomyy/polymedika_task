from fastapi import HTTPException
from pydantic import field_validator, BaseModel

from app.db import models
from app.db.database import service_session


class Student(BaseModel):
    first_name: str
    last_name: str
    address: str
    phone: str
    course_id: int
    group_id: int
    faculty_id: int


class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: str
    phone: str
    course_id: int
    group_id: int
    faculty_id: int


class StudentId(BaseModel):
    student_id: int

    @field_validator('student_id')
    def validate_student(cls, value: int) -> int:
        with service_session() as session:
            if not session.query(models.Student).filter(models.Student.id == value).first():
                raise HTTPException(status_code=404, detail=f'Student with id {value} does not exist')
        return value


class ProfessorResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    branch_id: int


class GetCourse(BaseModel):
    course_id: int

    @field_validator('course_id')
    def validate_course_exist(cls, value: int) -> int:
        with service_session() as session:
            if not session.query(models.Course).filter(models.Course.id == value).first():
                raise HTTPException(status_code=404, detail=f'Course with id {value} not found')
            return value


class CreateCourse(BaseModel):
    course: str

    @field_validator('course')
    def validate_course_exist(cls, value):
        with service_session() as session:
            if session.query(models.Course).filter(models.Course.course == value).first():
                raise HTTPException(status_code=409, detail='Already Exists')
            return value


class CourseResponse(BaseModel):
    id: int
    course: str


class GradeResponse(BaseModel):
    id: int
    score: int


class CreateGrade(BaseModel):
    student_id: int
    course_id: int
    exam_id: int
    score: int

    @field_validator('score')
    def validate_score(cls, score):
        if score < 1 or score > 5:
            raise ValueError('The score must be between 1 and 5')
        return score

    @field_validator('student_id')
    def validate_student_id(cls, value):
        with service_session() as session:
            if not session.query(models.Student).filter(models.Student.id == value).first():
                raise HTTPException(status_code=404, detail=f"Student with id {value} doesn't exist")
        return value

    @field_validator('course_id')
    def validate_course_id(cls, value):
        with service_session() as session:
            if not session.query(models.Course).filter(models.Course.id == value).first():
                raise HTTPException(status_code=404, detail=f"Course with id {value} doesn't exist")
        return value

    @field_validator('exam_id')
    def validate_exam_id(cls, value, values):
        with service_session() as session:
            if not session.query(models.Exam).join(models.AcademicPlan).filter(
                    models.AcademicPlan.course_id == values.get('course_id'),
                    models.Exam.id == value).first():
                raise HTTPException(status_code=404, detail=f"Exam with id {value} not found for the course")
        return value

    @field_validator('score')
    def validate_existing_score(cls, value, values):
        with service_session() as session:
            if session.query(models.Grades).filter(models.Grades.student_id == values.get('student_id'),
                                                   models.Grades.exam_id == values.get('exam_id')).first():
                raise HTTPException(status_code=409, detail="Score for this exam already exists")
        return value


class UpdateGrade(BaseModel):
    grade_id: int
    score: int

    @field_validator('score')
    def validate_score(cls, score):
        if score < 1 or score > 5:
            raise ValueError('The score must be between 1 and 5')
        return score

    @field_validator('grade_id')
    def validate_grade_id(cls, value):
        with service_session() as session:
            if not session.query(models.Grades).filter(models.Grades.id == value).first():
                raise HTTPException(status_code=404, detail=f"Grade with id {value} does not exist")
        return value
