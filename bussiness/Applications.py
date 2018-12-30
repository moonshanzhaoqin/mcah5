#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Author:moon.shan
from common.ResquestHelper import RequestHelper
import common.LogFileHelper
from bussiness.Login import Login
from bussiness.GetLegalPersonAid import GetLegalPersonAid
from bussiness.RelationCompany import RelationCompany
from bussiness.GetLegalPersonContracts import GetLegalPersonContracts
from bussiness.GetCompanyContracts import GetCompanyContracts
import json
import os
import sys
from common import LogFileHelper
import xlrd
import re
class Applications():
    def __init__(self,env = "DEMO",testData='../TestCase/TestCaseSuit.xlsx'):
        self.reqOne = RequestHelper(env=env,server="borrowapi")
        # self.productCode = "BU-MCA-DSDAITF-000000-02"
        # self.productCode = "BU-MCA-SCDAIGF-000000-02"
        # C版本
        self.productCode = "BU-MCA-SCDAIGR-019709-01"
        self.headers = {"Content-Type": "application/json","X-Role":"BORROWER"}
        self.AppAmount = 20000
        if not os.path.exists(testData):
            LogFileHelper.logging.info("测试数据不存在")
            sys.exit()
        table = xlrd.open_workbook(testData)
        tableSheet = table.sheet_by_index(1)
        self.applicationData= eval(tableSheet.cell(1,1).value.replace('\n', '').replace('\r', ''))
        self.configsData = eval(tableSheet.cell(2,1).value.replace('\n', '').replace('\r', ''))
        self.updataFilesData = None
        self.getMaterialsData = eval(tableSheet.cell(4,1).value.replace('\n', '').replace('\r', ''))
        self.putMaterialsData = eval(tableSheet.cell(5,1).value.replace('\n', '').replace('\r', ''))


    def application(self,jwt,aid):
        self.url="/gw/borrow-api/v3/borrowers/%s/applications"%aid
        self.data= self.applicationData
        print self.data,type(self.data)
        self.headers['Authorization'] = jwt
        self.reqOne.basicRequests('post', self.url, headers=self.headers,json=self.data)
        print self.reqOne.response
        return self.reqOne.response["loanAppId"]


    def configs(self,jwt,aid,loanAppId,companyId):
        print companyId
        print "-----------------------------------"
        self.url="/gw/borrow-api/v3/borrowers/%s/applications/%s/configs"%(aid,loanAppId)
        self.headers['Authorization'] = jwt
        self.data = self.configsData
        self.reqOne.basicRequests('put', self.url, headers=self.headers, json=self.data)
        print  self.reqOne.response
        return self.reqOne.response


    def upLoadDocuments(self,jwt,aid,loanAppId):
        self.headers={"Authorization":jwt}
        self.updataFiles = ["SV_APP_ORIGINAL_BUSINESS_LICENSE","SV_LEGAL_REPRESENTATIVE_IDENTITY_CARD","SV_LEGAL_REPRESENTATIVE_IDENTITY_CARD"]
        for updataFile in self.updataFiles:
            self.param = {"docType": updataFile}
            self.files = {'uploadedFiles': ("1.jpg", open("C:\\1.jpg", 'rb'), "images/jpg")}
            self.url = "/gw/zuul/borrow-api/v3/borrowers/%s/applications/%s/documents/" % (aid, loanAppId)
            self.reqOne.basicRequests("post",self.url,data=self.param,files=self.files,headers=self.headers)
        return self.reqOne.response


    def getMaterials(self,jwt,aid,appid):
        url2 = "/gw/borrow-api/v3/borrowers/%s/applications/%s/materials"%(aid,appid)
        headers2 = {'Authorization': jwt}
        params2 = self.getMaterialsData
        self.reqOne.basicRequests("get",url2, headers=headers2, params=params2)
        print self.reqOne.response
        return self.reqOne.response


    def PutMaterials(self,jwt,aid,appid,initDataOne):
        self.url3 = "/gw/borrow-api/v3/borrowers/%s/applications/%s/materials?configCode=mcah5"%(aid,appid)
        self.headers['Authorization'] = jwt
        json33 = self.putMaterialsData
        print  type(initDataOne["data"])
        for key, value in initDataOne["data"].items():
            if isinstance(value, dict):
                for k, v in value.iteritems():
                    if v:
                        json33[key][k] = v
            elif isinstance(value, list):
                for index, a in enumerate(value):
                    for k, v in a.iteritems():
                        if v:
                            json33[key][index][k] = v
        # pprint.pprint(json33)

        print json33
        self.reqOne.basicRequests("put",self.url3,json=json33, headers=self.headers)
        print self.reqOne.response


if __name__=='__main__':
    login = Login('demo')
    jwt = login.login()
    selfInfo = GetLegalPersonAid()
    aid = selfInfo.selfInformation(jwt)
    relatitonCom = RelationCompany()
    companyId = relatitonCom.relationCompany(jwt, aid)
    contracts = GetCompanyContracts()
    companyContracts = contracts.getContracts(jwt, companyId)
    contracts = GetLegalPersonContracts("demo")
    legalPersonContracts = contracts.getLegalPersonContracts(jwt,aid)
    application = Applications()
    loanAppId = application.application(jwt,aid)
    inputParams = application.configs(jwt,aid,loanAppId,companyId)
    getLoanInfo = application.getMaterials(jwt, aid, loanAppId)
    inputLoanInfo = application.PutMaterials(jwt,aid,loanAppId,getLoanInfo)
    uploadFile = application.upLoadDocuments(jwt,aid,loanAppId)





