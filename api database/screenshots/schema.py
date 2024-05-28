from pydantic import BaseModel
from typing import List, Dict

class TeacherCreate(BaseModel):
    fio: str

class StudentCreate(BaseModel):
    fio: str

class TestCreate(BaseModel):
    subject: str
    topic: str
    questions: List[str]
    answers: List[List[str]]
    correct_answers: List[int]

class TestingCreate(BaseModel):
    start_date: str
    end_date: str
    listOfStudents: List[int]
    test_id: int

class TestingResultCreate(BaseModel):
    testing_id: int
    student_id: int
    answers: List[int]
