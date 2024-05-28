from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel
from typing import List, Dict

#sqlalchemy

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    fio = Column(String)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    fio = Column(String)

class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    topic = Column(String)
    questions = Column(JSON)
    answers = Column(JSON)
    correct_answers = Column(JSON)

class Testing(Base):
    __tablename__ = "testings"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(String)
    end_date = Column(String)
    listOfStudents = Column(JSON)
    test_id = Column(Integer, ForeignKey("tests.id"))
    test = relationship("Test", backref="testings")

class TestingResult(Base):
    __tablename__ = "testing_results"

    id = Column(Integer, primary_key=True, index=True)
    testing_id = Column(Integer, ForeignKey("testings.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
    answers = Column(JSON)
    testing = relationship("Testing", backref="testing_results")
    student = relationship("Student", backref="testing_results")