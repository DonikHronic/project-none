from typing import Optional

from pydantic import BaseModel


class Error(BaseModel):
    error_note: Optional[str] = None
    error_code: Optional[int] = None
    error_data: Optional[dict] = None


class ResponseModel(BaseModel):
    success: bool
    error: Optional[Error] = None
    result: Optional[dict] = None


class SuccessResponseModel(ResponseModel):
    success: bool = True
    error: Optional[Error] = None
    result: Optional[dict] = None
