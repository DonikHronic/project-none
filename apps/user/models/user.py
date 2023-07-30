import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, MappedColumn

from apps.core.models.status import Status
from core.database import BaseModel


class User(BaseModel):
    """User Model"""

    email: Mapped[str] = MappedColumn(unique=True, nullable=False)
    phone: Mapped[str] = MappedColumn(unique=True, nullable=False)
    status_guid: Mapped[uuid.UUID] = MappedColumn(ForeignKey("statuses.guid"), nullable=False)
    status: Mapped[Status] = relationship()
    profiles: Mapped[list["Profile"]] = relationship(back_populates="user")  # noqa
