from selenium import  webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select#应用下拉选择框控件
import unittest
import datetime
import HTMLTestRunner
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
# driver = webdriver.Chrome()
# url1 = "https://www.lulutrip.com"
# driver.get(url1)
# driver.maximize_window()
# driver.implicitly_wait(3)#只能等待3s

class Sendmail:
    def __init__(self):
        print('发送邮件')
        sender = 'xxxxxxx'
        #接收邮箱
        receiver = 'xxxxxxxx'
        #主题
        subject = 'Lulutrip_PC AutoTest Report'
        #邮箱服务器
        smtpserver = 'imap.exmail.qq.com'
        #账号
        username = 'xxxxxxx'
        password = 'xxxxxxxxxx'

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
class Open:
    #打开浏览器输入url
    def __init__(self):
        # self.driver = webdriver.Chrome() 
        # driver = self.driver 
        # #global driver    
        url1 = "https://www.lulutrip.com"
        driver.get(url1)
        driver.maximize_window()
        driver.implicitly_wait(3)#只能等待3s

class Login:
    def anniu(self,driver01):
        #登录
        self.driver = driver01
        driver = self.driver
        login = driver.find_element_by_class_name("default")
        login.click()
        now_time =str(datetime.datetime.now())
        print("%s"%now_time + ':' + "点击登录按钮")
        time.sleep(5)
    def account(self,number,password,driver01):
        self.driver = driver01
        driver = self.driver
        self.number = number
        self.password = password
        usr_name = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form[1]/div[1]/div/div[1]/input")
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "找到账户输入框")
        usr_name.clear()
        usr_name.click()
        usr_name.send_keys(self.number)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "输入账户")
        pwd = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form[1]/div[2]/div/div[1]/span/input")
        pwd.clear()
        pwd.click()
        pwd.send_keys(self.password)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "输入密码")
        remember = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form[1]/div[3]/div[1]/label/input")
        remember.click()
        submit = driver.find_element_by_class_name("comm-btn1")
        submit.click()
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "点击提交")
        time.sleep(5)
    def now_cookie(self,driver01):
        self.driver = driver01
        driver = self.driver
        cookie = driver.get_cookies()
        for a in cookie:
            cookie01 = list(a.values())
            if cookie01[0] == 'LuluUser':
                now_time =str(datetime.datetime.now())
                print('%s'%now_time + ':' + "当前的cookie是:%s"%a)
                #print("当前的cookie是:%s"%a)
                #break
    def juege_login(self,driver01):       
        self.driver = driver01
        driver = self.driver
        nickname = driver.find_element_by_xpath("//*[@id='topbar-common']/div/div[1]/div/span").text   
        if nickname == '你好，baozi.wu，路路行欢迎你！':
            now_time = datetime.datetime.now()
            print('%s'%now_time + ':' + '登录成功' + '%s'%nickname)
        else:
            print('%s'%now_time + ':' + "失败")
            driver.quit()
class Search:
    #搜索产品
    def search_input(self,code,driver01):
        self.driver = driver01
        driver = self.driver
        self.code = code
        #driver.get(url1)#回到首页
        search_inpt = driver.find_element_by_xpath("//*[@id='header-common']/div/div[2]/div[3]/div/div[2]/input")
        time.sleep(5)
        print("等待5s")
        search_inpt.send_keys(self.code)
        now_time = datetime.datetime.now()
        print('%s'%now_time + ':' + '输入产品编号')
        serch_btn = driver.find_element_by_xpath("/html/body/header/div/div[2]/div[3]/div/div[2]/a")
        serch_btn.click()
        now_time = datetime.datetime.now()
        print('%s'%now_time + ':' + '执行搜索')
        time.sleep(5)
    def juege_search(self,driver01):
        self.driver = driver01
        driver = self.driver
        book_name = driver.find_element_by_xpath("//*[@id='content']/div[3]/div/div[2]/div[2]/h3/span").text
        if book_name == '我要订购':
            now_time = str(datetime.datetime.now())
            print('%s'%now_time + ':' + '显示订购按钮，产品搜索成功')
        else:
            now_time = str(datetime.datetime.now())
            print('%s'%now_time + ':' + '未显示订购按钮，请核对产品信息...')
            driver.quit()
