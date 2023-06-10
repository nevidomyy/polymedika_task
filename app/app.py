from fastapi import FastAPI
from app.config.settings import APP_NAME, API_VERSION
from app.routers import students, teachers, courses, grades


app = FastAPI(title=APP_NAME, version=API_VERSION, redoc_url='', docs_url='/docs')

app.include_router(students.router, tags=["Students"])
app.include_router(teachers.router, tags=["Teachers"])
app.include_router(courses.router, tags=["Courses"])
app.include_router(grades.router, tags=["Grades"])
