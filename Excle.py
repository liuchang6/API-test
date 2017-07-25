# -*- coding: utf-8 -*-
'''
创建者：liu
作用：制作excle
使用方法：workbook = xlsxwriter.Workbook(__dir__ + '/report/111.xlsx')
          worksheet = workbook.add_worksheet("测试总况")
          worksheet1 = workbook.add_worksheet("1111")
          base(workbook, worksheet)
          init(workbook,worksheet1)
          workbook.close()
创建日期：2017/7/21
'''
import xlsxwriter
import sys
from log import *
import logging
import os
reload(sys)
sys.setdefaultencoding('utf8')

__dir__ = os.path.dirname(os.path.abspath(__file__))

def get_format_center( workbook,num=2,color='white'):
    '''
    单元格增加格式，设置线宽
    :param workbook:
    :param num:
    :return:
    '''
    return  workbook.add_format({'align': 'center','valign': 'vcenter','border':num, 'bg_color':color })

def _write_center(worksheet, cl, data,  workbook,c = 'white'):
    '''
    单元个数据设置居中
    :param worksheet:
    :param cl: 单元格
    :param data:
    :param workbook:
    :return:
    '''

    return worksheet.write(cl, data, get_format_center( workbook,color=c))

def get_format( workbook, option={}):
    '''
    给单元格自定义格式
    :param workbook:
    :param option:
    :return:
    '''
    return  workbook.add_format(option)

def init(workbook,worksheet):
    '''
    总览概况sheet
    :param workbook:
    :param worksheet:
    '''
    worksheet.set_column("A:A", 15)
    worksheet.set_column("B:B", 20)
    worksheet.set_column("C:C", 20)
    worksheet.set_column("D:D", 20)
    worksheet.set_column("E:E", 20)
    worksheet.set_column("F:F", 20)

    worksheet.set_row(1, 30)
    worksheet.set_row(2, 30)
    worksheet.set_row(3, 30)
    worksheet.set_row(4, 30)
    worksheet.set_row(5, 30)

    define_format_H1 = get_format(workbook, {'bold': True, 'font_size': 18})
    define_format_H2 = get_format(workbook, {'bold': True, 'font_size': 14})
    define_format_H1.set_border(1)

    define_format_H2.set_border(1)
    define_format_H1.set_align("center")
    define_format_H2.set_align("center")
    define_format_H2.set_bg_color("blue")
    define_format_H2.set_color("#ffffff")

    worksheet.merge_range('A1:F1', '测试报告总概况', define_format_H1)
    worksheet.merge_range('A2:F2', '测试概括', define_format_H2)
    worksheet.merge_range('A3:A6', '这里放图片', get_format_center(workbook))
    worksheet.insert_image('A3:A6', __dir__+'/img/banma.png')

    _write_center(worksheet, "B3", '项目名称', workbook)
    _write_center(worksheet, "B4", '接口版本', workbook)
    _write_center(worksheet, "B5", '脚本语言', workbook)
    _write_center(worksheet, "B6", '测试网络', workbook)

    _write_center(worksheet, "C3", 'test_name', workbook)
    _write_center(worksheet, "C4", 'test_version', workbook)
    _write_center(worksheet, "C5", 'test_pl', workbook)
    _write_center(worksheet, "C6", 'test_net', workbook)

    _write_center(worksheet, "D3", "接口总数", workbook)
    _write_center(worksheet, "D4", "通过总数", workbook)
    _write_center(worksheet, "D5", "失败总数", workbook)
    _write_center(worksheet, "D6", "测试日期", workbook)

    _write_center(worksheet, "E3", 'test_sum', workbook)
    _write_center(worksheet, "E4", 'test_success', workbook)
    _write_center(worksheet, "E5", 'test_failed', workbook)
    _write_center(worksheet, "E6", 'test_date', workbook)
    _write_center(worksheet, "F3", "分数", workbook)

    worksheet.merge_range('F4:F6', '60', get_format_center(workbook))

def base( workbook,worksheet):
    '''
    测试详情表格头
    :param workbook:
    :param worksheet:
    '''
    worksheet.set_column("A:A", 20,)
    worksheet.set_column("B:B", 20)
    worksheet.set_column("C:C", 20)
    worksheet.set_column("D:D", 20)
    worksheet.set_column("E:E", 20)
    worksheet.set_column("F:F", 20)
    worksheet.set_column("G:G", 20)
    worksheet.set_column("H:H", 20)
    worksheet.set_column("I:I", 20)
    worksheet.set_column("J:J", 20)
    for i in range(1000):
        worksheet.set_row(i, 30)

    worksheet.merge_range('A1:J1', '测试详情', get_format(workbook, {'bold': True, 'font_size': 18, 'align': 'center', 'valign': 'vcenter', 'bg_color': 'blue','font_color': '#ffffff'}))

    _write_center(worksheet, "A2", '用例ID',workbook,c='#CFCFCF')
    _write_center(worksheet, "B2", '用例名称', workbook,c='#CFCFCF')
    _write_center(worksheet, "C2", '方法', workbook,c='#CFCFCF')
    _write_center(worksheet, "D2", 'URL', workbook,c='#CFCFCF')
    _write_center(worksheet, "E2", 'token', workbook,c='#CFCFCF')
    _write_center(worksheet, "F2", '参数', workbook,c='#CFCFCF')
    _write_center(worksheet, "G2", '预期值', workbook,c='#CFCFCF')
    _write_center(worksheet, "H2", '实际值', workbook,c='#CFCFCF')
    _write_center(worksheet, "I2", '响应时间', workbook,c='#CFCFCF')
    _write_center(worksheet, "J2", '测试结果', workbook,c='#CFCFCF')

def add_data(workbook,worksheet,data,temp):
    '''
    测试详情表格数据填写
    :param workbook:
    :param worksheet:
    :param data: 字典数据
    :param temp: 从第三行开始添加
    '''
    _write_center(worksheet, "A" + str(temp), data["id"], workbook)
    _write_center(worksheet, "B" + str(temp), data["name"], workbook)
    _write_center(worksheet, "C" + str(temp), data["method"], workbook)
    _write_center(worksheet, "D" + str(temp), data["url"], workbook)
    _write_center(worksheet, "E" + str(temp), data["token"], workbook)
    _write_center(worksheet, "F" + str(temp), str(data["param"]), workbook)
    _write_center(worksheet, "G" + str(temp), str(data["hope"]), workbook)
    _write_center(worksheet, "H" + str(temp), str(data["actual"]), workbook)
    _write_center(worksheet, "I" + str(temp), str(data["time"]), workbook)
    _write_center(worksheet, "J" + str(temp), str(data["result"]), workbook,c='red')

