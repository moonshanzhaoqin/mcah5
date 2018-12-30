#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Author:moon.shan
import common.LogFileHelper
from common.ResquestHelper import RequestHelper
from bussiness.Login import Login
from bussiness.GetLegalPersonAid import GetLegalPersonAid
import json
class RelationCompany():
    def __init__(self,env = None):
        self.relationReq = RequestHelper("demo","borrowapi")

    def relationCompany(self,jwt,aid):
        self.url = "/gw/borrow-api/v3/borrowers/%s/relative-users?relationType=IS_LEGAL_REP"%aid
        self.headers={'Authorization':jwt}
        # self.params = {"relationType":"IS_LEGAL_REP"}
        self.relationReq.basicRequests('get',self.url,headers=self.headers)
        print json.dumps(self.relationReq.response,ensure_ascii=False)
        print (len(self.relationReq.response))
        # for jb in self.relationReq.response:
        #     return jb
        print self.relationReq.response[0]["id"]

        return self.relationReq.response[0]["id"]


if __name__=="__main__":
    login = Login()
    jwt = login.login()
    selfinfo = GetLegalPersonAid()
    aid = selfinfo.selfInformation(jwt)
    relatitonCom = RelationCompany()
    companyId = relatitonCom.relationCompany(jwt,aid)
    print companyId
