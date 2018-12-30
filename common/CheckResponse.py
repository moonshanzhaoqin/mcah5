#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Author:moon.shan
from nose.tools import *
class CheckResponse():
    @staticmethod
    def check_result(response,params,expectNum=None):
        if expectNum is not None:
            eq_(expectNum,len(response.get("result")),'{0}!={1}'.format(expectNum,len(response['subjects'])))