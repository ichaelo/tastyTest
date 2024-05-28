from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal, get_db
from models import Base, Teacher, Student, Test, Testing, TestingResult
from schema import TeacherCreate, StudentCreate, TestCreate, TestingCreate, TestingResultCreate
app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Hello, World!"}

# GET

@app.get("/api/v1/teachers/")
def get_teachers(db: Session = Depends(get_db)):
    teachers = db.query(Teacher).all()
    return teachers

@app.get("/api/v1/teachers/{teacher_id}")
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail=f"No teacher with id {teacher_id}")
    return teacher

@app.get("/api/v1/students/")
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students

@app.get("/api/v1/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail=f"No teacher with id {student_id}")
    return student

@app.get("/api/v1/tests/")
def get_tests(db: Session = Depends(get_db)):
    tests = db.query(Test).all()
    return tests

@app.get("/api/v1/tests/{test_id}")
def get_test(test_id: int, db: Session = Depends(get_db)):
    test = db.query(Test).filter(Test.id == test_id).first()
    if not test:
        raise HTTPException(status_code=404, detail=f"No teacher with id {test}")
    return test

@app.get("/api/v1/testings/")
def get_testings(db: Session = Depends(get_db)):
    testings = db.query(Testing).all()
    return testings

@app.get("/api/v1/testings/{testing_id}")
def get_testing(testing_id: int, db: Session = Depends(get_db)):
    testing = db.query(Testing).filter(Testing.id == testing_id).first()
    if not testing:
        raise HTTPException(status_code=404, detail=f"No teacher with id {testing_id}")
    return testing

@app.get("/api/v1/testing-results/")
def get_testing_results(db: Session = Depends(get_db)):
    testing_results = db.query(TestingResult).all()
    return testing_results

@app.get("/api/v1/testing-results/{result_id}")
def get_testing_result(result_id: int, db: Session = Depends(get_db)):
    testing_result = db.query(TestingResult).filter(TestingResult.id == result_id).first()
    if not testing_result:
        raise HTTPException(status_code=404, detail=f"No teacher with id {result_id}")
    return testing_result


# POST

@app.post("/api/v1/teachers/")
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = Teacher(fio=teacher.fio)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

@app.post("/api/v1/students/")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(fio=student.fio)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.post("/api/v1/tests/")
def create_test(test: TestCreate, db: Session = Depends(get_db)):
    db_test = Test(subject=test.subject, topic=test.topic, questions=test.questions, answers=test.answers, correct_answers=test.correct_answers)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

@app.post("/api/v1/testings/")
def create_testing(testing: TestingCreate, db: Session = Depends(get_db)):
    db_test = db.query(Test).filter(Test.id == testing.test_id).first()
    if not db_test:
        raise HTTPException(status_code=404, detail="Test not found")
    db_testing = Testing(start_date=testing.start_date, end_date=testing.end_date, listOfStudents=testing.listOfStudents, test_id=testing.test_id)
    db.add(db_testing)
    db.commit()
    db.refresh(db_testing)
    return db_testing

@app.post("/api/v1/testing-results/")
def create_testing_result(testing_result: TestingResultCreate, db: Session = Depends(get_db)):
    db_testing = db.query(Testing).filter(Testing.id == testing_result.testing_id).first()
    db_student = db.query(Student).filter(Student.id == testing_result.student_id).first()
    if not db_testing or not db_student:
        raise HTTPException(status_code=404, detail="Testing or student not found")
    db_testing_result = TestingResult(testing_id=testing_result.testing_id, student_id=testing_result.student_id, answers=testing_result.answers)
    db.add(db_testing_result)
    db.commit()
    db.refresh(db_testing_result)
    return db_testing_result

