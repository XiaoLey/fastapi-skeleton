from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator

from app.support.helper import format_datetime


# Shared properties
class UserBase(BaseModel):
    id: int
    username: str
    nickname: str
    gender: str
    avatar: str

    class Config:
        from_attributes = True


class UserDetail(UserBase):
    cellphone: Optional[str] = None
    email: Optional[str] = None
    email_verified_at: Optional[datetime] = None
    state: str
    created_at: datetime

    # field_validators
    _format_datetime_email_verified_at = field_validator('email_verified_at')(format_datetime)
    _format_datetime_created_at = field_validator('created_at')(format_datetime)
