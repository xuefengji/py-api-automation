#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/9/6
# @Author: xuef
# @File: request_type.py
# @Desc:

import os
import random
import requests
from requests_toolbelt import MultipartEncoder
from utils.enums_utils.request_type_enum import RequestTypeEnum
from utils.log_utils.log_control import ERROR

class RequestType:

    @classmethod
    def request_type(
            cls,
            *,
            method,
            url,
            request_type,
            data,
            params,
            headers,
            cookies
    ):

        request_type_mapping = {
            RequestTypeEnum.JSON.value: cls.json,
            RequestTypeEnum.PARAMS.value: cls.params,
            RequestTypeEnum.FILE.value: cls.file,
            RequestTypeEnum.DATA.value: cls.data,
        }
        res = request_type_mapping.get(request_type)(
            method=method,
            url=url,
            data=data,
            params=params,
            headers=headers,
            cookies=cookies
        )
        return res

    @classmethod
    def file(
        cls,
        *,
        method,
        url,
        data,
        params,
        headers,
        cookies
    ):
        files = data
        for k, v in files.items():
            if os.path.isfile(v):
                files[k] = (os.path.basename(v), open(v, 'rb'))
        enc = MultipartEncoder(
            fields=files,
            boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
        )
        headers['Content-Type'] = enc.content_type
        try:
            res = requests.request(method=method,
                                   url=url,
                                   data=enc,
                                   params=params,
                                   headers=headers,
                                   cookies=cookies,
                                   verify=False)
            return res
        except Exception as e:
            ERROR.error("发送 {} 请求失败:{}".format(method,e))
            raise ValueError("发送 {} 请求失败！".format(method))

    @classmethod
    def json(
        cls,
        *,
        method,
        url,
        data,
        params,
        headers,
        cookies
    ):
        try:
            res = requests.request(
                method=method,
                url=url,
                json=data,
                params=params,
                headers=headers,
                cookies=cookies
            )
        except Exception as e:
            ERROR.error("发送 {} 请求失败:{}".format(method,e))
            raise ValueError("发送 {} 请求失败！".format(method))
        return res

    @classmethod
    def params(
        cls,
        *,
        method,
        url,
        data,
        params,
        headers,
        cookies
    ):
        try:
            res = requests.request(method=method,
                                   url=url,
                                   headers=headers,
                                   json=data,
                                   params=params,
                                   cookies=cookies,
                                   verify=False)
            return res
        except Exception as e:
            ERROR.error("发送 {} 请求失败:{}".format(method,e))
            raise ValueError("发送 {} 请求失败！".format(method))

    @classmethod
    def data(
        cls,
        *,
        method,
        url,
        data,
        params,
        headers,
        cookies
    ):
        try:
            res = requests.request(
                method=method,
                url=url,
                data=data,
                params=params,
                headers=headers,
                cookies=cookies,
                verify=False
            )
            return res
        except Exception as e:
            ERROR.error("发送 {} 请求失败:{}".format(method, e))
            raise ValueError("发送 {} 请求失败！".format(method))