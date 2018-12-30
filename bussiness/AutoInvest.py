#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Author:moon.shan
from common.ResquestHelper import RequestHelper

class AutoInvest():
    def __init__(self,env = "DEMO"):
        self.req = RequestHelper(env=env,server="fincore")

    def autoInvest(self,loanId):
        self.url = "/exposeService/service/autoInvest/%s"%loanId
        self.req.basicRequests("post",self.url)
        print self.req.response
if __name__=="__main__":
    loanId =1222;
    invest = AutoInvest()
    invest.autoInvest(loanId)