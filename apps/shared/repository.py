import abc

from pydantic import BaseModel
from sqlalchemy.orm import Session


class ABCRepository(abc.ABC):
    """Abstract class for all Repositories"""

    def __init__(self, session: Session) -> None:
        self.__session = session

    @abc.abstractmethod
    async def create(self, *args, **kwargs) -> BaseModel:
        raise NotImplementedError

    @abc.abstractmethod
    async def update(self, *args, **kwargs) -> BaseModel:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, *args, **kwargs) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    async def get(self, *args, **kwargs) -> BaseModel:
        raise NotImplementedError

    @abc.abstractmethod
    async def list(self, *args, **kwargs) -> list[BaseModel]:
        raise NotImplementedError
