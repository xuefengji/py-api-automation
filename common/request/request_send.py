#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/1
# @Author: xuef
# @File: request_send.py
# @Desc:

import allure
from utils.request_utils.request_base import BaseRequest
from utils.file_utils.operation_yaml import OperationYaml
from config import BaseConfig
from utils.log_utils.log_decorate import LogDecorate


class RequestSend(BaseRequest):

    def __init__(self):
        super(BaseRequest, self).__init__()

    @LogDecorate(True)
    def send_request(self, case_info:dict, case_data:dict):
        url = case_info['url']
        method = case_info['method']
        headers = case_data['headers']
        request_type = case_data['request_type']
        data = case_data['data']
        host = self.get_host()
        request_url = host + url
        if hasattr(RequestSend, method):
            res = getattr(RequestSend, method)(
                self,
                request_url,
                headers,
                data,
                request_type,
                cookies=None
            )
            with allure.step('发送{}请求'.format(method)):
                allure.attach(name="当前请求url：", body=request_url)

                allure.attach(name="当前请求headers：", body=str(headers))
                allure.attach(name="当前请求数据：", body=str(data))
                allure.attach(name="当前请求结果：", body=str(res.status_code))
            return res
        raise ValueError("当前请求方式不存在！")

    def get_host(self):
        """
        获取环境地址
        ：param environment:
        """
        env = OperationYaml.read_yaml(BaseConfig.setting_dir)
        return BaseConfig.get_environment(env['environment'])






