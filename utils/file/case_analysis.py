#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/10/9
# @Author: xuef
# @File: case_analysis.py
# @Desc:

from typing import Dict
from utils.file.operation_yaml import OperationYaml
from utils.caches.local_cache import CacheHandle
from utils.caches.redis_cache import RedisHandle
from utils import config
from common.request.request_send import BaseRequest
from utils.data.models.model import TestCase


class CaseHandle:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_url(self, case_id:str, data: Dict) -> str:
        """
        获取url和host并进行拼接
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
        _case_datas = OperationYaml.read_yaml(self.file_path)
        _case_lists = []
        for key, value in _case_datas.items():
            if key != 'info':
                case_data = {
                    'url': self.get_url(key, value),
                    'method': self.get_method(key, value),
                    'is_run': self.get_is_run(value),
                    'title': self.get_title(key, value),
                    'headers': self.get_headers(value),
                    'request_type': self.get_request_type(key, value),
                    'data': self.get_data(key, value),
                    'encode': self.get_encode(value),
                    'is_depend': self.get_is_depend(value),
                    'depends_case': self.get_depends_case(value),
                    'setup_sql': self.setup_sql(value),
                    'request_set_cache': self.get_request_set_cache(value),
                    'assert_data': self.get_assert_data(value),
                    'assert_sql': self.get_assert_sql(value),
                    'tear_down': self.get_tear_down(value),
                    'tear_down_sql': self.get_tear_down_sql(value),
                    'sleep': self.get_sleep(value)

                }
                _case_lists.append({key: TestCase(**case_data)})
        return _case_lists

    def get_method(self, case_id: str, data: Dict) -> str:
        """获取请求方式"""
        _method = data['method']
        if _method is None:
            raise ValueError(
                f"用例中的请求方式不能为空！\n "
                f"用例ID: {case_id} \n "
                f"用例路径: {self.file_path}"
            )
        if not hasattr(BaseRequest, _method):
            raise ValueError(
                f"用例中的请求方式不存在，请检查！\n "
                f"用例ID: {case_id} \n "
                f"用例路径: {self.file_path}"
            )
        return _method

    def get_is_run(self, data: Dict)->bool:
        """
        获取用例是否运行
        """
        _is_run = data['is_run']
        return _is_run

    def get_title(self):
        pass

    def get_headers(self):
        pass

    def get_request_type(self):
        pass

    def get_data(self):
        pass

    def get_encode(self):
        pass

    def get_is_depend(self):
        pass

    def get_depends_case(self):
        pass

    def setup_sql(self):
        pass

    def get_request_set_cache(self):
        pass

    def get_assert_data(self):
        pass

    def get_assert_sql(self):
        pass

    def get_tear_down(self):
        pass

    def get_tear_down_sql(self):
        pass

    def get_sleep(self):
        pass


class GetCaseHandle:

    @classmethod
    def get_cases(cls, ids: list, cache_type:int=0) -> list:
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




