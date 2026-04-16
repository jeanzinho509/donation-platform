import hashlib
import uuid
from datetime import datetime

def generate_receipt():
    receipt_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()
    raw_data = f"{receipt_id}-{timestamp}"
    receipt_hash = hashlib.sha256(raw_data.encode()).hexdigest()
    return receipt_id, receipt_hash
