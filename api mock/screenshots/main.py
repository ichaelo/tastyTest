from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from schema import Question, Answer, Test, Student, Teacher, Testing, TestingResult, TestingAnswer

app = FastAPI()

# Заглушки
tests = [
    Test(
        id=1,
        subject="Math",
        topic="Algebra",
        questions=[Question(question="What is 2 + 2?"), Question(question="What is 5 * 3?")],
        answer_options=[
            [Answer(answer="3", is_correct=False), Answer(answer="4", is_correct=True)],
            [Answer(answer="10", is_correct=False), Answer(answer="15", is_correct=True)],
        ],
        correct_answers=[2, 2],
    )
]

teachers = [
    Teacher(id=1, name="John Doe"),
    Teacher(id=2, name="Jane Smith"),
]

students = [
    Student(id=1, name="Alice"),
    Student(id=2, name="Bob"),
]

testings = [
    Testing(
        id=1,
        test_id=1,
        start_date=datetime(2023, 5, 1, 10, 0),
        end_date=datetime(2023, 5, 1, 11, 0),
        students=[Student(id=1, name="Alice"), Student(id=2, name="Bob")],
        teacher=Teacher(id=1, name="John Doe"),
    )
]

testing_results = [
    TestingResult(id=1, testing_id=1, student_id=1, answers=[2, 2]),
    TestingResult(id=2, testing_id=1, student_id=2, answers=[1, 2]),
]

# Получить список тестов
@app.get("/api/v1/tests")
def get_tests():
    return tests

# Создать тест
@app.post("/api/v1/tests")
def create_test(test: Test):
    test.id = len(tests) + 1
    tests.append(test)
    return test

@app.put("/api/v1/tests/{test_id}")
def update_test(test_id: int, test: Test):
    for i, t in enumerate(tests):
        if t.id == test_id:
            tests[i] = test
            return test
    raise HTTPException(status_code=404, detail="Test not found")

# Удалить тест
@app.delete("/api/v1/tests/{test_id}")
def delete_test(test_id: int):
    for i, test in enumerate(tests):
        if test.id == test_id:
            tests.pop(i)
            return {"message": "Test deleted successfully"}
    raise HTTPException(status_code=404, detail="Test not found")

# Получить определенный тест
@app.get("/api/v1/tests/{test_id}")
def get_test(test_id: int):
    for test in tests:
        if test.id == test_id:
            return test
    raise HTTPException(status_code=404, detail="Test not found")

# Создать преподавателя
@app.post("/api/v1/teachers")
def create_teacher(teacher: Teacher):
    teacher.id = len(teachers) + 1
    teachers.append(teacher)
    return teacher

# Получить преподавателей
@app.get("/api/v1/teachers")
def get_teachers():
    return teachers

# Получить преподавателя
@app.get("/api/v1/teachers/{teacher_id}")
def get_teacher(teacher_id: int):
    for teacher in teachers:
        if teacher.id == teacher_id:
            return teacher
    raise HTTPException(status_code=404, detail="Teacher not found")

# Изменить преподавателя
@app.put("/api/v1/teachers/{teacher_id}")
def update_teacher(teacher_id: int, teacher: Teacher):
    for i, t in enumerate(teachers):
        if t.id == teacher_id:
            teachers[i] = teacher
            return teacher
    raise HTTPException(status_code=404, detail="Teacher not found")

# Удалить преподавателя
@app.delete("/api/v1/teachers/{teacher_id}")
def delete_teacher(teacher_id: int):
    for i, teacher in enumerate(teachers):
        if teacher.id == teacher_id:
            teachers.pop(i)
            return {"message": "Teacher deleted successfully"}
    raise HTTPException(status_code=404, detail="Teacher not found")

# Создать студента
@app.post("/api/v1/students")
def create_student(student: Student):
    student.id = len(students) + 1
    students.append(student)
    return student

# Получить студентов
@app.get("/api/v1/students")
def get_students():
    return students

# Получить студента
@app.get("/api/v1/students/{student_id}")
def get_student(student_id: Optional[int] = None):
    if student_id:
        for student in students:
            if student.id == student_id:
                return student
        raise HTTPException(status_code=404, detail="Student not found")
    return students

