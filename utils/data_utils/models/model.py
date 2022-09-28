#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/9/23
# @Author: xuef
# @File: model.py
# @Desc:

from pydantic import BaseModel
from typing import Union, List


class Host(BaseModel):
    test: str
    proc: str


class MySqlConf(BaseModel):
    host: str
    port: int = 3306
    user: str
    password: str
    database: str
    charset: str = 'utf8'


class EmailConf(BaseModel):
    host: str
    user: str
    key: str
    recevies: Union[str, List[str]]


class DingTalkConf(BaseModel):
    webhook: str
    secret: str


class Config(BaseModel):
    project_name: str
    tester: str
    env: str
    host: Host
    notification_type: int = 0
    cache_type: int = 0
    mysql: MySqlConf
    email: EmailConf
    ding_talk: DingTalkConf


