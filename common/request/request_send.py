#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/1
# @Author: xuef
# @File: request_send.py
# @Desc:

import allure
from utils.request_utils.request_definition import BaseRequest
from utils.request_utils.request_type import RequestType
from utils.log_utils.log_decorate import LogDecorate


class RequestSend(BaseRequest,RequestType):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    @LogDecorate(True)
    def send_request(self, case_info:dict, case_data:dict):
        url = case_info['url']
        method = case_info['method']
        headers = case_data['headers']
        request_type = case_data['request_type']
        data = case_data['data']['body']
        params = case_data['data']['params']
        if hasattr(RequestSend, method):
            res = RequestSend.request_type(
                method=method,
                url=url,
                headers=headers,
                data=data,
                params=params,
                request_type=request_type,
                cookies=None
            )
            with allure.step('发送{}请求'.format(method)):
                allure.attach(name="当前请求url：", body=url)

                allure.attach(name="当前请求headers：", body=str(headers))
                allure.attach(name="当前请求数据：", body=str(data))
                allure.attach(name="当前请求结果：", body=str(res.status_code))
            return res
        raise ValueError("当前请求方式不存在！")







