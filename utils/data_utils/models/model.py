#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/9/23
# @Author: xuef
# @File: model.py
# @Desc:

from pydantic import BaseModel
from typing import Union, List, Dict, Optional


class Host(BaseModel):
    test: str
    proc: str


class MySqlConf(BaseModel):
    host: str
    port: int = 3306
    user: str
    password: str
    database: str
    charset: Optional[str] = 'utf8'


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


class RequestData(BaseModel):
    body: Optional[Union[Dict, None]] = None
    params: Optional[Union[Dict, None]] = None


class DependData(BaseModel):
    type: str
    json_path: str


class DependsCase(BaseModel):
    case_id: str
    depends_data: List[DependData]


class SetCache(BaseModel):
    name: str
    type: str
    json_path: str


class AssertData(BaseModel):
    assert_type: str
    actual: str
    type: str
    expect: str


class TestCaseData(BaseModel):
    id: str
    is_run: Union[bool, None] = None
    title: str
    headers: Dict = {}
    request_type: str
    data: RequestData
    encode: Optional[Union[List, str, None]] = None
    is_depend: Union[bool, None] = False
    depends_case: Optional[Union[List[DependsCase], None]]=None
    setup_sql: Optional[str, List[str], None] = None
    set_cache: Optional[Union[List[SetCache], None]] = None
    assert_data: Union[Dict[AssertData], str]
    assert_sql: Optional[str, List[str]] = None


class TestCaseInfo(BaseModel):
    url: str
    method: str


class TestCase(BaseModel):
    info: TestCaseInfo
    case: TestCaseData




