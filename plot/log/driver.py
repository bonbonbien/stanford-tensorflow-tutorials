#!/usr/bin/env python
#coding:utf-8

# from builtins import Exception
import logging.config
import os
import sys
import re
import json
import time
from exceptions import Exception

reload(sys)
sys.setdefaultencoding('utf-8')

# cur_path = os.path.dirname(__file__)
cur_path = os.getcwd()
sys.path.append(os.path.abspath(os.path.join(cur_path, "../conf/")))

# import conf
import relation_conf as tc_conf

logging.config.fileConfig(os.path.abspath(os.path.join(cur_path, "../conf/log.conf")))
ilog_root = logging.getLogger('root')
ilog_info = logging.getLogger('info')
ilog_warn = logging.getLogger('warn')

# from logfmt import ilog as ilog_root, ilog as ilog_info, ilog as ilog_warn
