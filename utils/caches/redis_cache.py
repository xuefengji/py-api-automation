#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/9/16
# @Author: xuef
# @File: redis_cache.py
# @Desc: 封装 redis

import redis


class RedisHandle:
    def __init__(self, config):
        self.conn = redis.Redis(**config)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def hash_set(self):
        pass



r = redis.Redis(host='127.0.0.1', password='hgj%li46h@', port=6379, db=0, decode_responses=True)
r.set('name', 'runoob')  # 设置 name 对应的值
print(r['name'])
print(r.get('name'))  # 取出键 name 对应的值
print(type(r.get('name')))  # 查看类型