# Изменить студента
@app.put("/api/v1/students/{student_id}")
def update_student(student_id: int, student: Student):
    for i, s in enumerate(students):
        if s.id == student_id:
            students[i] = student
            return student
    raise HTTPException(status_code=404, detail="Student not found")

# Удалить студента
@app.delete("/api/v1/students/{student_id}")
def delete_student(student_id: int):
    for i, student in enumerate(students):
        if student.id == student_id:
            students.pop(i)
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")

# Получить тестирования
@app.get("/api/v1/testings")
def get_tests():
    return testings

# Получить тестирование
@app.get("/api/v1/testings/{testing_id}")
def get_testing(testing_id: int):
    for testing in testings:
        if testing.id == testing_id:
            return testing
    raise HTTPException(status_code=404, detail="Testing not found")

# Создать тестирование
@app.post("/api/v1/testings")
def create_testing(testing: Testing):
    testing.id = len(testings) + 1
    testings.append(testing)
    return testing

# Изменить тестирование
@app.put("/api/v1/testing/{testing_id}")
def update_testing(testing_id: int, testing: Testing):
    for i, s in enumerate(testings):
        if s.id == testing_id:
            testings[i] = testing
            return testing
    raise HTTPException(status_code=404, detail="Testing not found")
# Удалить тестирование
@app.delete("/api/v1/testing/{testing_id}")
def delete_testing(testing_id: int):
    for i, testing in enumerate(testings):
        if testing.id == testing_id:
            testings.pop(i)
            return {"message": "Testing deleted successfully"}
    raise HTTPException(status_code=404, detail="Testing not found")

# Создать запись ответа пользователя на вопрос
@app.post("/api/v1/testings/{testing_id}/questions/{question_id}/answers")
def create_testing_answer(testing_id: int, question_id: int, answer: TestingAnswer):
    for testing in testings:
        if testing.id == testing_id:
            for test in tests:
                if test.id == testing.test_id:
                    for i, question in enumerate(test.questions):
                        if i == question_id:
                            for option in test.answer_options[i]:
                                if option.id == answer.answer_id:
                                    # Сохранить ответ пользователя
                                    return {"message": "Answer saved successfully"}
                    raise HTTPException(status_code=404, detail="Question not found")
            raise HTTPException(status_code=404, detail="Test not found")
    raise HTTPException(status_code=404, detail="Testing not found")

# Изменить ответ пользователя на вопрос
@app.put("/api/v1/testings/{testing_id}/questions/{question_id}/answers")
def update_testing_answer(testing_id: int, question_id: int, answer: TestingAnswer):
    for testing in testings:
        if testing.id == testing_id:
            for test in tests:
                if test.id == testing.test_id:
                    for i, question in enumerate(test.questions):
                        if i == question_id:
                            for option in test.answer_options[i]:
                                if option.id == answer.answer_id:
                                    # todo: Обновить ответ пользователя
                                    return {"message": "Answer updated successfully"}

                    raise HTTPException(status_code=404, detail="Question not found")
            raise HTTPException(status_code=404, detail="Test not found")
    raise HTTPException(status_code=404, detail="Testing not found")

# Получить ответы пользователя на вопросы
@app.get("/api/v1/testings/{testing_id}/answers")
def get_user_answers(testing_id: int):
    for result in testing_results:
        if result.testing_id == testing_id:
            return result.answers
    raise HTTPException(status_code=404, detail="Testing not found")

# Получить результаты тестирования пользователя
@app.get("/api/v1/testings/{testing_id}/results")
def get_testing_results(testing_id: int):
    results = []
    for result in testing_results:
        if result.testing_id == testing_id:
            test = next((t for t in tests if t.id == result.testing_id), None)
            if test:
                correct_answers = len([a for a, c in zip(result.answers, test.correct_answers) if a == c])
                max_score = len(test.correct_answers)
                results.append({"student_id": result.student_id, "score": correct_answers, "max_score": max_score})
            else:
                raise HTTPException(status_code=404, detail="Test not found")
    if not results:
        raise HTTPException(status_code=404, detail="Testing not found")
    return results