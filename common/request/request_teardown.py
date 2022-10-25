#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/3
# @Author: xuef
# @File: request_teardown.py
# @Desc:


import json
from jsonpath import jsonpath
from common.asserts.assert_base import Assert
from utils.database.mysql_control import MySQL
from utils.caches.local_cache import CacheHandle
from utils.caches.redis_cache import RedisHandle
from utils import config


class TearDown:

    @classmethod
    def assert_actual(cls,data:dict):
        """
        断言期望结果和实际结果
        :param data: 断言数据
        :return:
        """
        actual = data['actual']
        expect = data['expect']
        type = data['type']
        Assert().expect_check(expect, actual,type)

    @classmethod
    def get_assert_jsonpath(cls, data:dict, res=None):
        """
        获取 assert 数据
        :param res: 请求后数据
        :param data: 断言数据
        :return:
        """
        assert_type = data['assert_type']
        if assert_type == "response":
            data = TearDown.get_assert_response(res, data)
        elif assert_type == "headers":
            data = TearDown.get_assert_headers(res, data)
        elif assert_type == "sql":
            data = TearDown.get_assert_sql(data)
        return data

    @classmethod
    def get_depend_data(cls, res, data: dict):
        """
        获取 依赖数据
        :param res: 请求后数据
        :param data: 依赖数据
        :return:
        """
        depends_data = data['depends_data_type']
        if depends_data == "response":
            data = TearDown.get_depends_response(res, data)
        elif depends_data == "headers":
            data = TearDown.get_depends_headers(res, data)
        return data

    @staticmethod
    def get_assert_response(res, data:dict):
        """
        获取 response 数据
        :param res: 请求
        :param data: assert 值
        :return:
        """
        try:
            res = jsonpath(res.json(), data['actual'])
            data['actual'] = res[0]
            return data
        except Exception as e:
            raise ValueError("获取断言response相关值失败！")

    @staticmethod
    def get_assert_headers(res, data:dict):
        """
        获取请求头断言数据
        :param res: 请求
        :param data: assert 值
        :return:
        """
        try:
            res = jsonpath(res.request.headers, data['actual'])
            data['actual'] = res[0]
            return data
        except Exception as e:
            raise ValueError("获取断言headers相关值失败！")

    @staticmethod
    def get_assert_sql(data:dict):
        """
        获取sql请求断言数据
        :param data: assert 值
        :return:
        """
        config = ConfigGet.get_mysql()
        try:
            res = MySQL(config).select( data['actual'])
            data['actual'] = res
            return data
        except Exception as e:
            raise ValueError("获取数据库断言相关值失败！")


    @staticmethod
    def get_depends_response(res, data:dict):
        """
        获取 response 数据
        :param res: 请求后数据
        :param data: assert 值
        :return:
        """
        try:
            res = jsonpath(res.json(), data['depends_data'])
            data['depends_data'] = res[0]
            return data
        except Exception as e:
            raise ValueError("获取依赖response相关值失败！")

    @staticmethod
    def get_depends_headers(res, data:dict):
        """
        获取请求头数据
        :param res: 请求
        :param data: assert 值
        :return:
        """
        try:
            res = jsonpath(res.request.headers, data['depends_data'])
            data['depends_data'] = res[0]
            return data
        except Exception as e:
            raise ValueError("获取依赖headers相关值失败！")


class RequestSetCache:

    def __init__(self, request_set_cache, request_data, response_data):
        self.request_set_cache = request_set_cache
        self.response_data = response_data.json()
        self.request_data = {'data':request_data}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_response_cache(self, key, json_path, cache_type=config.cache_type):
        _data = jsonpath(self.response_data, json_path)
        if _data:
            if cache_type == 0:
                CacheHandle.update_cache(key, _data[0])
            elif cache_type == 1:
                #todo
                RedisHandle.hash_set(key, _data[0])

    def set_request_cache(self, key, json_path, cache_type=config.cache_type):
        _data = jsonpath(self.request_data, json_path)
        if _data:
            if cache_type == 0:
                CacheHandle.update_cache(key, _data[0])
            elif cache_type == 1:
                # todo
                RedisHandle.hash_set(key, _data[0])

    def set_cache(self):
        if self.request_set_cache:
            for i in self.request_set_cache:
                _name = i.name
                _json_path = i.json_path
                _type = i.type
                if _type == 'request':
                    self.set_request_cache(_name, _json_path)
                elif _type == 'response':
                    self.set_response_cache( _name, _json_path)