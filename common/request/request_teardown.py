#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/3
# @Author: xuef
# @File: request_teardown.py
# @Desc:


import json
from jsonpath import jsonpath
from common.asserts.assert_base import Assert
from utils.database_utils.mysql_control import MySQL
from utils.config_utils.config_control import ConfigGet

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
        assert_data = data['assert_data']
        if assert_data == "response":
            data = TearDown.get_assert_response(data, res)
        elif assert_data == "headers":
            data = TearDown.get_assert_headers(data, res)
        elif assert_data == "sql":
            data = TearDown.get_assert_sql(data)
        return data

    @classmethod
    def get_depend_jsonpath(cls, res, data: dict):
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

