from fastapi.exception_handlers import request_validation_exception_handler, http_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI

from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi import Request


def register(app: FastAPI):

    # Example
    # @app.exception_handler(TestException)
    # async def authentication_exception_handler(request: Request, e: TestException):
    #     """
    #     测试异常
    #     """
    #     return JSONResponse(status_code=HTTP_400_BAD_REQUEST, content={"message": e.message})

    @app.exception_handler(StarletteHTTPException)
    async def custom_http_exception_handler(request: Request, exc):
        return await http_exception_handler(request, exc)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc):
        return await request_validation_exception_handler(request, exc)
