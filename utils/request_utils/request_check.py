#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/4 14:37
# @Author: xuef
# @File: request_check.py
# @Desc:
import os.path

from jsonpath import jsonpath
from urllib.parse import quote
from config import BaseConfig
from utils.random_utils.random_data import RandomUtil
from utils.file_utils.operation_cache import OperationCache

class Check:

    @classmethod
    def check(cls, info:dict, data:dict):
        """
        检查请求前相应的数据
        :param data: 用例基本信息
        :param data: 用例数据
        :return:
        """
        info, data = Check.check_url(info, data)
        data = Check.check_headers(data)
        data = Check.check_data(data)
        return info, data

    @classmethod
    def check_data(cls,data:dict)->dict:
        """
        检查是否有参数需要编码
        :param data: 用例数据
        :return:
        """
        # print(case_data)
        encode_data = data['url_encode']
        case_data = data['data']
        # 校验是否有依赖数据
        for k, v in case_data.items():
            for j, h in v.items():
                if str(h).startswith('$'):
                    case_data[k][j] = jsonpath(data, h)[0]
                elif str(h).startswith('random'):
                    if hasattr(RandomUtil, str(h)):
                        case_data[k][j] = getattr(RandomUtil, str(h))('test', 3)
                    else:
                        raise ValueError('当前随机生成的函数不存在！')
        # 校验是否有参数编码
        if encode_data:
            for i in encode_data:
                case_data[i.split(':')[0]][i.split(':')[1]] = Check.url_encode(case_data[i.split(':')[0]][i.split(':')[1]])
            return data
        return data

    @classmethod
    def check_url(cls, info:dict, data:dict):
        """
        校验 url 中是否有参数
        :param info: 用例信息
        :param data: 用例数据
        :return:
        """
        url_list = info['url'].split('/')
        for index, value in enumerate(url_list):
            if value.startswith('$'):
                url_list[index] = jsonpath(data, value)[0]
                info['url'] = '/'.join(url_list)
        return info, data

    @classmethod
    def check_headers(cls, data:dict):
        """
        检查headers
        :param data: 用例数据
        :return:
        """
        headers = data['headers']
        try:
            for k, v in headers.items():
                if v.startswith('$'):
                    if k == 'Authorization':
                        headers[k] =jsonpath(data, v)[0]
                    else:
                        headers[k] = jsonpath(data, v)[0]
                elif v.startswith('cache'):
                    headers[k] = OperationCache.read_cache(BaseConfig.root_dir+v.split('.')[0]+'/'+v.split('.')[1])
            return data
        except Exception as e:
            raise ValueError("check headers 失败")

    @staticmethod
    def url_encode(data:str):
        """
        参数编码
        :param data: 需要编码的值
        :return:
        """
        try:
            encode_data = quote(data)
            return encode_data
        except Exception as e:
            raise ValueError("参数编码失败！")
