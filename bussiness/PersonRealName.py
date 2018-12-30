#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Author:moon.shan
import common.LogFileHelper
from bussiness.GetLegalPersonAid import GetLegalPersonAid
from bussiness.Login import Login
from common.ResquestHelper import RequestHelper
class PersonRealName():
    def __init__(self,env="demo"):
        self.requestOne = RequestHelper("demo", "borrowapi")
        self.ssn = 420322198706285700;
        self.name = "单小丽";

    def personRealName(self,jwt,aid):
        self.headers = {'Authorization': jwt}
        self.Url="/gw/borrow-api/v3/borrowers/%s/real-name?productCode=MCA_GREENLANE_ONLINE&ssn=%s&permanentAddr=undefined&name=u'%s'"%(aid,self.ssn,self.name)
        self.requestOne.basicRequests(method="put",suburl=self.Url,headers=self.headers)
        self.response =self.requestOne.response
        return self.response





if __name__=="__main__":
    login = Login()
    jwt = login.login()
    selfInfo = GetLegalPersonAid()
    aid = selfInfo.selfInformation(jwt)
    realName = PersonRealName()
    realName.personRealName(jwt,aid)

