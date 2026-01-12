from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate
from fastapi import HTTPException

def create_student(db: Session, student: StudentCreate):
    if get_student_by_email(db, student.email):
        raise HTTPException(status_code=400,detail="Email already registered")
    
    
    db_student = Student(
        name=student.name,
        email=student.email,
        password=student.password
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student_by_email(db: Session, email: str):
    return db.query(Student).filter(Student.email == email).first()