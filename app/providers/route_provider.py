from routes.api import api_router
from config.config import settings


def boot(app):
    # 注册api路由[routes/api.py]
    app.include_router(api_router, prefix=settings.API_PREFIX)

    # 打印路由
    if app.debug:
        for route in app.routes:
            print({'path': route.path, 'name': route.name, 'methods': route.methods})