class Product:
    #产品详情页
    def second_month(self,driver01):
        self.driver = driver01
        driver = self.driver
        month = driver.find_element_by_xpath("//*[@id='content']/div[3]/div/div[1]/div[1]/div[1]/div/ul/li[2]")
        month.click()
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "切换到到期可售卖日期的第二个月份")
    def info_product(self,driver01):
        self.driver = driver01
        driver = self.driver
        time.sleep(3)
        data = driver.find_element_by_xpath("//*[@id='content']/div[3]/div/div[1]/div[1]/ul/li[28]")
        data.click()
        now_data = data.text
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + '选择出发日期%s'%now_data)
        #sale_date = data.text
        #print("出发日期：%s"%sale_date)
        time.sleep(3)
        book_btn = driver.find_element_by_xpath("//*[@id='content']/div[3]/div/div[2]/div[2]/h3/span")
        book_btn.click()
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + '开始订购')
        time.sleep(3)

class Switch_handle:#切换窗口
    def window(self,driver01):
        self.driver = driver01
        driver = self.driver
        #获取当前窗口句柄
        handle = driver.current_window_handle
        #获取所有窗口的句柄
        handles = driver.window_handles
        #对窗口进行遍历
        for newhandle in handles:
            if newhandle != handle:
                driver.switch_to_window(newhandle)
                now_time =str(datetime.datetime.now())
                print('%s'%now_time + ':' + '切换到下单页面窗口')               
        time.sleep(3)
        new_url = driver.current_url
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "当前页面的URL是：%s"%new_url)
        time.sleep(10)
        #box = driver.find_element_by_xpath("/html/body/div[15]/div")
class Info:
    def queren(self,driver01):
        self.driver = driver01
        driver = self.driver   
        btn = driver.find_element_by_xpath("//*[@id='confirmModal']").find_element_by_xpath("//*[@id='confirmModal']/div/div/div[2]/button")
        btn.click()
    def tixing(self,driver01):
        self.driver = driver01
        driver = self.driver
        ipm_tips = driver.find_element_by_xpath("//*[@id='46969']")
        ipm_tips.click()
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "勾选重要提醒")
    def distance(self,driver01):
        self.driver = driver01
        driver = self.driver
        xingcheng = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/section[2]/div[1]/p")
        driver.execute_script("arguments[0].scrollIntoView();", xingcheng)#鼠标滑到到此元素
        ActionChains(driver).click_and_hold(xingcheng).perform()
        xingcheng = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/section[2]/div[1]/p")
        xingcheng.click()
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "点击行程安排")
        time.sleep(3)
    def bixuan(self,driver01):
        self.driver = driver01
        driver = self.driver
        mandatory_choose = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/section[2]/div[2]").find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/section[2]/div[2]/div/div/div[1]/ul/li[1]/label/p")
        mandatory_choose.click()
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "勾选必选项")
    def zixuan(self,driver01):
        self.driver = driver01
        driver = self.driver
        optional_choose = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/section[2]/div[2]/div/div/div[2]/ul/li[1]/label")
        optional_choose.click()
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "勾选自选项")
        time.sleep(5)
    def queding(self,driver01):
        self.driver = driver01
        driver = self.driver
        comfirm_btn = driver.find_element_by_xpath("//*[@id='top']/section[2]/div[2]/div/button")
        comfirm_btn.click()
        time.sleep(5)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "确认选择")
        #print("确认选择")
class Connect:
    def person(self,now_xing,now_ming,driver01):
    #预定联系人
        self.driver = driver01
        driver = self.driver
        self.xing =now_xing
        self.ming = now_ming
        xing = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[1]/div/div[1]/div[1]/input")
        xing.send_keys(self.xing)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "输入联系人的姓")      
        ming = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[1]/div/div[1]/div[2]/input")
        ming.send_keys(self.ming)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "输入联系人的名")
