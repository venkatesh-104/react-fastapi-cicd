from fastapi import FastAPI

app = FastAPI()

employees = [
    {"id": 1, "name": "Venkatesh", "role": "DevOps Engineer"},
    {"id": 2, "name": "Rahul", "role": "Python Developer"},
    {"id": 3, "name": "Priya", "role": "React Developer"},
]


@app.get("/")
def home():
    return {"message": "FastAPI Backend Running"}


@app.get("/employees")
def get_employees():
    return employees 