#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Author:moon.shan

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class SendMail():
    def sendMail(self):
        with open("../TestCaseSuit.xlsx",'r') as f:
            self.content = f.read().decode('UTF-8')