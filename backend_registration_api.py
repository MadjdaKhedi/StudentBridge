from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import shutil
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>StudentBridge</title>
        </head>
        <body>
            <h1>Welcome to StudentBridge!</h1>
            <p>Your registration system is online 🚀</p>
        </body>
    </html>
    """

@app.get("/")
def read_root():
    return {"message": "StudentBridge backend is running!"}

# CORS for local development with React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/register")
async def register_student(
    fullName: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    dob: str = Form(...),
    nationality: str = Form(...),
    major: str = Form(...),
    studyLevel: str = Form(...),
    preferredUniversity: str = Form(...),
    passport: UploadFile = File(...),
    transcripts: UploadFile = File(...),
    degree: UploadFile = File(...),
    statement: Optional[UploadFile] = File(None)
):
    student_dir = os.path.join(UPLOAD_DIR, email.replace("@", "_"))
    os.makedirs(student_dir, exist_ok=True)

    for doc, file in {
        "passport": passport,
        "transcripts": transcripts,
        "degree": degree,
        "statement": statement,
    }.items():
        if file:
            file_path = os.path.join(student_dir, f"{doc}_{file.filename}")
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

    # Simulate DB saving
    print("Registered student:", fullName, email)
    return {"message": "Student registered successfully"}
