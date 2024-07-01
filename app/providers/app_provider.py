from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.config import settings


def register(app: FastAPI):
    app.debug = settings.DEBUG
    app.title = settings.NAME

    add_global_middleware(app)


def add_global_middleware(app: FastAPI):
    """
    注册全局中间件
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
