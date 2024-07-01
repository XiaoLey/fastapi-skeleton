import uvicorn
from config.config import settings


uvicorn.run(app="api_app:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT, headers=[("server", settings.NAME)])
