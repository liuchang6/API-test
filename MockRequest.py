#coding:utf-8
'''
创建者：liu
作用：模拟发送请求，获取返回值
使用方法：调用方法，传入请求的url，头信息，发送的json数据。
创建日期：2017/7/20
'''

import requests
import json
import time
import os
import re

__dir__ = os.path.dirname(os.path.abspath(__file__))

def use_time(fun):
    '''

    :param fun: 函数
    :return: 修饰返回时间
    '''
    def wrapper(*args, **kwargs):
        t1 = time.time()
        t = fun(*args, **kwargs)
        t2 = time.time()
        return t, t2 - t1
    return wrapper

class MockRequest():
    '''
    发送请求，获取返回值
    '''
    @use_time
    def requests_post(self, url, header, datas):
        r = requests.post(url, headers=header, data=json.dumps(datas))
        return r.content

    def r_json(self, url, header, datas):
        r = requests.post(url, headers=header, data=json.dumps(datas))
        return r.json()