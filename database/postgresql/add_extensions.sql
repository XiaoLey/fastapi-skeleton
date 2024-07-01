-- 添加 hstore 扩展，支持键值对存储
-- 这个扩展用于在数据库中存储键值对，需要 Peewee 的 HStoreField
CREATE EXTENSION IF NOT EXISTS hstore;

-- 添加 pg_trgm 扩展，用于 trigram 索引以加速文本搜索
-- 主要用于全文搜索，提高 LIKE 和 ILIKE 查询性能
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- 添加 unaccent 扩展，用于去除文本中的重音符号
-- 对提高全文搜索的匹配率有帮助，尤其是处理国际化文本时
CREATE EXTENSION IF NOT EXISTS unaccent;

-- 添加 uuid-ossp 扩展，用于生成 UUID
-- Peewee 可以利用 UUIDField 存储和生成 UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 添加 btree_gin 和 btree_gist 扩展，用于创建 B-tree 索引的 GIN 和 GiST 索引支持
-- 这些索引类型对于特定查询可以提高性能
CREATE EXTENSION IF NOT EXISTS btree_gin;
CREATE EXTENSION IF NOT EXISTS btree_gist;

-- 添加 fuzzystrmatch 扩展，用于实现模糊字符串匹配
-- 这个扩展可以辅助文本相似度分析和匹配
CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;

-- 查看所有已安装的扩展
-- 这个命令用于验证上述扩展是否已成功安装
SELECT * FROM pg_extension;
