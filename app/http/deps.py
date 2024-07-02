from contextlib import asynccontextmanager
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.exceptions.exception import AuthenticationError
from app.models.user import User
from app.providers import database
from app.providers.database import db_mgr, reset_db_state
from app.services.auth import jwt_helper
from jose import jwt
from config.config import settings as config_settings

oauth2_token_schema = OAuth2PasswordBearer(
    tokenUrl=f"{config_settings.API_PREFIX[1:]}/auth/token/form",
)


async def get_auth_user(
        token: str = Depends(oauth2_token_schema)
) -> User:
    try:
        payload = jwt_helper.get_payload_by_token(token)
    except jwt.ExpiredSignatureError:
        raise AuthenticationError(message="Token Expired")
    except (jwt.JWTError, jwt.JWTClaimsError):
        raise AuthenticationError(message="Could not validate credentials")

    user_id = payload.get('sub')
    user = await db_mgr.get_or_none(User, User.id == user_id)

    if not user:
        raise AuthenticationError(message="User not found")
    if not user.is_enabled():
        raise AuthenticationError(message='Inactive user')
    return user


async def get_db(db_state=Depends(reset_db_state)):
    try:
        await database.db_mgr.connect()
        yield
    finally:
        await database.db_mgr.close()
