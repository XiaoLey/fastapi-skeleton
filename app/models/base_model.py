import datetime

from peewee import CharField, DateTimeField, Model, SQL

from app.providers.database import db, objects


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())

    _async_wrapper = None  # For async manager

    @classmethod
    def async_(cls):
        if cls._async_wrapper is None:
            class AsyncWrapper:
                def __init__(self, model_class):
                    self.model_class = model_class

                def __getattr__(self, name):
                    async_method = getattr(objects, name)

                    def wrapper(*args, **kwargs):
                        return async_method(self.model_class, *args, **kwargs)
                    return wrapper

            cls._async_wrapper = AsyncWrapper(cls)
        return cls._async_wrapper

    class Meta:
        database = db


class BaseModelWithSoftDelete(BaseModel):
    deleted_at = DateTimeField(null=True)

    @classmethod
    def undelete(cls):
        return cls.select().where(SQL("deleted_at is NULL"))
