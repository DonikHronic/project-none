import uuid

from pydantic import BaseModel

from apps.shared.scheme import BaseScheme


class UserModel(BaseScheme):
    email: str
    phone: str
    status_guid: uuid.UUID


class UserCreateData(BaseModel):
    email: str
    phone: str


class UserUpdateData(BaseModel):
    email: str
    phone: str
