# !/usr/bin/env python
# coding=utf8
# Blog：https://www.bstester.com/2015/08/interface-test-automation-scheme-details

import json
import requests
import re
from common import LogFileHelper
import os, sys

try:
    import xlrd
except:
    os.system('pip install -U xlrd')
    import xlrd
# 获取并执行测试用例
def runTest(testCaseFile):
    print testCaseFile
    if not os.path.exists(testCaseFile):
        LogFileHelper.logging.error('测试用例文件不存在！！！')
        sys.exit()
    testCase = xlrd.open_workbook(testCaseFile)
    table = testCase.sheet_by_index(0)
    errorCase = []
    correlationDict = {}
    correlationDict["token"]=None
    correlationDict["aid"]=None
    for i in range(1, table.nrows):
        if table.cell(i, 11).value.replace('\n', '').replace('\r', '') != 'Yes':
            continue
        #params:num, APIPurpose, baseURL, subURL, requestMethod, requesBodyData, requesBodyJSON, headers, filePath, correlation, checkPoint,active
        num = str(int(table.cell(i, 0).value))
        APIPurpose = table.cell(i, 1).value.replace('\n', '').replace('\r', '')
        baseURL = table.cell(i, 2).value.replace('\n', '').replace('\r', '')
        subURL = table.cell(i, 3).value.replace('\n', '').replace('\r', '')
        requestMethod = table.cell(i, 4).value.replace('\n', '').replace('\r', '')
        requesBodyData = eval(table.cell(i, 5).value.replace('\n', '').replace('\r', ''))
        requesBodyJSON = json.dumps(table.cell(i, 6).value.replace('\n', '').replace('\r', ''))
        headers = eval(table.cell(i, 7).value.replace('\n', '').replace('\r', ''))
        filePath = table.cell(i, 8).value.replace('\n', '').replace('\r', '')
        correlation = table.cell(i, 9).value.replace('\n', '').replace('\r', '').split(';')
        checkPoint = table.cell(i, 10).value.replace('\n', '').replace('\r', '')

        for key in correlationDict:
            print correlationDict
            if subURL.find(key) > 0:
                subURL = subURL.replace(key, str(correlationDict[key]))
        headers['token']= correlationDict['token']
        status, resp = interfaceTest(num, APIPurpose, baseURL, subURL, requestMethod, requesBodyData, requesBodyJSON, headers, filePath,checkPoint)
        if status != 200:
            errorCase.append((num + ' ' + APIPurpose, str(status),  baseURL + subURL, resp))
            continue
        for j in range(len(correlation)):

            param = correlation[j].split('=')
            if len(param) == 2:
                if param[1] == '' or not re.search(r'^\[', param[1]) or not re.search(r'\]$', param[1]):
                    LogFileHelper.logging.error(num + ' ' + APIPurpose + ' 关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！')
                    continue
                value = resp
                for key in param[1][1:-1].split(']['):
                    try:
                        temp = value[int(key)]
                    except:
                        try:
                            temp = value[key]
                        except:
                            break
                    value = temp
                correlationDict[param[0]] = value
    return errorCase


# 接口测试
def interfaceTest(num, APIPurpose, baseURL, subURL, requestMethod, requesBodyData, requesBodyJSON, headers, filePath,checkPoint):
    if requestMethod.upper() == 'POST':
        print headers,requesBodyData,requesBodyJSON,baseURL+subURL
        if not requesBodyData is None:
            data = requesBodyData
            res = requests.post(url=baseURL + subURL, data=data, headers=headers, verify=False)
        else:
            data=requesBodyJSON
            res = requests.post(url=baseURL + subURL, josn=data, headers=headers, verify=False)

    elif requestMethod.upper() == 'GET':
        res=requests.get(url=baseURL+subURL, params=None, headers=headers, verify=False)
    else:
        LogFileHelper.logging.error(num + ' ' + APIPurpose + ' HTTP请求方法错误，请确认[Request Method]字段是否正确！！！')
        return 400, requestMethod
    response = res.json()
    status = res.status_code


    if status == 200:
        if re.search(str(checkPoint),str(response)):
            print num,APIPurpose,status,checkPoint
            LogFileHelper.logging.info(num + ' ' + APIPurpose + ' 成功, '.decode("utf-8") + str(status) + ', ' + str(response))
            return status, response
        else:
            LogFileHelper.logging.error(num + ' ' + APIPurpose + ' 失败！！！, [ ' + str(status) + ' ], ' + str(response))
            return 2001, response
    else:
        LogFileHelper.logging.error(num + ' ' + APIPurpose + ' 失败！！！, [ ' + str(status) + ' ], ' + str(response))
        return status, response


def main():
    errorTest = runTest('../TestCase/TestCaseSuit.xlsx')
    print len(errorTest)
    html = '接口自动化定期扫描，共有 ' + str(len(errorTest)) + ' 个异常接口，列表如下：' + ''
    print html
    if len(errorTest) > 0:

        print len(errorTest)
        for test in errorTest:
            html = html + ''
            html = html + '<table><tbody><tr><th style="width:100px;">接口</th><th style="width:50px;">状态</th><th style="width:200px;">接口地址</th><th>接口返回值</th></tr><tr><td>' + \
               test[0] + '</td><td>' + test[1] + '</td><td>' + test[2] + '</td><td>' + test[
                   3] + '</td></tr></tbody></table>'

if __name__ == '__main__':
    main()