from sqlalchemy.orm import Session

from apps.shared.repository import ABCRepository
from apps.user import models
from apps.user.schemes.profile.profile import ProfileModel


class ProfileRepository(ABCRepository):
    """Profile model repository"""

    def __init__(self, session: Session) -> None:
        super().__init__(session)
        self.__model = models.Profile
        self.__session = session

    async def create(self, *args, **kwargs) -> ProfileModel:
        raise NotImplementedError

    async def update(self, *args, **kwargs) -> ProfileModel:
        raise NotImplementedError

    async def delete(self, *args, **kwargs) -> None:
        raise NotImplementedError

    async def get(self, *args, **kwargs) -> ProfileModel:
        raise NotImplementedError

    async def list(self, *args, **kwargs) -> list[ProfileModel]:
        raise NotImplementedError
