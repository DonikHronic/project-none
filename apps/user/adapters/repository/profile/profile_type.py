from sqlalchemy.orm import Session

from apps.shared.repository import ABCRepository
from apps.user import models
from apps.user.schemes.profile.profile_type import ProfileTypeModel


class ProfileTypeRepository(ABCRepository):
    """Profile types model Repository"""

    def __init__(self, session: Session):
        super().__init__(session)
        self.__model = models.ProfileType
        self.__session = session

    async def create(self, *args, **kwargs) -> ProfileTypeModel:
        raise NotImplementedError

    async def update(self, *args, **kwargs) -> ProfileTypeModel:
        raise NotImplementedError

    async def delete(self, *args, **kwargs) -> None:
        raise NotImplementedError

    async def get(self, *args, **kwargs) -> ProfileTypeModel:
        raise NotImplementedError

    async def list(self, *args, **kwargs) -> list[ProfileTypeModel]:
        raise NotImplementedError
