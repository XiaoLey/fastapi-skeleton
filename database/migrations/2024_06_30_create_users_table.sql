-- 创建用户表users
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL DEFAULT '',
  cellphone VARCHAR(45) UNIQUE,
  email VARCHAR(255) UNIQUE,
  email_verified_at TIMESTAMP,
  state VARCHAR(50) NOT NULL DEFAULT 'enabled',
  nickname VARCHAR(255) NOT NULL DEFAULT '',
  gender VARCHAR(10) NOT NULL DEFAULT 'unknown',
  avatar VARCHAR(255) NOT NULL DEFAULT '',
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
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

-- 插入用户，密码均为123456
INSERT INTO users (username, password, created_at, updated_at) VALUES
('fake_user1', 'ukPEqhgLpgUFNBwmRjb2+uVzAHMkbeqcUs+MmHGx5RM=', NOW(), NOW()),
('fake_user2', 'F/zgAxSBr9LSP4CIj01Tr4Z6g56cqUalOxpd32C6GbQ=', NOW(), NOW());