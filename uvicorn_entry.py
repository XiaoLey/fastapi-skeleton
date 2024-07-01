import uvicorn
from config.config import settings


if __name__ == "__main__":
    uvicorn.run(app="main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT, headers=[("server", settings.NAME)])
