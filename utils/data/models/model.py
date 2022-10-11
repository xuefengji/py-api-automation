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


class RedisConf(BaseModel):
    host: str
    password: Optional[str]
    port: int = 6379
    db: Optional[int] = 0
    decode_responses: Optional[bool] = True


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
    redis: RedisConf


class RequestData(BaseModel):
    data: Optional[Union[Dict, None]] = None
    param: Optional[Union[Dict, None]] = None
    file: Optional[Union[Dict, None]] = None


class DependsData(BaseModel):
    type: str
    depend_data: str
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


class Prepare(BaseModel):
    depend_type: str
    json_path: str
    set_cache: str


class SendRequest(BaseModel):
    depend_type: str
    json_path: Optional[str]
    cache_key: Optional[str]
    replace_key: Optional[str]
    set_cache: Optional[str]


class TearDown(BaseModel):
    case_id: str
    prepare: Optional[List[Prepare]]
    send_request: Optional[List[SendRequest]]



class TestCase(BaseModel):
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
    setup_sql: Optional[Union[str, List[str], None]] = None
    request_set_cache: Optional[Union[List[RequestSetCache], None]] = None
    assert_data: AssertData
    assert_sql: Optional[Union[str, List[str], None]] = None
    tear_down: Optional[Union[List[TearDown], None]] = None
    tear_down_sql: Optional[List] = None
    sleep: Optional[Union[int, float]]


class TestCaseInfo(BaseModel):
    url: str
    method: str





