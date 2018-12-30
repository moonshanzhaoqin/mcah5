#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Author:moon.shan


from bussiness.GetLegalPersonAid import GetLegalPersonAid
from bussiness.Login import Login
from common.ResquestHelper import RequestHelper


class GetLegalPersonContracts():
    def __init__(self,env=None):
        self.params = {"phase":"REALNAME","owner":"COMMON_RONGLI"}

    def getLegalPersonContracts(self,jwt,aid):
        self.headers = {"Authorization":jwt}
        self.url = "/gw/borrow-api/v3/borrowers/%s/phase-contracts"%aid
        self.reqOne = RequestHelper("demo","borrowapi")
        self.reqOne.basicRequests("get",self.url,params=self.params,headers=self.headers)
        return self.reqOne.response

if __name__=="__main__":
    login = Login()
    jwt = login.login()
    selfInfo = GetLegalPersonAid()
    aid = selfInfo.selfInformation(jwt)
    contracts = GetLegalPersonContracts("demo")
    legalPersonContracts = contracts.getLegalPersonContracts(jwt,aid)