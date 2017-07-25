#coding:utf-8
'''
创建者：liu
作用：发送邮件，附带附件
使用方法：调用方法，传入要发送的excle附件。
创建日期：2017/7/21
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import sys
from log import *
import logging
reload(sys)
sys.setdefaultencoding("utf8")

__dir__ = os.path.dirname(os.path.abspath(__file__))

def Email(report):
    username = 'liuchang_bmkp@163.com'
    password = "Liu7792049"
    sender = 'liuchang_bmkp@163.com'
    #'zhaowenya_bmkp@163.com'
    receivers = ','.join(['liuchang_bmkp@163.com'])

    msg = MIMEMultipart()
    msg['Subject'] = '接口测试结果'
    msg['From'] = sender
    msg['To'] = receivers

    t = '结果见附件'

    puretext = MIMEText(t,'plain','utf-8')
    puretext["Accept-Language"] = "zh-CN"
    puretext["Accept-Charset"] = "ISO-8859-1,utf-8"
    msg.attach(puretext)

    xlsxpart = MIMEApplication(open(__dir__+'/report/'+report, 'rb').read())
    xlsxpart.add_header('Content-Disposition', 'attachment', filename='test.xlsx')
    msg.attach(xlsxpart)
    try:
        client = smtplib.SMTP()
        client.connect('smtp.163.com')
        client.login(username, password)
        client.sendmail(sender, receivers, msg.as_string())
        client.quit()
        logging.info(u'邮件发送成功')
    except smtplib.SMTPRecipientsRefused:
        logging.error(u'邮件发送失败：RecipientsRefused')
    except smtplib.SMTPAuthenticationError:
        logging.error(u'邮件发送失败：AuthenticationError')
    except smtplib.SMTPSenderRefused:
        logging.error(u'邮件发送失败：SenderRefused')
    except smtplib.SMTPException,e:
        logging.error(u'邮件发送失败：%s' % e.message)
