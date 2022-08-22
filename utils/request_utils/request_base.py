#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/1
# @Author: xuef
# @File: request_base.py
# @Desc: 封装请求方式

import os, random
import requests
from requests_toolbelt import MultipartEncoder



class BaseRequest:

    def get(self, url, headers, data, request_type, cookies):
        return BaseRequest.request_type(self.get.__name__,
                                        url,
                                        headers,
                                        data,
                                        request_type,
                                        cookies=cookies)

    def post(self, url, headers, data, request_type, cookies):
        return BaseRequest.request_type(self.post.__name__,
                                        url,
                                        headers,
                                        data,
                                        request_type,
                                        cookies=cookies)

    def put(self, url, headers, data,request_type,cookies):
        return BaseRequest.request_type(self.put.__name__,
                                        url,
                                        headers,
                                        data,
                                        request_type,
                                        cookies=cookies)

    def delete(self, url, headers, data, request_type,cookies):
        return BaseRequest.request_type(self.delete.__name__,
                                        url,
                                        headers,
                                        data,
                                        request_type,
                                        cookies=cookies)

    @staticmethod
    def request_type(func_name, url, headers, data, request_type,cookies=None):
        params = {}
        if len(list(data.keys())) > 1:
            params = data['params']
        if request_type == 'json':
            try:
                res = requests.request(method=func_name,
                                       url=url,
                                       json=data['data'],
                                       params=params,
                                       headers=headers,
                                       cookies=cookies,
                                       verify=False)
                return res
            except Exception as e:
                raise ValueError("发送 {} 请求失败！".format(func_name))
        elif request_type == 'file':
            #判断是否为文件
            files = data['data']
            for k, v in files.items():
                if os.path.isfile(v):
                    files[k] = (os.path.basename(v), open(v, 'rb'))
            enc = MultipartEncoder(
                fields=files,
                boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
            )
            headers['Content-Type'] = enc.content_type
            try:
                res = requests.request(method=func_name,
                                       url=url,
                                       data=enc,
                                       params=params,
                                       headers=headers,
                                       cookies=cookies,
                                       verify=False)
                return res
            except Exception as e:
                raise ValueError("发送 {} 请求失败！".format(func_name))
        elif request_type == 'params':
            try:
                res = requests.request(method=func_name,
                                       url=url,
                                       headers=headers,
                                       params=data['data'] | params,
                                       cookies=cookies,
                                       verify=False)
                return res
            except Exception as e:
                raise ValueError("发送 {} 请求失败！".format(func_name))
        try:
            res = requests.request(method=func_name,
                                   url=url,
                                   data=data['data'],
                                   params=params,
                                   headers=headers,
                                   cookies=cookies,
                                   verify=False)
            return res
        except Exception as e:
            raise ValueError("发送 {} 请求失败！".format(func_name))
