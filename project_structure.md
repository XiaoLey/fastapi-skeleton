```
/kaxiluo/fastapi-skeleton/
|-- app
|   |-- commands                                ----- 放置一些命令行
|   |   `-- __init__.py
|   |-- exceptions                              ----- 自定义的异常类
|   |   |-- __init__.py
|   |   `-- exception.py
|   |-- http                                    ----- http目录
|   |   |-- api                                 ----- api控制器目录
|   |   |   |-- __init__.py
|   |   |   |-- auth.py                         ----- 登录认证api的控制器
|   |   |   |-- demo.py
|   |   |   `-- users.py
|   |   |-- middleware                          ----- 放置自定义中间件
|   |   |   `-- __init__.py
|   |   |-- __init__.py
|   |   `-- deps.py                             ----- 依赖
|   |-- jobs                                    ----- 调度任务
|   |   |-- __init__.py
|   |   `-- demo_job.py
|   |-- models                                  ----- 模型目录
|   |   |-- __init__.py
|   |   |-- base_model.py                       ----- 定义模型的基类
|   |   `-- user.py
|   |-- providers                               ----- 核心服务提供者
|   |   |-- __init__.py
|   |   |-- app_provider.py                     ----- 注册应用的全局事件、中间件等
|   |   |-- database.py                         ----- 数据库连接
|   |   |-- handle_exception.py                 ----- 异常处理器
|   |   |-- logging_provider.py                 ----- 集成loguru日志系统
|   |   `-- route_provider.py                   ----- 注册路由文件routes/*
|   |-- schemas                                 ----- 数据模型，负责请求和响应资源数据的定义和格式转换
|   |   |-- __init__.py
|   |   `-- user.py
|   |-- services                                ----- 服务层，业务逻辑层
|   |   |-- auth                                ----- 认证相关服务
|   |   |   |-- __init__.py
|   |   |   |-- grant.py                        ----- 认证核心类
|   |   |   |-- hashing.py
|   |   |   |-- jwt_helper.py
|   |   |   |-- oauth2_schema.py
|   |   |   `-- random_code_verifier.py
|   |   `-- __init__.py
|   |-- support                                 ----- 公共方法
|   |   |-- __init__.py
|   |   `-- helper.py
|   `-- __init__.py
|-- bootstrap                                   ----- 启动项
|   |-- __init__.py
|   |-- application.py                          ----- 创建app实例
|   `-- scheduler.py                            ----- 创建调度器实例
|-- config                                      ----- 配置目录
|   |-- auth.py                                 ----- 认证-JWT配置
|   |-- config.py                               ----- app配置
|   |-- database.py                             ----- 数据库配置
|   `-- logging.py                              ----- 日志配置
|-- database
|   `-- migrations                              ----- 初始化SQL
|       `-- 2022_09_07_create_users_table.sql
|-- routes                                      ----- 路由目录
|   |-- __init__.py
|   `-- api.py                                  ----- api路由
|-- storage
|   `-- logs                                    ----- 日志目录
|-- README.md
|-- docker-compose.yaml
|-- main.py                                     ----- app主程序
|-- requirements.txt
|-- scheduler.py                                ----- 调度任务启动入口
|-- uvicorn_entry.py                            ----- app/api启动入口
```