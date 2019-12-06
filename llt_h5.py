#conding = utrf-8
#载入基础配置
from selenium import webdriver
import  time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
mobileEmulation = {'deviceName': 'iPhone 6'}
options = webdriver.ChromeOptions()
options01 = options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(chrome_options=options)
# url_1 = 'https://app.lulutrip.com'
# open01 = driver.get(url_1)
# window = driver.maximize_window()

# #将浏览器H5化
class Home(object):
    def __init__(self):
        url_1 = 'https://app.lulutrip.com'
        driver.get(url_1)
        window = driver.maximize_window()
    def __str__(self):
        msg = "进入首页"
        return msg
    def __del__(self):
        print("释放首页对象的内存")
    def end(self):
        driver.quit()



#登录
class login(Home):
    def __init__(self):
        tab_me = driver.find_element_by_class_name("me")
        tab_me.click()
        time.sleep(3)
        print("点击我的tab进入我的页面")
    def Account(self,number,passward):
        self.number = number
        self.passward = passward
        email_type = driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/span")
        email_type.click()
        email_account = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/div[1]/input")
        #email_account.clear()
        email_account.send_keys(self.number)
        print("输入账号")
        time.sleep(3)
        email_pwd = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/div[2]/input")
        #email_pwd.clear()
        email_pwd.send_keys(self.passward)
        print("输入密码")
    def tijiao(self):      
        commit = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/div[4]")
        commit.click()
        print(" 提交登录信息")
        time.sleep(3)
    def cookies(self):
    #登录--获取当前的cookie
        now_cookie = driver.get_cookies()
        print(now_cookie)
    def home01(self):
        Home.__init__(self)
        print("完成登录后返回首页")



#搜索
class Sousuo:
    def __init__(self):
        time.sleep(3)
        search_icon = driver.find_element_by_class_name("search-img")
        search_icon.click()
        print("点击搜索icon")
    def __str__(self):
        return "点击icon，打开搜索输入框"
    def product(self,pcode):
        self.pcode = pcode       
        time.sleep(3)
        keyword = driver.find_element_by_xpath("//*[@id='destination']/div[1]/div[1]/div/span[1]/input")
        keyword.send_keys(self.pcode)
        print("输入搜索产品：%s"%self.pcode)
    def searchbtn(self):
        time.sleep(3)
        search_icon1 = driver.find_element_by_xpath("//*[@id='destination']/div[1]/div[1]/div/span[1]/span")
        search_icon1.click()
        print("开始执行搜索")
        time.sleep(3)



#进入详情页
class Book:#点击订购按钮
    def __init__(self):
        url_2 = driver.current_url
        print("详情页的URL：%s"%url_2)
    def bookbtn(self):
        book_now = driver.find_element_by_xpath("//*[@id='container']/div[1]/div[3]/div[2]/p")
        book_now.click()
        print("点击立即订购按钮")
        time.sleep(5)
class Bookdata():
    def __init__(self):
        price_date = driver.find_element_by_xpath("//*[@id='c_booking_calendar']")
        #driver.execute_script("arguments[0].click();", price_date)
        price_date.click()
        time.sleep(3)
        # print("层级定位")
        # book_date = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div[35]/div[1]")
        # book_date.click()
        print("选择出发日期")
        time.sleep(8)
        print("等待8s")
    def importance(self):
        trip = driver.find_element_by_xpath("//*[@id='container']/div[1]/div[3]/div[1]/div/div")
        trip.click()#勾选重要提示
        time.sleep(5)
