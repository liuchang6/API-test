#coding:utf-8
'''
创建者：liu
作用：配置log输出样式
创建日期：2017/7/21
'''

import logging
import os

__dir__ = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=__dir__+'\log\d.log',
                    filemode='w')