class Travel1:
    def passenger1_name(self,now_xing,now_ming,driver01):
        self.driver = driver01
        driver = self.driver
        self.xing = now_xing
        self.ming = now_ming
        #乘客1信息
        room1_xing = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[1]/div[2]/div[1]/input")
        room1_xing.send_keys(self.xing)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "输入姓1")
        #print("输入姓1")
        room1_ming = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[1]/div[2]/div[2]/input")
        room1_ming.send_keys(self.ming)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "输入名1")
        #print("输入名1")
    def date1(self,now_date,driver01):
        self.driver = driver01
        driver = self.driver
        self.date = now_date
        js = "$('input[name=birthday]').removeAttr('readonly')" # jQuery，移除属性将日期设置为可以输入的文本框
        driver.execute_script(js)
        room1_date =driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[1]/div[3]/div[1]/input")
        room1_date.send_keys(self.date)
        room1_date =driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[1]/div[3]/div[1]/input")
        room1_date.send_keys(Keys.ENTER)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "填写出生日期1")
        #print("填写出生日期1")
        time.sleep(4)
    def guoji1(self,guojia,driver01):
        self.driver = driver01
        driver = self.driver
        self.guojia = guojia
        room1_nationality = driver.find_element_by_xpath("//*[@id='fellowTraveler']/div/ul/li/div[1]/div[3]/div[2]/input")
        room1_nationality.send_keys(self.guojia)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "填写国籍1")
        #print("填写国籍1")
    def huzhao1(self,passport,driver01):
        self.driver = driver01
        driver = self.driver
        self.passport = passport
        room1_passport = driver.find_element_by_xpath("//*[@id='fellowTraveler']/div/ul/li/div[1]/div[3]/div[3]/input")
        room1_passport.send_keys(self.passport)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "填写护照1")
        #print("填写护照1")
        room2_xing = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[2]/div[1]/input")
        driver.execute_script("arguments[0].scrollIntoView();", room2_xing)#鼠标滑到到此元素
        ActionChains(driver).click_and_hold(room2_xing).perform()

    # chengren = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[1]/span[1]")
    # driver.execute_script("arguments[0].scrollIntoView();", chengren)#鼠标滑到到此元素
    # ActionChains(driver).click_and_hold(chengren).perform()
    # time.sleep(3)
    # room1_area = driver.find_element_by_id("fellowTravelerAreaCode").find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[1]/div[4]/div/div/select/option[2]")
    # room1_area.click()
    #TETS
    
    def connect_phone(self,phoneno,driver01):
        self.driver = driver01
        driver = self.driver
        self.phoneno = phoneno
        nr = driver.find_element_by_id("fellowTravelerAreaCode")
        select = Select(nr)
        select.select_by_value("86")#使用select下拉选择中国区域码
        room1_phone = driver.find_element_by_xpath("//*[@id='fellowTravelerPhoneNum']")
        room1_phone.send_keys(self.phoneno)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "填写联系人的手机号码1")
        #print("填写联系人的手机号码1")
        time.sleep(3)
    #乘客2信息
    # room2_xing = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[2]/div[1]/input")
    # driver.execute_script("arguments[0].scrollIntoView();", room2_xing)#鼠标滑到到此元素
    # ActionChains(driver).click_and_hold(room2_xing).perform()
class Travel2:
    def passenger2_name(self,now_xing,now_ming,driver01):
        self.driver = driver01
        driver = self.driver
        self.xing = now_xing
        self.ming = now_xing
        room2_xing = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[2]/div[1]/input")
        room2_xing.send_keys(self.xing)
        #room2_xing.send_keys(Keys.TAB)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "填写姓2")
        #print("填写姓2")
        time.sleep(3)
        room2_ming = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[2]/div[2]/input")
        room2_ming.send_keys(self.ming)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "填写名2")
    def date2(self,now_date,driver01):
        self.driver = driver01
        driver = self.driver
        self.date = now_date
        js = "$('input[name=birthday]').removeAttr('readonly')" # jQuery，移除属性将日期设置为可以输入的文本框
        driver.execute_script(js)
        room2_date = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[3]/div[1]/input")
        room2_date.send_keys(self.date)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "出生日期2")
        room2_date = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[3]/div[1]/input")
        room2_date.send_keys(Keys.ENTER)
    def guoji2(self,guojia,driver01):
        self.driver = driver01
        driver = self.driver
        self.guojia = guojia
        room2_nationality = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[3]/div[2]/input")
        room2_nationality.send_keys(self.guojia)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "填写国籍2")
    def huzhao2(self,passport,driver01):
        self.driver = driver01
        driver = self.driver
        self.passport = passport
        room2_passport = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[3]/div[3]/input")
        room2_passport.send_keys(self.passport)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "填写护照2")
class Beizhu:
    def remark(self,remark,driver01):
        self.driver = driver01
        driver = self.driver
        self.remark = remark
        order_remark = driver.find_element_by_name("remarks")
        order_remark.send_keys(self.remark)
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "订单备注")
        time.sleep(3)
    def tongyi(self,driver01):
        self.driver = driver01
        driver = self.driver
        now_agreement = driver.find_element_by_id("agreement")
        now_agreement.click()
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "勾选协议")
    def tijiao(self,driver01):
        self.driver = driver01
        driver = self.driver               
        commit_order = driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/section/div/button[1]/span[1]")
        now_price = commit_order.text
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "当前的订单价格%s"%now_price)
        #print("当前的订单价格%s"%now_price)
        time.sleep(3)
        commit_order.click()
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "提交订单")
        time.sleep(20)