class Distance:
    def rukou(self):#打开入口
        arrow = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]")
        driver.execute_script("arguments[0].click();", arrow)
        #arrow.click()
        time.sleep(15)
        print("等待15s打开行程选择页面")
    #driver.find_element_by_xpath("//*[@id='c_acts_view']/div[2]").click()
    def mandatory(self):
        choose_mandatory = driver.find_element_by_xpath("//*[@id='c_act_cell']/div[1]/div/div")
        driver.execute_script("arguments[0].click();", choose_mandatory)#定位的原因有其他遮挡，采用此方法移除遮挡来点击
        choose_mandatory = driver.find_element_by_xpath("//*[@id='c_act_cell']/div[1]/div/div")
        driver.execute_script("arguments[0].click();", choose_mandatory)#定位的原因有其他遮挡，采用此方法移除遮挡来点击
        print("勾选必填项")
    def optional(self):
        choose_optional = driver.find_element_by_xpath("//*[@id='c_act_cell']/div[2]/div[1]")
        driver.execute_script("arguments[0].click();", choose_optional)
        print("勾选非必填项")
    def distancebtn(self):
        choose_btn = driver.find_element_by_xpath("//*[@id='c_acts_view']/div[3]")
        choose_btn.click()
        print("完成按钮")
        time.sleep(3)

class Info:
#资料填写页面
    def dayphone(self,phone):
        self.phone = phone
        next_book = driver.find_element_by_class_name("nextBtn")
        next_book.click()
        time.sleep(6)
        connect_tel = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/input")
        connect_tel.send_keys(self.phone)
        print("输入联系方式")
    def passenger_one(self,fristnme,secondname,bathdata,nationality,password):#成人1资料
        self.fristname = fristnme
        self.secondname = secondname
        self.bathdata = bathdata
        self.nationality = nationality
        self.password = password
        frist_name = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/span[2]/input")
        frist_name.send_keys(self.fristname)
        brith_date = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/span[2]/input[1]")
        brith_date.send_keys(self.bathdata)
        second_name =driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]/input")
        second_name.send_keys(self.secondname)
        country = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/span[2]/input")
        country.send_keys(self.nationality)
        pass_port = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[2]/span[2]/input")
        pass_port.send_keys(self.password)

    def passenger_two(self,fristnme,secondname,bathdata,nationality,password):#成人2资料
        self.fristname = fristnme
        self.secondname = secondname
        self.bathdata = bathdata
        self.nationality = nationality
        self.password = password
        frist_name2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[1]/span[2]/input")
        frist_name2.send_keys(self.fristname)
        brith_date2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/span[2]/input[1]")
        brith_date2.send_keys(self.bathdata)
        second_name2 =driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]/input")
        second_name2.send_keys(self.secondname)
        country2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/span[2]/input")
        country2.send_keys(self.nationality)
        pass_port2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[3]/div[2]/span[2]/input")
        pass_port2.send_keys(self.password)

    def commit(self): #提交订单      
        commit_order = driver.find_element_by_xpath("/html/body/div[1]/footer/div[2]")
        commit_order.click()
        time.sleep(5)
class Paycenter:
    def __init__(self):
        url_3 = driver.current_url
    def __str__(self):
        msg = "支付中心连接:%s"%url_3
        return msg


#第一步：打开首页并登录
home_page = Home()
newlogin = login()
newlogin.Account("baozi.wu@ipptravel.com","ceshi321")
newlogin.tijiao()
newlogin.cookies()
newlogin.home01()

#第二步：搜索产品
newsearch = Sousuo()
newsearch.product("12504")
newsearch.searchbtn()

#第三步：详情页里点击订购
newbook = Book()
newbook.bookbtn()

#第四：选择出发日期和行程
try:
    newbookdata = Bookdata()
    newbookdata.importance()
    
except Exception as result:
    print("捕获到异常：%s"%result)
    
    #home_page = Home()
#第五步：选择行程
else:
    print("未有异常时执行")
    newdistance = Distance()
    newdistance.rukou()
    newdistance.mandatory()
    newdistance.optional()
    newdistance.distancebtn()
finally:
    print("有无异常都继续执行")

#第六步：填写出行人员信息
newinfo = Info()
newinfo.dayphone("13600136000")
newinfo.passenger_one("bao","zi","1988-11-28","China","W9527001")
newinfo.passenger_two("lu","renjia","1988-11-28","China","W9527002")
newinfo.commit()

#第七步：提交订单
payment = Paycenter()



#关闭浏览器
home_page.end()   