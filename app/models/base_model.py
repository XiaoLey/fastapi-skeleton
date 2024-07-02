import datetime

from peewee import DateTimeField, Model

from app.providers.database import db, db_mgr


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db


class BaseModelWithSoftDelete(BaseModel):
    deleted_at = DateTimeField(null=True)

    @classmethod
    async def undelete(cls):
        return await db_mgr.get(cls, cls.deleted_at.is_null(True))
