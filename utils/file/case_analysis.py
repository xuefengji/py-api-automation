#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/10/9
# @Author: xuef
# @File: case_analysis.py
# @Desc:

from typing import Dict
from utils.file.operation_yaml import OperationYaml
from utils.data.models.model import TestCase
from utils.caches.local_cache import CacheHandle
from utils.caches.redis_cache import RedisHandle
from utils import config


class CaseHandle:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def url_process(self, case_id:str, data: Dict) -> str:
        """
        拼接 host+url
        """
        _url = data['url']
        _host = data['host']
        if _url is None or _host is None:
            raise ValueError(
                f"用例中的 url 或者 host 不能为空！\n "
                f"用例ID: {case_id} \n "
                f"用例路径: {self.file_path}"
            )
        return _host + _url


    def case_handle(self):
        """
        获取yaml文件中的用例
        """
        print(self.file_path)
        _case_datas = OperationYaml.read_yaml(self.file_path)
        _case_lists = []

        for key, value in _case_datas.items():
            if key != 'info':
                _case_info = {
                    'url': self.url_process(key, value),
                    'method': value['method'],
                    'is_run': value['is_run'],
                    'title': value['title'],
                    'headers': value['headers'],
                    'request_type': value['request_type'],
                    'data': value['data'],
                    'encode': value['data'],
                    'is_depend': value['is_depend'],
                    'depends_case': value['depends_case'],
                    'setup_sql': value['setup_sql'],
                    'request_set_cache': value['request_set_cache'],
                    'assert_data': value['assert_data'],
                    'assert_sql': value['assert_sql'],
                    'tear_down': value['tear_down'],
                    'tear_down_sql': value['tear_down_sql'],
                    'sleep': value['sleep']
                }
                _case_lists.append({key: TestCase(**_case_info).dict()})
        return _case_lists


class GetCaseHandle:

    @classmethod
    def get_cases(cls, cache_type:int, ids: list) -> list:
        """
        获取想要执行的用例
        param cache_type: 缓存类型
        param ids: 缓存中的用例 id
        """
        _case_lists = []
        for id in ids:
            if cache_type == 0:
                case_data = CacheHandle.get_cache(id)
                _case_lists.append(case_data)
            else:
                case_data = RedisHandle(config.redis).hash_get(id)
                _case_lists.append(case_data)
        return _case_lists




