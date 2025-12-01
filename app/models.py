from sqlmodel import SQLModel, Field
from typing import Optional

class Email(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    subject: str
    sender: str
    region: str
    body: str
    received_at: str
