#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/16
# @Author: xuef
# @File: operation_cache.py
# @Desc: 操作cache
import os.path
from config import BaseConfig

class OperationCache:
    @classmethod
    def read_cache(cls, path):
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return f.read()
            except Exception as e:
                raise IOError("读取缓存文件失败！")
        else:
            print(111)

    @classmethod
    def write_cache(cls, path, data):
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(data)
        except Exception as e:
            raise IOError("写入缓存文件失败！")


