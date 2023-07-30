import uuid
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, MappedColumn

from core.database import BaseModel


class Status(BaseModel):
    """Statuses"""

    code: Mapped[str] = MappedColumn(unique=True, nullable=False)
    type_guid: Mapped[uuid.UUID] = MappedColumn(ForeignKey("status_types.guid"), nullable=False)
    type: Mapped["StatusType"] = relationship(back_populates="statuses")
    name: Mapped[str] = MappedColumn(nullable=False)
    description: Mapped[Optional[str]]


class StatusType(BaseModel):
    """Status Types"""

    code: Mapped[str] = MappedColumn(unique=True, nullable=False)
    name: Mapped[str] = MappedColumn(nullable=False)
    description: Mapped[Optional[str]]
    statuses: Mapped[list[Status]] = relationship(back_populates="type")
