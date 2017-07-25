#coding:utf-8
'''
创建者：liu
作用：从jmeter脚本中提取url，头文件，发送的json数据，发送的方法等
使用方法：实例化的时候传入jmeter脚本。
创建日期：2017/7/20
'''
import os
import re
import json
import sys
from log import *
import logging
reload(sys)
sys.setdefaultencoding('utf8')

__dir__ = os.path.dirname(os.path.abspath(__file__))
jmeter_path = __dir__+'/jmeter/'

class Analysis():

    def __init__(self,file):
        self.file = unicode(jmeter_path+file)

    def __get_value(self,keyvalue):
        '''
        return 正则匹配'>' '<'之间的值。
        '''
        con = self.__open_jmeter()
        patt = re.compile(r"\>(.*?)\<")
        l = [patt.findall(i)[0] for i in con if keyvalue in i]
        return l

    def __open_jmeter(self):
        '''
        :return: jmeter脚本读取的文本
        '''
        try:
            with open(self.file,'r') as f:
                con = f.readlines()
                return con
        except:
            logging.error(u'jmeter脚本打开错误')
            logging.info(u'退出执行py脚本')
            exit()


    def get_headers(self):
        '''

        :return: 请求头信息
        '''
        headers_key = self.__get_value('<stringProp name="Header.name">')
        headers_value = self.__get_value('<stringProp name="Header.value">')
        headers = {}
        for i in range(len(headers_value)):
            headers[headers_key[i]] = headers_value[i]
        logging.info(u'提取头文件')
        return headers

    def get_casename(self):
        '''

        :return: 线程组名字
        '''
        con = self.__open_jmeter()
        for i in con:
            if 'guiclass="ThreadGroupGui"' in i:
                if 'testname' in i:
                    l = i.strip(' ')
        name = l.split(' ')[3].split('=')[1].strip('"')
        logging.info(u'提取名字')
        return name

    def get_method(self):
        '''

        :return: 请求的方法
        '''
        method = self.__get_value('<stringProp name="HTTPSampler.method">')[0]
        logging.info(u'提取方法')
        return method

    def get_url(self):
        '''

        :return: 请求的url
        '''
        IP = self.__get_value('<stringProp name="HTTPSampler.domain">')[0]
        path = self.__get_value('<stringProp name="HTTPSampler.path">')[0]
        protocol = self.__get_value('<stringProp name="HTTPSampler.protocol">')[0]
        url = protocol+'://'+IP+path
        logging.info(u'提取url')
        return url

    def get_post_data(self):
        '''

        :return: 发送的json数据
        '''
        con = self.__open_jmeter()
        for i in con:
            if '<stringProp name="Argument.value">' in i:
                index1 = con.index(i)
            if '<stringProp name="Argument.metadata">' in i:
                index2 = con.index(i)
        p = [i.replace('&quot;','"') for i in con[index1:index2]]
        p1 = ''.join([i.replace('&#xd;\n', '') for i in p])
        patt1 = re.compile("\{(.*)\}", )
        data = '{'+patt1.findall(p1)[0]+'}'
        logging.info(u'提取post数据')
        return eval(data)

#a = Analysis('14queryActionCenter_7.jmx')
#print a.get_method()
#print a.get_url()
#print a.get_headers()
#print a.get_casename()
#print a.get_post_data()
