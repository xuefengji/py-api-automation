#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/9/6
# @Author: xuef
# @File: dingtalk.py
# @Desc:

import time
import hmac
import hashlib
import base64
import urllib.parse
from typing import Text
from dingtalkchatbot.chatbot import DingtalkChatbot
from utils import config


class DingTalk:
    def __init__(self):
        self.timestamp = str(round(time.time() * 1000))
        self.config = config

    def xiao_ding(self):
        sign = self.get_sign()
        # 从yaml文件中获取钉钉配置信息
        webhook = self.config.ding_talk.webhook + "&timestamp=" + self.timestamp + "&sign=" + sign
        return DingtalkChatbot(webhook)

    def get_sign(self):
        secret = self.config.ding_talk.secret
        string_to_sign = '{}\n{}'.format(self.timestamp, secret).encode('utf-8')
        hmac_code = hmac.new(secret.encode('utf-8'), string_to_sign, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return sign

    def send_markdown(
            self,
            title: Text,
            msg: Text,
            mobiles=None,
            is_at_all=False
    ) -> None:
        if mobiles is None:
            self.xiao_ding().send_markdown(title=title, text=msg, is_at_all=is_at_all)
        else:
            if isinstance(mobiles, list):
                self.xiao_ding().send_markdown(title=title, text=msg, at_mobiles=mobiles)
            else:
                raise TypeError("mobiles类型错误 不是list类型.")

    def send_ding_notification(self):
        """ 发送钉钉报告通知 """
        text = f"#### 测试通知  " \
               f"我是一个测试机器人"
        self.send_markdown(
            title="【测试通知】",
            msg=text,
            mobiles=[1234567890]
        )

if __name__ == '__main__':
    info = DingTalk().send_ding_notification()
    print(info)
