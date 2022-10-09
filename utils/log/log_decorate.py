#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/11
# @Author: xuef
# @File: log_decorate.py
# @Desc:

from utils.log.log_control import ERROR, INFO


class LogDecorate():
    def __init__(self, switch:bool):
        self.switch = switch

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            message = f"\n======================================================\n" \
                           f"请求路径: {res.request.url}\n" \
                           f"请求方式: {res.request.method}\n" \
                           f"请求头: {res.request.headers}\n" \
                           f"请求内容: {res.request.body}\n" \
                           f"Http状态码: {res.status_code}\n" \
                           "====================================================="

            if self.switch:
                if res.status_code == 200:
                    INFO.info(message)
                else:
                    ERROR.error(message)
            return res
        return wrapper