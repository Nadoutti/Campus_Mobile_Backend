from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.teacher_routes import router as teacher_router
from routes.student_routes import router as student_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# Register the teacher and student router
app.include_router(teacher_router)
app.include_router(student_router)

