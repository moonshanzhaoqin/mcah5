#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Author:moon.shan
from common import LogFileHelper
from common.ResquestHelper import RequestHelper
import xlrd
import os,sys

class Login():
    # def __init__(self,env="DEMO"):
    #     LogFileHelper.logging.info(u"=====================================start loginlite")
    #     self.suburl = "/auth-server/api/jwt/pwd/login"
    #     self.headers = {"X-Role":"BORROWER","Content-Type": "application/x-www-form-urlencoded"}
    #     self.requestOne = RequestHelper(env=env,server="auth")
    #     self.params = {"identity":"15121000080","password":"welcome1"}
    #     self.requestOne.basicRequests(method="post", suburl=self.suburl, headers=self.headers,data=self.params)

    def __init__(self,env="DEMO",dataFile=r"E:\pythonWorkspace\mcah5\TestCase\TestCaseSuit.xlsx"):
        LogFileHelper.logging.info(u"=====================================start loginlite")
        print dataFile,env
        self.requestOne = RequestHelper(env=env,server='auth')
        self.url = "/auth-server/api/jwt/pwd/login"
        if not os.path.exists(dataFile):
            LogFileHelper.logging.error('测试用例文件不存在！！！')
            sys.exit()
        testCase = xlrd.open_workbook(dataFile)
        table = testCase.sheet_by_index(0)
        for i in range(1,table.nrows):
            self.num=int(table.cell(i,0).value)
            self.api=table.cell(i,1).value.replace('\n', '').replace('\r', '')
            self.host= table.cell(i,2).value.replace('\n', '').replace('\r', '')
            self.url = table.cell(i,3).value.replace('\n','').replace('\r','')
            self.method = table.cell(i, 4).value.replace('\n', '').replace('\r', '')
            self.params = eval(table.cell(i,5).value.replace('\n', '').replace('\r', ''))
            self.bodyJson = table.cell(i,6).value.replace('\n', '').replace('\r', '')
            self.headers = eval(table.cell(i, 7).value.replace('\n', '').replace('\r', ''))
            self.filePath = table.cell(i, 8).value.replace('\n', '').replace('\r', '')
            self.correlation = table.cell(i,9).value.replace('\n','').replace('\r','')
            self.requestOne.basicRequests(self.method,self.url,headers=self.headers,data=self.params)


    #
    # def getTestcase(self,dataFile):BU-MCA-SCDAIGR-019709-01
    #     if not os.path.exists(dataFile):
    #         LogFileHelper.logging.error('测试用例文件不存在！！！')
    #         sys.exit()
    #     testCase = xlrd.open_workbook(dataFile)
    #     table = testCase.sheet_by_index(0)
    #     for i in range(1,table.nrows):
    #         self.num=table.cell(i,0).value
    #         self.api=table.cell(i,1).value
    #         self.params= table.cell(i,2).value
    #         self.headers = table.cell(i, 3).value
    #         self.expectResponse=table.cell(i, 4).value
    #         print self.num,self.api,self.params,self.headers,self.expectResponse

    def login(self):
        if self.requestOne.status_code == 200:
            print self.requestOne.response['content']['authenticationJwt']
            return self.requestOne.response['content']['authenticationJwt']

        else:
            print "fail"
            return None

if __name__=="__main__":
    login = Login("demo")
    # login.getTestcase("E:\pythonWorkspace\mcah5\TestCase\TestCaseSuit.xlsx")
    jwt = login.login()



