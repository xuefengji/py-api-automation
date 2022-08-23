#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/23
# @Author: xuef
# @File: config_control.py
# @Desc: 获取 config 内容

from config import BaseConfig
from utils.file_utils.operation_yaml import OperationYaml


class ConfigGet(BaseConfig):

    # 获取环境地址
    @classmethod
    def get_environment(cls, environment: str) -> dict:
        """
        获取相应环境信息
        : param environment: setting 中配置的环境信息
        """
        env = OperationYaml.read_yaml(cls.environment_dir)
        if environment in env.keys():
            return env[environment]
        raise ValueError("配置的环境信息不存在")

    # 获取setting配置
    @classmethod
    def get_setting(cls) -> dict:
        setting = OperationYaml.read_yaml(cls.setting_dir)
        return setting

    # 获取主机host
    @classmethod
    def get_host(cls) -> str:
        # print(cls.setting_dir)
        environment = cls.setting_dir['environment']
        return cls.get_environment(str(environment))['host']

    #获取 email 信息
    @classmethod
    def get_email(cls) -> dict:
        return cls.setting_dir['email']


    @classmethod
    def get_mysql(cls) -> dict:
        return cls.setting_dir['mysql']


if __name__ == '__main__':
    data = ConfigGet.get_setting()
    print(data)


