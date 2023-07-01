from sqlalchemy import Column, Text, String, ForeignKey, UUID
from sqlalchemy.orm import relationship

from core.database import BaseModel


class Status(BaseModel):
    """Statuses"""

    code = Column(String(50), unique=True, nullable=False)
    type_guid = Column(UUID, ForeignKey("status_types.guid"), nullable=False)
    type = relationship("StatusType", back_populates="statuses")
    name = Column(String(150), nullable=False)
    description = Column(Text)


class StatusType(BaseModel):
    """Status Types"""

    code = Column(String(50), unique=True, nullable=False)
    name = Column(String(150), nullable=False)
    description = Column(Text)
