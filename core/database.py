import os
import uuid
from datetime import datetime
from functools import lru_cache
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declared_attr,
    declarative_base,
    Mapped,
    MappedColumn,
    scoped_session,
    sessionmaker,
)

from core.config import settings
from core.utils import generate_tablename

sqlalchemy_database_url = f"postgresql://{settings.PG_USER}:{settings.PG_PASSWORD}@{settings.PG_HOST}:{settings.PG_PORT}/{settings.PG_DB}"  # noqa

engine = create_engine(sqlalchemy_database_url, pool_pre_ping=True)


@lru_cache()
def create_session() -> scoped_session:
    session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    return session


def get_session() -> Generator[scoped_session, None, None]:
    session = create_session()
    try:
        yield session
    finally:
        session.remove()


def import_models():
    apps_list = settings.APPS if settings.APPS else []
    apps_dir = os.path.join(settings.PROJECT_DIR, "apps")

    for app in os.listdir(apps_dir):
        if app.startswith("__"):
            continue
        if app not in apps_list:
            continue

        try:
            __import__("apps." + app + ".models")
        except ModuleNotFoundError as e:
            raise e


class Model(object):
    """Base Model for all database models"""

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return generate_tablename(cls.__name__)

    __table_args__: dict = {}

    id: Mapped[int] = MappedColumn(primary_key=True, autoincrement=True)
    guid: Mapped[uuid.UUID] = MappedColumn(unique=True, default=uuid.uuid4())
    created: Mapped[datetime] = MappedColumn(nullable=False, default=datetime.now())
    updated: Mapped[datetime] = MappedColumn(nullable=False, default=datetime.now(), onupdate=datetime.now())

    def __str__(self):
        return f"{self.__class__.__name__} object with id {self.id}"

    def __repr__(self):
        return f"{self.__class__.__name__} object with id {self.id}"

    @classmethod
    def fields(cls):
        pass


BaseModel = declarative_base(cls=Model)
