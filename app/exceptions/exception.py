"""
框架异常类
"""

from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_422_UNPROCESSABLE_ENTITY


class AuthenticationError(HTTPException):
    """
    未认证
    """

    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(status_code=HTTP_401_UNAUTHORIZED, detail=detail)


class AuthorizationError(HTTPException):
    """
    未授权
    """

    def __init__(self, detail: str = "Forbidden"):
        super().__init__(status_code=HTTP_403_FORBIDDEN, detail=detail)


class InvalidCellphoneError(HTTPException):
    """
    非法手机号
    """

    def __init__(self, detail: str = "Invalid cellphone"):
        super().__init__(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)
