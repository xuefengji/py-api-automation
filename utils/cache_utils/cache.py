#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/10/4
# @Author: xuef
# @File: cache.py
# @Desc:

from typing import Any

_cache_data = {}

class CacheHandle:

    @staticmethod
    def update_cache(key: str, value:Any) -> bool:
        try:
            _cache_data[key] = value
            return True
        except Exception as e:
            raise ValueError("更新缓存失败！") from e


    @staticmethod
    def get_cache(key: str) -> Any:
        if key in _cache_data.keys():
            return _cache_data[key]
        raise AttributeError("无该缓存，请检查缓存名是否正确")


