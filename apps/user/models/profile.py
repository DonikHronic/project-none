import bcrypt
from sqlalchemy import Column, String, UUID, ForeignKey, Text
from sqlalchemy.orm import relationship

from apps.core.models import Status
from apps.user.models import User
from core.database import BaseModel


class Profile(BaseModel):
    """User Profiles"""

    username = Column(String(50), unique=True, nullable=False)
    password = Column(String, unique=True, nullable=True)
    first_name = Column(String(150), default="First Name", nullable=False)
    second_name = Column(String(150), default="Second Name", nullable=False)

    type_guid = Column(UUID, ForeignKey("profile_types.guid"), nullable=False)
    type = relationship("ProfileType", back_populates="profiles")
    user_guid = Column(UUID, ForeignKey("users.guid"), nullable=False)
    user = relationship(User, back_populates="profiles")
    status_guid = Column(UUID, ForeignKey("statuses.guid"), nullable=False)
    status = relationship(Status)

    @classmethod
    def make_password(cls, password: str):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))


class ProfileType(BaseModel):
    """User Profile Types"""

    code = Column(String(50), nullable=False, unique=True)
    name = Column(String(150), nullable=False)
    description = Column(Text)
