from sqlalchemy import Column, String, Integer, ForeignKey, UUID
from sqlalchemy.orm import relationship

from apps.core.models.status import Status
from core.database import BaseModel


class User(BaseModel):
    """User Model"""

    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    status_guid = Column(UUID, ForeignKey("statuses.guid"), nullable=False)
    status = relationship(Status, back_populates="users")
