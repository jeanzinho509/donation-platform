from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class ProjectCreate(BaseModel):
    title: str
    description: str
    goal_amount: float

class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    goal_amount: float
    raised_amount: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class DonationCreate(BaseModel):
    project_id: int
    amount: float

class DonationResponse(BaseModel):
    id: int
    user_id: int
    project_id: int
    amount: float
    created_at: datetime
    receipt_id: Optional[str] = None
    receipt_hash: Optional[str] = None

    class Config:
        from_attributes = True
