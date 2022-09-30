#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/17
# @Author: xuef
# @File: mysql_control.py
# @Desc: 封装操作数据库

import pymysql
import traceback
from typing import List
from utils.log_utils.log_control import ERROR




class MySQL:

    def __init__(self, config: dict):
        try:
            self.conn = pymysql.connect(**config)
            # 使用 cursor 方法获取操作游标，得到一个可以执行sql语句，并且操作结果为字典返回的游标
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)  # 括号内不写参数,数据是元组套元组
        except Exception :
            ERROR.error(f"连接数据库失败，错误信息：{traceback.format_exc()}")
            quit()


    def __del__(self):
        if hasattr(self, "conn"):
            self.cursor.close()
            self.conn.close()

    def execute(self, sql):
        """
        update、delete、insert操作
        :param sql: sql 语句
        :return: 影响的行数
        """
        try:
            rows = self.cursor.execute(sql)
            self.conn.commit()
            return rows
        except Exception:
            self.conn.rollback()    # 发生错误时回滚
            ERROR.error(f"sql语句执行失败，错误信息：{traceback.format_exc()}")
            raise

    def query(self, sql, type='all'):
        """
        select 查询操作
        :param sql: sql 语句
        :param type: 查询的数据条目，all表示全部，one 表示一条
        """
        try:
            flag = self.execute(sql)
            if flag:
                if type == 'one':
                    data = self.cursor.fetchone()
                else:
                    data = self.cursor.fetchall()
                return data
        except Exception:
            ERROR.error(f"sql语句执行失败，错误信息：{traceback.format_exc()}")


class SetUpSql(MySQL):
    """处理依赖前置sql"""
    def set_up_sql(self, sql:List):
        if sql:
            data = {}
            for i in sql:
                if i[0:6].upper() == 'SELECT':
                    sql_data = self.query(i)
                    for key, value in sql_data.items():
                        data[key]=value
                else:
                    self.execute(i)
            return data

