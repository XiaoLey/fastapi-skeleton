-- 创建性别枚举类型
SELECT create_enum_type_if_not_exists('gender', 'male', 'female', 'unknown');

-- 创建用户表users
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,                                      -- 自增ID
  username VARCHAR(255) NOT NULL UNIQUE,                      -- 用户名
  password VARCHAR(255) NOT NULL DEFAULT '',                  -- 密码
  cellphone VARCHAR(45) UNIQUE,                               -- 手机
  email VARCHAR(255) UNIQUE,                                  -- 邮箱
  email_verified_at TIMESTAMP,                                -- 邮箱验证时间
  state VARCHAR(50) NOT NULL DEFAULT 'enabled',               -- 状态
  nickname VARCHAR(255) NOT NULL DEFAULT '',                  -- 昵称
  gender gender NOT NULL DEFAULT 'unknown',                   -- 性别
  avatar VARCHAR(255) NOT NULL DEFAULT '',                    -- 头像
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,  -- 创建时间
  updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP   -- 更新时间
);

-- 添加列注释
COMMENT ON COLUMN users.username Is '用户名';
COMMENT ON COLUMN users.password IS '密码';
COMMENT ON COLUMN users.cellphone IS '手机';
COMMENT ON COLUMN users.email IS '邮箱';
COMMENT ON COLUMN users.email_verified_at IS '邮箱验证时间';
COMMENT ON COLUMN users.state IS '状态 enabled disabled';
COMMENT ON COLUMN users.nickname IS '昵称';
COMMENT ON COLUMN users.gender IS '性别 male，female';
COMMENT ON COLUMN users.avatar IS '头像';
COMMENT ON COLUMN users.created_at IS '创建时间';
COMMENT ON COLUMN users.updated_at IS '更新时间';
