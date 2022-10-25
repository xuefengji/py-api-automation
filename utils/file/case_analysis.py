#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/10/9
# @Author: xuef
# @File: case_analysis.py
# @Desc:

from typing import Dict, Union
from utils.file.operation_yaml import OperationYaml
from utils.caches.local_cache import CacheHandle
from utils.caches.redis_cache import RedisHandle
from utils import config
from utils.data.enums.enums import RequestMethod, RequestTypeEnum
from utils.data.models.model import TestCase


class CaseHandle:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_url(self, case_id:str, data: Dict):
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
                    'depends_case': self.get_depends_case(key, value),
                    'setup_sql': self.get_setup_sql(value),
                    'request_set_cache': self.get_request_set_cache(value),
                    'assert_data': self.get_assert_data(key, value),
                    'assert_sql': self.get_assert_sql(value),
                    'tear_down': self.get_tear_down(value),
                    'tear_down_sql': self.get_tear_down_sql(value),
                    'sleep': self.get_sleep(value)

                }
                _case_lists.append({key: TestCase(**case_data).dict()})
        return _case_lists

    def get_method(self, case_id: str, data: Dict):
        """获取请求方式"""
        _method = data['method']
        if _method is None:
            raise ValueError(
                f"用例中的请求方式不能为空！\n "
                f"用例ID: {case_id} \n "
                f"用例路径: {self.file_path}"
            )
        if _method not in [e.value for e in RequestMethod]:
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
        try:
            _is_run = data['is_run']
            return _is_run
        except Exception as e:
            return False

    def get_title(self, case_id: str,data:Dict):
        try:
            _title = data['title']
            return _title
        except Exception as e:
            raise ValueError(
                f"用例中的描述不能为空！\n "
                f"用例ID: {case_id} \n "
                f"用例路径: {self.file_path}"
            )

    def get_headers(self, data:Dict):
        try:
            _headers = data['headers']
            return _headers
        except Exception as e:
            return None

    def get_request_type(self, case_id: str, data:Dict):
        _request_type = data['request_type']
        if _request_type is None:
            raise ValueError(
                f"用例中的参数请求类型不能为空！\n "
                f"用例ID: {case_id} \n "
                f"用例路径: {self.file_path}"
            )
        return _request_type

    def get_data(self, case_id:str, data:Dict):
        _data = data['data']
        _request_types = [e.value for e in RequestTypeEnum]
        if self.get_request_type(case_id, data) not in _request_types:
            raise ValueError(
                f"用例中的参数类型不支持！\n "
                f"用例ID: {case_id} \n "
                f"用例路径: {self.file_path}"
            )
        if _data is not None:
            if not any(_data.values()):
                raise ValueError(
                    f"用例中的请求参数不能为空！\n "
                    f"用例ID: {case_id} \n "
                    f"用例路径: {self.file_path}"
                )
        return _data

    def get_encode(self, data:Dict):
        try:
            _encode = data['encode']
            return _encode
        except Exception as e:
            return None

    def get_is_depend(self, data:Dict):
        _is_depend = data['is_depend']
        if _is_depend is None:
           return False
        return _is_depend

    def get_depends_case(self,case_id: str , data:Dict)-> Union[Dict, None]:
        """
        判断是否有依赖数据，有则返回，无则返回 None
        """
        if self.get_is_depend(data):
            _depends_case = data['depends_case']
            if _depends_case is None:
                raise ValueError(
                    f"用例中的依赖数据不能为空！\n "
                    f"用例ID: {case_id} \n "
                    f"用例路径: {self.file_path}"
                )
            return _depends_case
        else:
            return None


    def get_setup_sql(self, data:Dict):
        try:
            _setup_sql = data['setup_sql']
            return _setup_sql
        except Exception as e:
            return None

    def get_request_set_cache(self, data:Dict):
        try:
            _request_set_cache = data['request_set_cache']
            return _request_set_cache
        except Exception as e:
            return None

    def get_assert_data(self, case_id:str, data:Dict):
        _assert_data = data['assert_data']
        if _assert_data is None:
            raise ValueError(
                f"用例中的断言不能为空！\n "
                f"用例ID: {case_id} \n "
                f"用例路径: {self.file_path}"
            )
        return _assert_data

    def get_assert_sql(self, data:Dict):
        _assert_sql = data['assert_sql']
        return _assert_sql

    def get_tear_down(self, data:Dict):
        try:
            _tear_down =data['tear_down']
            return _tear_down
        except Exception as e:
            return None

    def get_tear_down_sql(self, data:Dict):
        try:
            _tear_down_sql = data['tear_down_sql']
            return _tear_down_sql
        except Exception as e:
            return None

    def get_sleep(self, data:Dict):
        try:
            _sleep = data['sleep']
            return _sleep
        except Exception as e:
            return None


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




