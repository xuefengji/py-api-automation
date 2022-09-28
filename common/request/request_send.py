#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/1
# @Author: xuef
# @File: request_send.py
# @Desc:

import allure
from common.request.request_definition import BaseRequest
from common.request.request_type import RequestType
from utils.data_utils.models.model import TestCase, TestCaseInfo, TestCaseData
from utils.log_utils.log_decorate import LogDecorate
from utils import config

class RequestHandle(BaseRequest, RequestType):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, case_info, case_data):
        self._case_data = TestCase(
            info=TestCaseInfo(**case_info),
            case=TestCaseData(**case_data)
        )

    @LogDecorate(True)
    def send_request(self):
        if self._case_data.case.is_run is True or None:
            if hasattr(RequestHandle, self._case_data.info.method):
                res = RequestHandle.request_type(
                    method=self._case_data.info.method,
                    url=config.host + self._case_data.info.url,
                    headers=self._case_data.case.headers,
                    data=self._case_data.case.data.body,
                    params=self._case_data.case.data.params,
                    request_type=self._case_data.case.request_type,
                )
                with allure.step('发送{}请求'.format(self._case_data.info.method)):
                    allure.attach(name="当前请求url：", body=self._case_data.info.url)

                    allure.attach(name="当前请求headers：", body=str(self._case_data.case.headers))
                    allure.attach(name="当前请求数据：", body=str(self._case_data.case.data.body))
                    allure.attach(name="当前请求结果：", body=str(res.status_code))
                return res
            raise ValueError("当前请求方式不存在，请检查")

        # url = case_info['url']
        # method = case_info['method']
        # headers = case_data['headers']
        # request_type = case_data['request_type']
        # data = case_data['data']['body']
        # params = case_data['data']['params']
        # if hasattr(RequestHandle, method):
        #     res = RequestHandle.request_type(
        #         method=method,
        #         url=url,
        #         headers=headers,
        #         data=data,
        #         params=params,
        #         request_type=request_type,
        #     )
        #     with allure.step('发送{}请求'.format(method)):
        #         allure.attach(name="当前请求url：", body=url)
        #
        #         allure.attach(name="当前请求headers：", body=str(headers))
        #         allure.attach(name="当前请求数据：", body=str(data))
        #         allure.attach(name="当前请求结果：", body=str(res.status_code))
        #     return res
        # raise ValueError("当前请求方式不存在！")










