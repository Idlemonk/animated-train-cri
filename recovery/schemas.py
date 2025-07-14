from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from decimal import Decimal
from datetime import datetime

class RecoveryRequestSchema(BaseModel):
    name: constr(max_length=100)
    email: EmailStr
    wallet_address: str
    crypto_type: str
    issue_description: str
    status: Optional[str] = "Pending"
    created_at: Optional[datetime] = None

class WalletRecoverySchema(BaseModel):
    email: EmailStr
    wallet_name: str
    recovery_status: Optional[str] = "Pending"
    created_at: Optional[datetime] = None

class BlockchainTransactionSchema(BaseModel):
    transaction_id: str
    sender_address: str
    receiver_address: str
    amount: Decimal
    timestamp: datetime

class ContactSchema(BaseModel):
    name: constr(max_length=100)
    email: EmailStr
    phone: Optional[str] = None
    country: Optional[str] = None
    type_of_recovery: str
    message: str
    privacy_policy: bool
    created_at: Optional[datetime] = None
