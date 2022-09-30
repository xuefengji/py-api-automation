#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/9/30
# @Author: xuef
# @File: __init__.py.py
# @Desc:


from typing import Any


_cache_data = {}


class CacheHandle:

    @classmethod
    def get_cache(cls, key:str) -> str:
        """
        获取缓存值
        :param key: 缓存名
        """
        if key in _cache_data:
            return _cache_data[key]
        raise ValueError('该缓存名不存在')


    @classmethod
    def update_cache(cls, key: str, value:Any) -> bool:
        """
        更新缓存内容
        :params key: 要更新的缓存名
        :params value: 更新的值
        """
        try:
            _cache_data[key] = value
            return True
        except Exception:
            raise ValueError('更新缓存失败')


