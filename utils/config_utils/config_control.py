#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/23
# @Author: xuef
# @File: config_control.py
# @Desc: 获取 config 内容

from config import BaseConfig
from utils.file_utils.operation_yaml import OperationYaml


class ConfigGet(BaseConfig):

    def __init__(self):
        self.yaml_data = OperationYaml.read_yaml(ConfigGet.setting_dir)

    def get_environment(self, environment: str) -> dict:
        """
        获取相应环境信息
        : param environment: setting 中配置的环境信息
        """
        env = OperationYaml.read_yaml(self.environment_dir)
        if environment in env.keys():
            return env[environment]
        raise ValueError("配置的环境信息不存在")

    #获取主机信息
    def get_host(self) -> str:
        # print(cls.setting_dir)
        environment = self.yaml_data['environment']
        return str(self.get_environment(str(environment)))

    #获取 email 信息

    def get_email(self) -> dict:
        return self.yaml_data['email']


    def get_mysql(self) -> dict:
        return self.yaml_data['mysql']


    def get_ding_talk(self) -> dict:
        return self.yaml_data['ding_talk']




