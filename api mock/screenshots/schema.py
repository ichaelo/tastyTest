from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class Question(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str
    is_correct: bool

class Test(BaseModel):
    id: int
    subject: str
    topic: str
    questions: List[Question]
    answer_options: List[List[Answer]]
    correct_answers: List[int]

class Student(BaseModel):
    id: int
    name: str

class Teacher(BaseModel):
    id: int
    name: str

class Testing(BaseModel):
    id: int
    test_id: int
    start_date: datetime
    end_date: datetime
    students: List[Student]
    teacher: Teacher

class TestingResult(BaseModel):
    id: int
    testing_id: int
    student_id: int
    answers: List[int]

class TestingAnswer(BaseModel):
    question_id: int
    answer_id: int