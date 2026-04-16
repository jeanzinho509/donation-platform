from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.donation import Donation
from app.models.project import Project
from app.schemas import DonationCreate, DonationResponse
from app.utils.auth import get_current_user_id
from app.utils.receipts import generate_receipt

router = APIRouter(prefix="/donations", tags=["donations"])

@router.post("/", response_model=DonationResponse)
def create_donation(
    donation: DonationCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    project = db.query(Project).filter(Project.id == donation.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    receipt_id, receipt_hash = generate_receipt()

    new_donation = Donation(
        user_id=user_id,
        project_id=donation.project_id,
        amount=donation.amount,
        receipt_id=receipt_id,
        receipt_hash=receipt_hash
    )

    project.raised_amount += donation.amount

    db.add(new_donation)
    db.commit()
    db.refresh(new_donation)

    return new_donation
