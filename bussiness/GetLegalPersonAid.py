#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Author:moon.shan
from common.ResquestHelper import RequestHelper
#from common.LogFileHelper import LogFileHelper
from bussiness.Login import Login
import time



class GetLegalPersonAid():
    def __init__(self,env = "DEMO"):
        self.subUrl = "/gw/borrow-api/v3/borrowers/self"
        self.reqOne = RequestHelper(env=env,server="borrowapi")

    def selfInformation(self,jwt):
        self.headers = {'Authorization':jwt}
        time.sleep(5)
        self.reqOne.basicRequests("get", self.subUrl,headers = self.headers)
        print self.reqOne.response['id']
        return self.reqOne.response['id']

if __name__ == "__main__":
    jWT = Login()
    jWToken = jWT.login()
    selfInfo = GetLegalPersonAid()
    selfInfo.selfInformation(jWToken)




