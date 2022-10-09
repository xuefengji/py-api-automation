#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/10
# @Author: xuef
# @File: notify_mail.py
# @Desc:

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from utils.file.operation_yaml import OperationYaml
from config import BaseConfig
from utils.report.report_summary import Summary

class SendMail:

    def __init__(self, case_report):
        self.case_report = case_report
        self.email_data = OperationYaml.read_yaml(BaseConfig.setting_dir)['email']
        self.host = self.email_data['host']
        self.user = self.email_data['user']
        self.password = self.email_data['key']
        self.recevies = self.email_data['recevies']


    def send_mail(self, sub, content):
        sender = "snowji" + '<' + self.user + '>'
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['From'] = sender
        message['To'] = ';'.join(self.recevies)
        subject = sub
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(self.user, self.password)
            smtpObj.sendmail(sender, self.recevies, message.as_string())
        except smtplib.SMTPException:
            raise smtplib.SMTPException("无法发送邮件")

    def send_main(self):
        sub = '接口自动化测试'
        content = f"""
        Dear all:
            自动化用例执行完成，执行结果如下:
            用例运行总数: {self.case_report['total']} 个
            通过用例个数: {self.case_report['passed']} 个
            失败用例个数: {self.case_report['failed']} 个
            异常用例个数: {self.case_report['error']} 个
            跳过用例个数: {self.case_report['skipped']} 个
            成  功   率: {self.case_report['pass_rate']} %
        """
        self.send_mail(sub, content)

if __name__ == '__main__':
    case_report = Summary.get_case_report()
    SendMail(case_report).send_main()

