from fastapi import FastAPI
from app.database import engine
from app.models import student
from app.routers import student as student_router

app = FastAPI()

student.Base.metadata.create_all(bind=engine)

app.include_router(student_router.router)

@app.get("/")
def root():
    return {"message": "Student API is running"}


