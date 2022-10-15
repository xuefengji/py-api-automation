#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/1
# @Author: xuef
# @File: request_send.py
# @Desc: HTTP 请求发送相关操作

import allure
import requests
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
        res = requests.request(
            method=_method,
            url=_url,
            headers = _headers,
            json=_data.body,
            params = _data.body,
        )
        return res

    def type_for_params(self):
        _data = self._case_data.data
        _method = self._case_data.method
        _url = self._case_data.url
        _headers = self._case_data.headers
        if _data.query is None:
            raise ValueError(f"参数数据不能为空，：{_data.query}")
        res = requests.request(
            method=_method,
            url=_url,
            headers=_headers,
            params=_data.query,
        )
        return res

    def type_for_file(self):
        pass

    def type_for_data(self):
        pass

    def type_for_export(self):
        pass

    def data_analysis(self):
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






