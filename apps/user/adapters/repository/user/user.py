import uuid

from sqlalchemy.orm import Session

from apps.shared.repository import ABCRepository
from apps.user import models
from apps.user.schemes.user import UserModel, UserCreateData, UserUpdateData


class UserRepository(ABCRepository):
    """User models repository"""

    def __init__(self, session: Session):
        super().__init__(session)
        self.__model = models.User
        self.__session = session

    async def create(self, data: UserCreateData) -> UserModel:
        raise NotImplementedError

    async def update(self, data: UserUpdateData) -> UserModel:
        raise NotImplementedError

    async def delete(self, guid: uuid.UUID) -> None:
        raise NotImplementedError

    async def get(self, guid: uuid.UUID) -> UserModel:
        raise NotImplementedError

    async def list(self) -> list[UserModel]:
        raise NotImplementedError
