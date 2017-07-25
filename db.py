#coding:utf-8
import MySQLdb
import types
from AnalysisJmeter import Analysis
from MockRequest import MockRequest
from ReplaceVariables import Config
import os
__dir__ = os.path.dirname(os.path.abspath(__file__))
# 获取字典中的objkey对应的值，适用于字典嵌套
# dict:字典
# objkey:目标key
# default:找不到时返回的默认值
def dict_get(dict, objkey, default):
    tmp = dict
    for k, v in tmp.items():
        if k == objkey:
            return v
        else:
            if type(v) is types.DictType:
                ret = dict_get(v, objkey, default)
                if ret is not default:
                    return ret
    return default

class ZebrarunDB():

    def __init__(self):
        config_path = __dir__+"/config/db.ini"
        c = Config(config_path)
        self.con= MySQLdb.connect(
                host=c.get_zebrarunDB('host'),
                port = int(c.get_zebrarunDB('port')),
                user=c.get_zebrarunDB('user'),
                passwd=c.get_zebrarunDB('passwd'),
                db = c.get_zebrarunDB('db'),
                )

    def select_code(self,p):
        cur = self.con.cursor()
        try:
            cur.execute("select code from verification_code where phone=%s" % p)
            l =cur.fetchall()[-1]
        except :
            pass
        cur.close()
        return l

db = ZebrarunDB()
a = Analysis('/token/driver_verifycode.jmx')
h = a.get_headers()
u = a.get_url()
d =a.get_post_data()
mr = MockRequest()
result = mr.requests_post(u, h, d)[0].encode('utf-8')

v = db.select_code('15827628139')
print v
a = Analysis('/token/driver_login.jmx')
h = a.get_headers()
u = a.get_url()
d =a.get_post_data()
m = MockRequest()
d['verify_code'] = v[0]
print d
result1 = m.r_json(u, h, d)
print result1['msg']
ret=dict_get(result1, 'token', None)
print '手机15827628139的token：\n',ret
c=Config(__dir__+'/variable.ini')
c.get('Authorization','value',ret)
c.write(open(__dir__+'/variable.ini', "w"))
