#coding:utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

__dir__ = os.path.dirname(os.path.abspath(__file__))

file_list = os.listdir(__dir__+'/jmeter')
result = []
for i in file_list:
    print i