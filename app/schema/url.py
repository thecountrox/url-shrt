from pydantic import BaseModel, Field
from datetime import datetime


class URLBase(BaseModel):
    target_url: str = Field(..., description="Full target URL")


class URL(URLBase):
    id: int
    short_code: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
