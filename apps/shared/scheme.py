import datetime
import uuid

from pydantic import BaseModel


class BaseScheme(BaseModel):
    id: int
    guid: uuid.UUID
    created: datetime.datetime
    updated: datetime.datetime

    class Config:
        orm_mode = True
