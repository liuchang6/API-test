#coding:utf-8
'''
启动脚本入口
'''
from AnalysisJmeter import Analysis
from MockRequest import *
from ReplaceVariables import Config
from Excle import *
from Email import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')

__dir__ = os.path.dirname(os.path.abspath(__file__))

def get_all_file():
     l = os.listdir(__dir__+'/jmeter')
     file_list = [i for i in l if '.jmx' in i]
     return file_list

def data(file):
    config_file = __dir__+"/variable.ini"
    data = {}
    a = Analysis(file)
    data['url'] = a.get_url()
    data['method'] = a.get_method()
    data['headers'] = a.get_headers()
    data['param'] = a.get_post_data()
    data['name'] = a.get_casename()
    r = Config(config_file)
    data['param'] = r.check(data['param'])
    data['headers'] = r.check(data['headers'])
    data['token'] = r.get_authorization(data['headers'])
    data['hope'] = '{}'
    data['result'] = 'n'
    return data

if __name__ == "__main__":
    file_list = get_all_file()
    id = 1
    l = []
    for i in file_list:
        logging.info(u'打开jmter脚本：' + i)
        print i
        d= data(i)
        if d['method'] == 'POST':
            b = MockRequest()
            result = b.requests_post(d['url'],d['headers'],d['param'])[0].encode('utf-8')
            d['time'] ='%.2f' % b.requests_post(d['url'],d['headers'],d['param'])[1]
            d['actual'] = result
            d['id'] = '00'+str(id)
            id=id+1

        l.append(d)
    workbook = xlsxwriter.Workbook(__dir__ + '/report/test.xlsx')
    worksheet = workbook.add_worksheet('测试概况')
    worksheet1 = workbook.add_worksheet("测试详情")
    init(workbook, worksheet)
    base(workbook, worksheet1)
    temp = 3
    for i in l:
        add_data(workbook, worksheet1, i,temp)
        temp = temp+1

    workbook.close()
    Email('test.xlsx')

