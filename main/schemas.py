from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import datetime

class RecoveryRequestSchema(BaseModel):
    name: constr(max_length=100)
    email: EmailStr
    wallet_address: str
    crypto_type: str
    issue_description: str
    status: Optional[str] = "Pending"
    created_at: Optional[datetime] = None

class ContactSchema(BaseModel):
    name: constr(max_length=100)
    email: EmailStr
    phone: Optional[str] = None
    country: Optional[str] = None
    type_of_recovery: str
    message: str
    privacy_policy: bool
    created_at: Optional[datetime] = None
