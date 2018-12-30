#!/usr/local/bin/python
#coding:utf-8
# @Author:moon.shan

import requests
import json
from requests import Request
from common import Setting
from common import LogFileHelper
class RequestHelper():
    def __init__(self,env=None,server=None):
        self.env=env.upper()
        if server:
            self.base_url = Setting.Settings[self.env]["URL"][server]
            print self.base_url
        else:
            self.base_url=""
    #
    # def getRequest(self,suburl,params=None,headers=None):
    # # def getRequest(self, suburl, **kwargs):
    #     LogFileHelper.logging.info("-"*50+"post params"+"-"*50)
    #     # arguments = kwargs.get("params") or kwargs.get("data") or kwargs.get("json") or kwargs.get("file") or kwargs.get("headers") or {}
    #     # self.req = requests.get(url=self.base_url+suburl,params=arguments,headers=arguments,verify=False)
    #     self.req = requests.get(url=self.base_url + suburl, params=params, headers=headers, verify=False)
    #     LogFileHelper.logging.info("url=="+self.base_url+suburl)
        # LogFileHelper.logging.info(arguments)
    #
    #
    # def postRequest(self,suburl, data = None, json=None, headers = None,files=None):
    #     LogFileHelper.logging.info("-"*50+"post params"+"-"*50)
    #     self.req = requests.post(url=self.base_url + suburl, json=json, data=data, headers=headers,files=files, verify=False)
    #     LogFileHelper.logging.info("url=="+self.base_url+suburl)
    #     LogFileHelper.logging.info(headers)
    #     LogFileHelper.logging.info(json)
    #     LogFileHelper.logging.info(data)
    #     LogFileHelper.logging.info(files)
    #
    #
    # def putRequest(self,suburl , data = None,json=None, headers = None):
    #     LogFileHelper.logging.info("-"*50+"post params"+"-"*50)
    #     self.req = requests.put(url =  self.base_url+suburl, json = json, data=data,headers = headers,verify=False)
    #     LogFileHelper.logging.info("url==" + self.base_url + suburl)
    #     LogFileHelper.logging.info(headers)
    #     LogFileHelper.logging.info(json)
    #     LogFileHelper.logging.info(data)



    # def basicRequests(self,method = None, suburl = None,json=None, data = None, headers = None, params = None,files=None):
    #     # print type(data)
    #     if method.lower() == "get":
    #         self.getRequest(suburl = suburl, params = params, headers = headers)
    #     if method.lower() == "post":
    #         self.postRequest(suburl = suburl,data = data,json=json, files=files, headers = headers)
    #
    #     if method.lower() == "put":
    #         self.putRequest(suburl = suburl, data = data,json =json, headers = headers)
    #         if not self.req.text:
    #             return self.req
    #         else:
    #             return self.req.json()
    #
    #
    #
    #     #print self.req.content
    #     LogFileHelper.logging.info(self.req.content)
    #     self.response =self.req.json()
    #     self.status_code = self.req.status_code


    def basicRequests(self,method,suburl, **kwargs):
        # method,suburl=args
        # arguments = kwargs.get("params") or kwargs.get("data") or kwargs.get("json") or kwargs.get("file") or kwargs.get("headers") or {}

        if method.lower() == "get":
            self.req = requests.get(self.base_url + suburl, verify=False,**kwargs)
            # self.getRequest(suburl,**kwargs)
            LogFileHelper.logging.info("url=="+self.base_url+suburl)
            LogFileHelper.logging.info(kwargs.get("headers"))
            LogFileHelper.logging.info(kwargs.get("params"))

        if method.lower() == "post":
            self.req = requests.post(self.base_url + suburl,verify=False, **kwargs)
            LogFileHelper.logging.info("url==" + self.base_url + suburl)
            LogFileHelper.logging.info(kwargs.get("headers"))
            LogFileHelper.logging.info(kwargs.get("json"))
            LogFileHelper.logging.info(kwargs.get("data"))
            LogFileHelper.logging.info(kwargs.get("file"))


        if method.lower()=="put":
            self.req = requests.put(self.base_url + suburl, verify=False,**kwargs)
            LogFileHelper.logging.info("url==" + self.base_url + suburl)
            LogFileHelper.logging.info(kwargs.get("headers"))
            LogFileHelper.logging.info(kwargs.get("json"))
            LogFileHelper.logging.info(kwargs.get("data"))

        if method.lower()=="options":
            self.req = requests.options(self.base_url+suburl,verify=False,**kwargs)

        if method.lower()=="delete":
            pass

        self.status_code = self.req.status_code
        print self.req.text
        print self.req.json()
        LogFileHelper.logging.info(self.req.text)

        if self.req.text:
            self.response = self.req.json()
            return self.req.json()
        else:
            return self.req






if __name__=='__main__':

    r = RequestHelper(env="DEMO")
    paramsOne = {"identity": "15121000080", "password": "welcome1"}
    headers = {"Content-Type": "application/x-www-form-urlencoded", "X-Role": "BORROWER"}
    res=r.basicRequests("post", "/auth-server/api/jwt/pwd/login", data=paramsOne,headers=headers)
    print res



