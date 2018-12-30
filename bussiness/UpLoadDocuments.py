#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Author:moon.shan
from bussiness.Login import Login
from common.ResquestHelper import RequestHelper
import json

class UpLoadDocuments():
    def __init__(self):
        self.Req = RequestHelper("demo", "borrowapi")
        self.headers = {}

    def upLoadDocuments(self,jwt,companyId,loanAppId):
        self.headers["Authorization"]=jwt
        self.updataFiles = ["SV_APP_ORIGINAL_BUSINESS_LICENSE","SV_LEGAL_REPRESENTATIVE_IDENTITY_CARD"]

        for updataFile in self.updataFiles:
            print type(updataFile)
            self.param = {"docType": updataFile}
            self.files = {'uploadedFiles': ("1.jpg", open("C:\\1.jpg", 'rb'), "images/jpg")}
            self.url = "/gw/zuul/borrow-api/v3/borrowers/%s/applications/%s/documents/" %(companyId, loanAppId)
            self.Req.basicRequests("post",self.url,files=self.files,headers=self.headers,data=self.param)
            print self.Req.response

if __name__=="__main__":
    loanAppId = 6000036356
    companyid = 17132333
    login = Login()
    jwt = login.login()
    upLoad =  UpLoadDocuments()
    upLoad.upLoadDocuments(jwt,companyid,loanAppId)


