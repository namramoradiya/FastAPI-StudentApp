from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.student import StudentCreate, StudentResponse
from app.crud import student as student_crud

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/register", response_model=StudentResponse)
def register_student(student: StudentCreate, db: Session = Depends(get_db)):
    return student_crud.create_student(db, student)
