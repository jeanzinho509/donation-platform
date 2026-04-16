from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
from app.core.database import Base
from datetime import datetime

class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    receipt_id = Column(String, unique=True, index=True, nullable=True) # for traceability
    receipt_hash = Column(String, nullable=True)
