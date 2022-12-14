#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/9/16
# @Author: xuef
# @File: redis_cache.py
# @Desc: 封装 redis

import redis
from typing import Any, Dict
from utils.data.models.model import RedisConf


class RedisHandle:
    def __init__(self, config: Dict):
        try:
         self.conn = redis.Redis(RedisConf(**config))
        except ConnectionError as e:
            raise ConnectionError('Redis 连接失败') from e

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def hash_set(self, key: str, value: Any, name: str='cases') -> None:
        """
        设置hash类型存储的数据
        param name:
        param key:
        param value:
        """
        self.conn.hset(name, key, value)

    def hash_get(self, key, name='cases'):
        """
        hash类型单个值获取
        param name:
        param key:
        """
        res = self.conn.hget(name, key)
        if res:
            return res


