import uuid
from typing import Optional

import bcrypt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, MappedColumn

from apps.core.models import Status
from core.database import BaseModel
from .user import User


class Profile(BaseModel):
    """User Profiles"""

    username: Mapped[str] = MappedColumn(unique=True, nullable=False)
    password: Mapped[str] = MappedColumn(unique=True, nullable=True)
    first_name: Mapped[str] = MappedColumn(default="First Name", nullable=False)
    second_name: Mapped[str] = MappedColumn(default="Second Name", nullable=False)

    type_guid: Mapped[uuid.UUID] = MappedColumn(ForeignKey("profile_types.guid"), nullable=False)
    type: Mapped["ProfileType"] = relationship(back_populates="profiles")
    user_guid: Mapped[uuid.UUID] = MappedColumn(ForeignKey("users.guid"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="profiles")
    status_guid: Mapped[uuid.UUID] = MappedColumn(ForeignKey("statuses.guid"), nullable=False)
    status: Mapped[Status] = relationship(back_populates="profiles")

    @classmethod
    def make_password(cls, password: str):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))


class ProfileType(BaseModel):
    """User Profile Types"""

    code: Mapped[str] = MappedColumn(nullable=False, unique=True)
    name: Mapped[str] = MappedColumn(nullable=False)
    description: Mapped[Optional[str]]
