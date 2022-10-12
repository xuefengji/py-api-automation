#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/10/11
# @Author: xuef
# @File: case_regular.py
# @Desc: 处理 yaml 数据

import random
import re
from faker import Faker
from utils.log.log_control import ERROR


class DataSimulate:
    """
    生成随机数据和获取相应的数据
    """
    def __int__(self):
        self.faker = Faker(locale='zh_CN')

    def simulate_name(self) -> str:
        """
        生成模拟姓名
        """
        return self.faker.name()

    def simulate_phone(self):
        """
        生成模拟手机号
        """
        return self.faker.phone_number()


    @classmethod
    def host(cls) -> str:
        """
        获取主机信息
        """
        from utils import config
        return config.host





def regular(target):
    """
    处理 yaml 文件中类似于 ${{host()}} 的数据
    param target: 需要处理的用例
    """
    pattern = r'\${(.*?)}'
    try:
        while re.findall(pattern, target):
            regular_data = re.search(pattern, target).group(1)
            func_name = regular_data.split('(')[0]
            value_data = regular_data.split('(')[1][:-1]
            if value_data:
                params = value_data.split(',')
                value = getattr(DataSimulate(), func_name)(*params)
                target = re.sub(pattern, str(value), target, 1)
                return target
            value = getattr(DataSimulate(), func_name)()
            target = re.sub(pattern, str(value), target, 1)
            return target
    except AttributeError:
        ERROR.error("未找到对应的替换的数据, 请检查数据是否正确 %s", target)
        raise

