from peewee import CharField, DateTimeField, IntegerField

from app.models.base_model import BaseModel


class User(BaseModel):
    id = IntegerField(primary_key=True)
    username = CharField(unique=True)
    password = CharField()
    cellphone = CharField(unique=True)
    email = CharField(unique=True)
    email_verified_at = DateTimeField(null=True)
    state = CharField(default='enabled')
    nickname = CharField()
    gender = CharField(default='unknown')
    avatar = CharField()

    class Meta:
        table_name = 'users'

    def is_enabled(self):
        return self.state == 'enabled'
