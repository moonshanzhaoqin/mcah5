#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Author:moon.shan

import logging
from datetime import datetime
logName = "E:\\pythonWorkspace\\mcah5\\log\\app"+str(datetime.now())[0:10]+".log"
format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
datefmt="%a, %d %b %Y %H:%M:%S"
logging.basicConfig(filename=logName, level=logging.INFO,format=format)


