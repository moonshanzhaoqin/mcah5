#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Author:moon.shan
import common.LogFileHelper
from common.ResquestHelper import RequestHelper
from bussiness.Login import Login
from bussiness.GetLegalPersonAid import GetLegalPersonAid
from bussiness.RelationCompany import RelationCompany

class McaLoanable():
    def __init__(self,env="demo"):
        self.params = {"loanProductCode": "MCA_GREENLANE_ONLINE"}

    def loanAble(self,jwt,aid):
        self.url = "/gw/borrow-api/v3/companies/%s/mca-loanable"%aid
        self.headers = {'Authorization': jwt}
        self.loanReq = RequestHelper("demo","borrowapi")

        self.loanReq.basicRequests('get',self.url,params=self.params,headers=self.headers)
        print self.loanReq.response

if __name__=="__main__":
    loginOne  = Login("demo")
    jwt = loginOne.login()
    selfInfo = GetLegalPersonAid()
    aid =selfInfo.selfInformation(jwt)
    mcaLoanable = McaLoanable()
    company = RelationCompany()
    companyId = company.relationCompany(jwt,aid)
    loanable = mcaLoanable.loanAble(jwt,companyId)