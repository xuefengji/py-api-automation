#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/10/9
# @Author: xuef
# @File: local_cache.py
# @Desc:

from typing import Any

_cache_data = {}


class CacheHandle:

    @classmethod
    def update_cache(cls, name: str, value: str) -> bool:
        try:
            _cache_data[name] = value
            return True
        except Exception as e:
            raise ValueError('更新缓存失败')

    @classmethod
    def get_cache(cls, name: str) -> Any:
        if name in _cache_data.keys():
            return _cache_data[name]
        raise ValueError('缓存不存在')
