from fastapi import APIRouter, Depends

from app.http.deps import get_db
from app.models.user import User
from app.providers.database import db_mgr, redis_client
from app.schemas.user import UserDetail
from app.services.auth import hashing

router = APIRouter(
    prefix="/demo"
)


@router.get("/")
async def index():
    return "demo index"


@router.get("/db_test", response_model=UserDetail, dependencies=[Depends(get_db)])
async def db_test():
    password = hashing.get_password_hash("123456")
    user = await db_mgr.create(User, username='fake_user_by_db_test_2', password=password)
    return user


@router.get("/redis_test")
def redis_test():
    redis_client.incr('fastapi:test')
    return {'value': redis_client.get('fastapi:test')}


@router.get("/{demo_id}")
async def show(demo_id: str):
    return {"demo_id": demo_id}
