from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, text
from app.core.database import Base
from datetime import datetime

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    goal_amount = Column(Float, nullable=False)
    raised_amount = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="active") # active, funded, closed
