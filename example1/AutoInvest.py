#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Author:moon.shan

from common import LogFileHelper
from common.ResquestHelper import RequestHelper
import json

class AutoInvest():
    def __init__(self,env='demo'):
        LogFileHelper.logging.info("Start invotest================")
        self.loanId = 790959
        self.req = RequestHelper(env=env,server="fincore")

    #自动募集
    def test_autoInvest(self,loanId):
        self.url = "/exposeService/service/autoInvest/%s"%loanId;
        self.req.basicRequests("post",self.url)
        return self.req.response

    #自动放款
    def test_autoLoan(self,loanId):
        self.url = "/exposeService/service/hourly/%s"%loanId;
        self.req.basicRequests("post",self.url)
        print self.req.response
        return self.req.response

    #查看还款计划
    def test_paymentPlan(self,loanId):
        self.url = "/exposeService/service/payment_plan/submitted/%s"%loanId;
        self.req.basicRequests("get",self.url)

        print self.req.response
        billList = self.req.response['content']['bills']
        return billList

    #生成每期账单
    def test_paymentDate(self,loanId,dueDate):
        self.url="/exposeService/service/NewPaymentScheduler/loanId/%s/paymentDate/%s"%(loanId,dueDate)
        self.req.basicRequests('post',self.url)
        print json.dumps(self.req.response,)

    #还款
    def test_repayment(self,loanId,dueDate):
        # for value in paymentDate:
        #     dueDate2 = value.get("dueDate","")
        self.url = "/exposeService/service/NewPaymentProcessor/loanId/%s/paymentDate/%s"%(loanId,dueDate)
        self.req.basicRequests('post',self.url)
        print self.req.response


    #循环还清每笔账单
    def test_allRepayment(self,loanId,planDates):
        self.count=0
        for planDate in planDates:
            dueDate = planDate.get("dueDate","")
            # print dueDate,
            # self.count+=1
            # print self.count

            self.test_paymentDate(loanId,dueDate)
            self.test_repayment(loanId, dueDate)






if __name__=='__main__':
    loanId = 790326
    invest = AutoInvest()
    # invest.autoInvest(loanId)
    # invest.test_autoLoan(loanId)
    plan=invest.test_paymentPlan(loanId)
    invest.test_allRepayment(loanId,plan)
