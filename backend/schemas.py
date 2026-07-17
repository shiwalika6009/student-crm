from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class StudentCreate(BaseModel):
    name: str
    roll_no: str
    grade: str
    marks: int

class StudentOut(StudentCreate):
    id: int
    class Config:
        orm_mode = True