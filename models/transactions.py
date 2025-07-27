from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal


class Transaction(BaseModel):
    id: str
    source: str  # 'upbank' or 'qif'
    date: date
    description: str
    amount: Decimal
    currency: str = "AUD"
    category: Optional[str] = None
    account: Optional[str] = None
