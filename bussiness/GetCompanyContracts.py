#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Author:moon.shan

import common.LogFileHelper
from common.ResquestHelper import RequestHelper
from bussiness.Login import Login
from bussiness.GetLegalPersonAid import GetLegalPersonAid
from bussiness.RelationCompany import RelationCompany
from bussiness.GetLegalPersonAid import GetLegalPersonAid

class GetCompanyContracts():
    def __init__(self,env = "Demo"):
        self.params = {"phase":"REALNAME","owner": "COMMON_RONGLI"}
    def getContracts(self,jwt,companyId):
        self.url= "/gw/borrow-api/v3/borrowers/%s/phase-contracts"%companyId
        self.headers = {"Authorization":jwt}
        self.reqOne = RequestHelper("demo","borrowapi")
        self.reqOne.basicRequests("get",self.url,params=self.params,headers=self.headers)
        return self.reqOne.response
if __name__=="__main__":
    login = Login()
    jwt = login.login()
    selfInfo = GetLegalPersonAid()
    aid = selfInfo.selfInformation(jwt)
    company = RelationCompany()
    companyId = company.relationCompany(jwt,aid)

    contracts = GetCompanyContracts()
    companyContracts = contracts.getContracts(jwt,companyId)