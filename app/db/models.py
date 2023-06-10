from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, autoincrement=True)
    course = Column(String, unique=True, nullable=False)


class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)


class Branch(Base):
    __tablename__ = 'branch'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)


class Build(Base):
    __tablename__ = 'build'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    address = Column(String, nullable=False, unique=True)
    number = Column(Integer, nullable=False, unique=True)


class Semester(Base):
    __tablename__ = 'semester'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=False, nullable=False)


class Exam(Base):
    __tablename__ = 'exam'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)


class SelfWork(Base):
    __tablename__ = 'self_work'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False)
    topic = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)


class Faculty(Base):
    __tablename__ = 'faculty'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    branch_id = Column(ForeignKey('branch.id'), nullable=False)


class Auditorium(Base):
    __tablename__ = 'auditorium'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, nullable=False, unique=True)
    build_id = Column(ForeignKey('build.id'), nullable=False)


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    course_id = Column(ForeignKey('course.id'), nullable=False)
    group_id = Column(ForeignKey('group.id'), nullable=False)
    faculty_id = Column(ForeignKey('faculty.id'), nullable=False)


class Professor(Base):
    __tablename__ = 'professor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    branch_id = Column(ForeignKey('branch.id'), nullable=False)


class Grades(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(ForeignKey('student.id', ondelete='CASCADE'), nullable=False)
    exam_id = Column(ForeignKey('exam.id'), nullable=False)
    score = Column(Integer, nullable=False)


class CourseProgram(Base):
    __tablename__ = 'course_program'

    id = Column(Integer, primary_key=True, autoincrement=True)
    faculty_id = Column(ForeignKey('faculty.id'), nullable=False)
    course_id = Column(ForeignKey('course.id'), nullable=False)
    description = Column(Text, nullable=False)


class Schedule(Base):
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime, nullable=False)
    build_id = Column(ForeignKey('build.id'), nullable=False)
    group_id = Column(ForeignKey('group.id'), nullable=False)
    professor_id = Column(ForeignKey('professor.id'), nullable=False)
    auditorium_id = Column(ForeignKey('auditorium.id'), nullable=False)
    subject = Column(String, nullable=False)


class AcademicPlan(Base):
    __tablename__ = 'academic_plan'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False)
    exam_id = Column(ForeignKey('exam.id'), nullable=True)
    self_work_id = Column(ForeignKey('self_work.id', ondelete='SET NULL'), nullable=True)
    course_id = Column(ForeignKey('course.id'), nullable=False)
    semester_id = Column(ForeignKey('semester.id'), nullable=False)
    professor_id = Column(ForeignKey('professor.id'), nullable=False)
    subject = Column(String, nullable=False)
