#conding = utf-8
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import time 
#执行用例
caselist = os.listdir('D:\\autotest\\PC\\testcase')#找到这个文件夹的路径
for a in caselist:
    s = a.split(".")[1]
    if s == "py":
        os.system('python D:\\autotest\\PC\\testcase\\%s 1>D:\\autotest\\PC\\log.txt 2>&1'%a)
        print("写入日志成功")


# time.sleep(3)
print('发送邮件')
sender = 'xxxxxx'
#接收邮箱
receiver = 'xxxxxxx'
#主题
subject = 'Lulutrip_PC AutoTest Report'
#邮箱服务器
smtpserver = 'xxxxxx'
#账号
username = 'xxxxxxxx'
password = 'xxxxxxxx'

file_report = 'D:\\autotest\\PC\\report\\result.html'
report = open(file_report,'rb')
new_report = report.read()
report.close()

msg = MIMEText(new_report,'html','utf-8')
msg['subject'] = Header(subject,'utf-8')
smtp = smtplib.SMTP(smtpserver,25)
smtp.connect('imap.exmail.qq.com')
smtp.login(username,password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()