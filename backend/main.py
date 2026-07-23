from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

employees = [
    {"id": 1, "name": "Venkatesh", "role": "DevOps Engineer"},
    {"id": 2, "name": "Rahul", "role": "Python Developer"},
    {"id": 3, "name": "Priya", "role": "React Developer"}
]

@app.get("/")
def home():
    return {"message": "FastAPI Backend Running"}

@app.get("/employees")
def get_employees():
    return employees