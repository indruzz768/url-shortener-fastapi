from datetime import datetime
from pydantic import BaseModel, HttpUrl, Field

class URLCreate(BaseModel):
    original_url: HttpUrl = Field(..., description="Long URL to shorten")

class URLItem(BaseModel):
    id: int
    original_url: str
    short_code: str
    clicks: int
    created_at: datetime
    class Config:
        from_attributes = True
