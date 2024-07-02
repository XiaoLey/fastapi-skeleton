from contextvars import ContextVar

import redis
from peewee import _ConnectionState
from peewee_async import Manager
from peewee_asyncext import PooledPostgresqlExtDatabase

from config.database import settings, redis_settings

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(_ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()


db = PooledPostgresqlExtDatabase(
    settings.POSTGRES_DB,
    user=settings.POSTGRES_USER,
    host=settings.POSTGRES_HOST,
    password=settings.POSTGRES_PASSWORD,
    port=settings.POSTGRES_PORT,
    max_connections=20,    # 最大连接数，根据需要调整
)
db._state = PeeweeConnectionState()

db_mgr = Manager(db)

# redis
redis_pool = redis.ConnectionPool(
    host=redis_settings.REDIS_HOST,
    port=redis_settings.REDIS_PORT,
    db=redis_settings.REDIS_DB,
    password=redis_settings.REDIS_PASSWORD,
    decode_responses=True
)
redis_client = redis.Redis(connection_pool=redis_pool)
