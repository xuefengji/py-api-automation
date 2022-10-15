#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/1
# @Author: xuef
# @File: request_send.py
# @Desc: HTTP 请求发送相关操作
import os
import random

import allure
import requests
from requests_toolbelt import MultipartEncoder

from utils.data.enums.enums import RequestTypeEnum
from utils.data.models.model import TestCase
from utils.log.log_decorate import LogDecorate
from utils.log.log_control import ERROR


class BaseRequest:
    @classmethod
    def get(cls):
        pass

    @classmethod
    def post(cls):
        pass

    @classmethod
    def put(cls):
        pass

    @classmethod
    def delete(cls):
        pass


class RequestHandle:
    """
    处理http请求发送
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, case_data: TestCase):
        self._case_data = case_data

    def type_for_json(self):
        _data= self._case_data.data
        _method = self._case_data.method
        _url = self._case_data.url
        _headers = self._case_data.headers
        if _data.body is None:
            raise ValueError(f"参数数据不能为空，：{_data.body}")
        if _data.param is None:
            _data.param = {}
        try:
            res = requests.request(
                method=_method,
                url=_url,
                headers = _headers,
                json=_data.body,
                params = _data.body,
            )
            return res
        except Exception as e:
            ERROR.error("发送 {} 请求失败:{}".format(self._case_data.method, e))
            raise ValueError("发送 {} 请求失败！".format(self._case_data.method))

    def type_for_params(self):
        _data = self._case_data.data
        _method = self._case_data.method
        _url = self._case_data.url
        _headers = self._case_data.headers
        if _data.query is None:
            raise ValueError(f"参数数据不能为空，：{_data.query}")
        try:
            res = requests.request(
                method=_method,
                url=_url,
                headers=_headers,
                params=_data.query,
            )
            return res
        except Exception as e:
            ERROR.error("发送 {} 请求失败:{}".format(self._case_data.method, e))
            raise ValueError("发送 {} 请求失败！".format(self._case_data.method))

    def type_for_file(self):
        files = self._case_data.data.file
        if files is None:
            raise ValueError(f"参数数据不能为空，：{self._case_data.data.file}")
        for k, v in files.items():
            if os.path.isfile(v):
                files[k] = (os.path.basename(v), open(v, 'rb'))
        enc = MultipartEncoder(
            fields=files,
            boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
        )
        self._case_data.headers['Content-Type'] = enc.content_type
        try:
            res = requests.request(method=self._case_data.method,
                                   url=self._case_data.url,
                                   data=enc,
                                   params=self._case_data.data.query,
                                   headers=self._case_data.headers,
                                   verify=False)
            return res
        except Exception as e:
            ERROR.error("发送 {} 请求失败:{}".format(self._case_data.method, e))
            raise ValueError("发送 {} 请求失败！".format(self._case_data.method))

    def type_for_data(self):
        _data= self._case_data.data
        if _data.body is None:
            raise ValueError(f"参数数据不能为空，：{_data.body}")
        if _data.param is None:
            _data.param = {}
        try:
            res = requests.request(
                method=self._case_data.method,
                url=self._case_data.url,
                headers = self._case_data.headers,
                data=_data.body,
                params = _data.query,
            )
            return res
        except Exception as e:
            ERROR.error("发送 {} 请求失败:{}".format(self._case_data.method, e))
            raise ValueError("发送 {} 请求失败！".format(self._case_data.method))

    def type_for_export(self):
        pass

    @LogDecorate(True)
    def send_request(self):
        """
        发送 http 请求
        """
        if self._case_data.is_run is True or None:
            if hasattr(BaseRequest, self._case_data.method):
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
                    allure.attach(name="当前请求数据：", body=str(self._case_data.data.data))
                    allure.attach(name="当前请求结果：", body=str(res.status_code))
                return res
            raise ValueError("当前请求方式不存在，请检查")






