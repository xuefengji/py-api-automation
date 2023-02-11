#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/1
# @Author: xuef
# @File: request_send.py
# @Desc: HTTP 请求发送相关操作
import os
import random
import ast
import allure
import requests
from jsonpath import jsonpath
from urllib.parse import quote
from requests_toolbelt import MultipartEncoder
from utils.data.enums.enums import RequestTypeEnum
from utils.data.models.model import TestCase
from utils.log.log_decorate import LogDecorate
from utils.log.log_control import ERROR
from utils import config
from common.request.request_teardown import RequestSetCache
from utils.file.case_regular import regular_cache
from config import BaseConfig


class RequestHandle:
    """
    处理http请求发送
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, case_data):
        # self.data_encode(case_data)
        self._case_data = TestCase(**case_data)

    def type_for_json(self):
        """
        请求方式为json
        """
        _data= self._case_data.data
        _method = self._case_data.method
        _url = self._case_data.url
        _headers = self._case_data.headers
        if _data.body is None:
            raise ValueError(f"参数数据不能为空，：{_data.body}")
        try:
            res = requests.request(
                method=_method,
                url=regular_cache(_url),
                headers=ast.literal_eval(regular_cache(_headers)),
                json=_data.body,
                params = _data.query,
            )
            return res
        except Exception as e:
            ERROR.error("发送 {} 请求失败:{}".format(self._case_data.method, e))
            raise ValueError("发送 {} 请求失败！".format(self._case_data.method))

    def type_for_params(self):
        """
        请求方式为params
        """
        _data = self._case_data.data
        _method = self._case_data.method
        _url = self._case_data.url
        _headers = self._case_data.headers
        if _data.query is None:
            raise ValueError(f"参数数据不能为空，：{_data.query}")
        try:
            res = requests.request(
                method=_method,
                url=regular_cache(_url),
                headers=ast.literal_eval(regular_cache(str(_headers))),
                params=_data.query,
            )
            return res
        except Exception as e:
            ERROR.error("发送 {} 请求失败:{}".format(self._case_data.method, e))
            raise ValueError("发送 {} 请求失败！".format(self._case_data.method))

    def multipart_file(self):
        """
        将文件进行编码
        """
        files = self._case_data.data.file
        if files is None:
            raise ValueError(f"参数数据不能为空，：{self._case_data.data.file}")
        for k, v in files.items():
            file_path = os.path.join(BaseConfig.file_dir, v)
            if not os.path.isfile(file_path):
                raise ValueError('当前参数不是文件')
            files[k] = (os.path.basename(v), open(file_path, 'rb'))
        return files

    def type_for_file(self):
        """
        请求方式为文件类型
        """
        files = self.multipart_file()
        enc = MultipartEncoder(
            fields=files,
            boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
        )
        self._case_data.headers['Content-Type'] = enc.content_type
        try:
            res = requests.request(method=self._case_data.method,
                                   url=regular_cache(self._case_data.url),
                                   data=enc,
                                   params=self._case_data.data.query,
                                   headers=ast.literal_eval(regular_cache(str(self._case_data.headers))),
                                   verify=False)
            return res
        except Exception as e:
            ERROR.error("发送 {} 请求失败:{}".format(self._case_data.method, e))
            raise ValueError("发送 {} 请求失败！".format(self._case_data.method))

    def type_for_data(self):
        """
        请求方式为data
        """
        _data= self._case_data.data
        if _data.body is None:
            raise ValueError(f"参数数据不能为空，：{_data.body}")
        if _data.param is None:
            _data.param = {}
        try:
            res = requests.request(
                method=self._case_data.method,
                url=self._case_data.url,
                headers = ast.literal_eval(regular_cache(str(self._case_data.headers))),
                data=_data.body,
                params = _data.query,
            )
            return res
        except Exception as e:
            ERROR.error("发送 {} 请求失败:{}".format(self._case_data.method, e))
            raise ValueError("发送 {} 请求失败！".format(self._case_data.method))

    def type_for_export(self, file=False):
        #TODO 导出接口
        param = self._case_data.data.query
        body = self._case_data.data.body
        try:
            res = requests.request(
                method=self._case_data.method,
                url=self._case_data.url,
                headers = self._case_data.headers,
                data=body,
                params = param
            )
        except Exception as e:
            ERROR.error("发送 {} 请求失败:{}".format(self._case_data.method, e))
            raise ValueError("发送 {} 请求失败！".format(self._case_data.method))



    @staticmethod
    def cache_check():
        pass

    @LogDecorate(config.log)
    def send_request(self):
        """
        发送 http 请求
        """
        if self._case_data.is_run is True or None:
            request_type_mapping = {
                RequestTypeEnum.JSON.value: self.type_for_json,
                RequestTypeEnum.PARAMS.value: self.type_for_params,
                RequestTypeEnum.FILE.value: self.type_for_file,
                RequestTypeEnum.DATA.value: self.type_for_data,
                RequestTypeEnum.EXPORT.value: self.type_for_export
            }
            res = request_type_mapping.get(self._case_data.request_type)()
            with allure.step('发送{}请求'.format(self._case_data.method)):
                allure.attach(name="当前请求url：", body=self._case_data.url)

                allure.attach(name="当前请求headers：", body=str(self._case_data.headers))
                allure.attach(name="当前请求数据：", body=str(self._case_data.data.body))
                allure.attach(name="当前请求结果：", body=str(res.status_code))

            RequestSetCache(self._case_data.request_set_cache, self._case_data.data, res).set_cache()

            return res






