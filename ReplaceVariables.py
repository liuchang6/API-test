#coding:utf-8
'''
创建者：liu
作用：将jmeter中的变量替换成配置文件的参数。
使用方法：
创建日期：2017/7/20
'''

from ConfigParser import ConfigParser,SafeConfigParser
import os

__dir__ = os.path.dirname(os.path.abspath(__file__))

class Config(ConfigParser,SafeConfigParser):

    def __init__(self,config_file):
        ConfigParser.__init__(self)
        self.cp = SafeConfigParser()
        self.cp.read(config_file)

    def set(self,key,value,new):
        return self.cp.set(key,value,new)

    def get_zebrarunDB(self,value):
        return self.cp.get('ZebrarunDB' ,value)

    def get_authorization(self,header):
        '''
        获取配置文件的'Authorization'的值
        :return:
        '''

        for i in header.keys():
            if 'Authorization' in i:
                if '${' in header['Authorization']:
                    return self.cp.get('Authorization','value')
                else:
                    return header['Authorization']
        return u'无'

    def get_a(self):
        return self.cp.get('Authorization', 'value')

    def get_ownerPhone(self):
        '''
        获取配置文件的'ownerPhone'的值
        :return:
        '''
        return self.cp.get('ownerPhone','value')

    def check(self,dict):
        '''

        :param dict: 传入发送的header或者post的json数据
        :return: 如果数据里面有变量，就用配置文件的字段去替代
        '''
        for i in dict:
            if '${' in str(dict[i]):
                if 'Authorization' in str(dict[i]):
                    dict[i] = self.get_authorization(dict)
                if 'ownerPhone' in str(dict[i]):
                    dict[i] = self.get_ownerPhone()
        return dict