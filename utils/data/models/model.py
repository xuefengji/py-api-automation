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
    mysql: MySqlConf
    email: EmailConf
    ding_talk: DingTalkConf


class RequestData(BaseModel):
    data: Optional[Union[Dict, None]] = None
    param: Optional[Union[Dict, None]] = None
    file: Optional[Union[Dict, None]] = None


class DependsData(BaseModel):
    type: str
    data: str
    set_cache: Optional[str]


class DependsCase(BaseModel):
    case_id: str
    depends_data: Union[None, List[DependsData]] = None


class RequestSetCache(BaseModel):
    name: str
    type: str
    json_path: str


class AssertData(BaseModel):
    assert_type: str
    actual: str
    type: str
    expect: str


class TestCaseData(BaseModel):
    url: str
    method: str
    is_run: Union[bool, None] = False
    title: str
    headers: Dict = {}
    request_type: str
    data: RequestData
    encode: Optional[Union[List, None]] = None
    is_depend: Union[bool, None] = False
    depends_case: Optional[Union[List[DependsCase], None]]=None
    setup_sql: Optional[str, List[str], None] = None
    request_set_cache: Optional[Union[List[RequestSetCache], None]] = None
    assert_data: Union[Dict[AssertData], str]
    assert_sql: Optional[str, List[str]] = None


class TestCaseInfo(BaseModel):
    url: str
    method: str


class TestCase(BaseModel):
    info: TestCaseInfo
    case: TestCaseData