#支付页面
class Pay:
    def paypagesss(self,driver01):
        self.driver = driver01
        driver = self.driver
        now_url = driver.current_url
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "当前页面的支付连接是：%s"%now_url)
        #print("当前页面的支付连接是：%s"%now_url)
    def paymethod(self,driver01):
        self.driver = driver01
        driver = self.driver
        qudao = driver.find_element_by_xpath("//*[@id='paymentMethod']").find_element_by_xpath("//*[@id='paymentMethod']/div/div[1]/ul/li[1]/a")
        #xingcheng = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/section[2]/div[1]/p")
        driver.execute_script("arguments[0].scrollIntoView();", qudao)#鼠标滑到到此元素
        ActionChains(driver).click_and_hold(qudao).perform()
        qudao = driver.find_element_by_xpath("//*[@id='paymentMethod']").find_element_by_xpath("//*[@id='paymentMethod']/div/div[1]/ul/li[1]/a")
        bizhong = qudao.text
        now_time =str(datetime.datetime.now())
        print('%s'%now_time + ':' + "支付币种是：%s"%bizhong)
        #print("支付币种是：%s"%bizhong)
        qudao.click()
    def paypal(self,driver01):
        self.driver = driver01
        driver = self.driver
        now_paypal = driver.find_element_by_xpath("//*[@id='paymentMethod']/div/div[2]/ul/li[4]/a/div")
        now_paypal.click()
    def pay(self,driver01):
        self.driver = driver01
        driver = self.driver
        commit_pay = driver.find_element_by_xpath("//*[@id='goToPay']")
        commit_pay.click()


class End:
    def __init__(self):
        driver.quit()

##引用unittest模块

class Llt_pc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        url1 = "https://www.lulutrip.com"
        driver.get(url1)
        driver.maximize_window()
        driver.implicitly_wait(3)#只能等待3s

    def test_login(self):
        try:
            driver01= self.driver
            new_login = Login()
            new_login.anniu(driver01)
            new_login.account("baozi.wu@ipptravel.com","ceshi321",driver01)
            new_login.now_cookie(driver01)
            new_login.juege_login(driver01)
        except Exception as error01:
            print('失败原因:%s'%error01)
            sendmail_error = Sendmail()#失败时发送邮件
    def test_search(self):
        try:
            driver01 = self.driver
            new_search = Search()#调用搜索对象
            new_search.search_input("12504",driver01)
            new_search.juege_search(driver01)
        except Exception as error02:
            print('失败原因:%s'%error02)
            Sendmail = Sendmail()
    def test_product(self):
        try:
            driver01 = self.driver
            new_login = Login()#登录
            new_login.anniu(driver01)
            new_login.account("baozi.wu@ipptravel.com","ceshi321",driver01)
            new_login.now_cookie(driver01)
            new_search = Search()#调用搜索对象
            new_search.search_input("12504",driver01)
            new_product = Product()#调产品详情页对象
            new_product.second_month(driver01)
            new_product.info_product(driver01)
            new_window = Switch_handle()#切换到新窗口
            new_window.window(driver01)
            order_info = Info()#下单信息
            order_info.queren(driver01)
            order_info.tixing(driver01)
            order_info.distance(driver01)
            order_info.bixuan(driver01)
            order_info.zixuan(driver01)
            order_info.queding(driver01)
            new_connect = Connect()#预定联系人
            new_connect.person("bao","zi",driver01)
            new_travel1 = Travel1()#出现旅客1
            new_travel1.passenger1_name("bao","zi",driver01)
            new_travel1.date1("1988-12-01",driver01)
            new_travel1.guoji1("China",driver01)
            new_travel1.huzhao1("9527001",driver01)
            new_travel1.connect_phone("13600136000",driver01)
            new_travel2 =Travel2()#出现旅客2
            new_travel2.passenger2_name("lu","renjia",driver01)
            new_travel2.date2("1988-11-20",driver01)
            new_travel2.guoji2("China",driver01)
            new_travel2.huzhao2("9527002",driver01)
            new_remark = Beizhu()#同意并提交
            new_remark.remark("test order",driver01)
            new_remark.tongyi(driver01)
            new_remark.tijiao(driver01)
            new_pay = Pay()#进入支付页面
            new_pay.paypagesss(driver01)
            new_pay.paymethod(driver01)
            new_pay.paypal(driver01)
            new_pay.pay(driver01)
        except Exception as error03:
            print('失败原因:%s'%error03)
            sendmail_error = Sendmail()

    def tearDown(self):
        driver = self.driver
        driver.quit()

if __name__ =="__main__":
    #unittest.main()
    testunit = unittest.TestSuite()
    testunit.addTest(Llt_pc("test_login"))
    testunit.addTest(Llt_pc("test_product"))
    testunit.addTest(Llt_pc("test_search"))
    filename = 'D:\\autotest\PC\\report\\result.html'
    report = open(filename,'wb')
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = report,
        title = u'路路行PC端下单流程测试报告',
        description = u'用例执行情况'
    )
    runner.run(testunit)
   