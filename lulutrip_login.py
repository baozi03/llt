#condind = utf-8
from selenium import  webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select#应用下拉选择框控件

#打开浏览器输入url
driver = webdriver.Chrome()
url1 = "https://www.lulutrip.com"
driver.get(url1)
driver.maximize_window()
driver.implicitly_wait(3)#只能等待3s
#登录
login = driver.find_element_by_class_name("default")
login.click()
time.sleep(5)
usr_name = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form[1]/div[1]/div/div[1]/input")
print("找到账户输入框")
usr_name.clear()
usr_name.click()
usr_name.send_keys("baozi.wu@ipptravel.com")
print("输入账户")
pwd = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form[1]/div[2]/div/div[1]/span/input")
pwd.clear()
pwd.click()
pwd.send_keys("ceshi321")
print("输入密码")
remember = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form[1]/div[3]/div[1]/label/input")
remember.click()
submit = driver.find_element_by_class_name("comm-btn1")
submit.click()
print("点击提交")
cookie = driver.get_cookies()
for a in cookie:
    #print(a)
    cookie01 = list(a.values())
    #print(cookie01)
    #print(cookie01[0])
    if cookie01[0] == 'LuluUser':
        print("当前的cookie是:%s"%a)
        break
    
#print("打印cookie信息%s"%cookie)
# driver.delete_all_cookies()
# print("删除所有的cookies")
# driver.implicitly_wait(3)


#搜索产品
driver.get(url1)#回到首页
search_inpt = driver.find_element_by_class_name("search-input")
search_inpt.send_keys("12504")
serch_btn = driver.find_element_by_xpath("/html/body/header/div/div[2]/div[3]/div/div[2]/a")
serch_btn.click()
time.sleep(5)


#产品详情页
data = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div[1]/div[1]/ul/li[28]")
data.click()
time.sleep(3)
book_btn = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div[2]/div[2]/h3/span")
book_btn.click()
time.sleep(3)


#获取当前窗口句柄
handle = driver.current_window_handle

#获取所有窗口的句柄
handles = driver.window_handles

#对窗口进行遍历
for newhandle in handles:
    if newhandle != handle:
        driver.switch_to_window(newhandle)
        print("切换到下单页面窗口")
time.sleep(3)
new_url = driver.current_url
print("当前页面的URL是：%s"%new_url)
time.sleep(10)
#box = driver.find_element_by_xpath("/html/body/div[15]/div")

btn = driver.find_element_by_xpath("//*[@id='confirmModal']").find_element_by_xpath("//*[@id='confirmModal']/div/div/div[2]/button")
btn.click()


ipm_tips = driver.find_element_by_xpath("//*[@id='46969']")
ipm_tips.click()
print("勾选重要提醒")


xingcheng = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/section[2]/div[1]/p")
driver.execute_script("arguments[0].scrollIntoView();", xingcheng)#鼠标滑到到此元素
ActionChains(driver).click_and_hold(xingcheng).perform()
xingcheng = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/section[2]/div[1]/p")
xingcheng.click()
print("点击行程安排")
time.sleep(3)
mandatory_choose = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/section[2]/div[2]").find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/section[2]/div[2]/div/div/div[1]/ul/li[1]/label/p")
mandatory_choose.click()
print("勾选必选项")
optional_choose = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/section[2]/div[2]/div/div/div[2]/ul/li[1]/label")
optional_choose.click()
print("勾选自选项")
comfirm_btn = driver.find_element_by_class_name("modal-confirm-btn")
comfirm_btn.click()
time.sleep(5)
print("确认选择")

#预定联系人
xing = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[1]/div/div[1]/div[1]/input")
xing.send_keys("bao")
ming = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[1]/div/div[1]/div[2]/input")
ming.send_keys("zi")
#乘客1信息
room1_xing = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[1]/div[2]/div[1]/input")
room1_xing.send_keys("bao")
print("输入姓1")
room1_ming = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[1]/div[2]/div[2]/input")
room1_ming.send_keys("zi")
print("输入名1")

js = "$('input[name=birthday]').removeAttr('readonly')" # jQuery，移除属性将日期设置为可以输入的文本框
driver.execute_script(js)
room1_date =driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[1]/div[3]/div[1]/input")
room1_date.send_keys('1988-12-03')
room1_date =driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[1]/div[3]/div[1]/input")
room1_date.send_keys(Keys.ENTER)
print("填写出生日期1")
time.sleep(4)
room1_nationality = driver.find_element_by_xpath("//*[@id='fellowTraveler']/div/ul/li/div[1]/div[3]/div[2]/input")
room1_nationality.send_keys("China")
print("填写国籍1")
room1_passport = driver.find_element_by_xpath("//*[@id='fellowTraveler']/div/ul/li/div[1]/div[3]/div[3]/input")
room1_passport.send_keys("9527001")
print("填写护照1")


# chengren = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[1]/span[1]")
# driver.execute_script("arguments[0].scrollIntoView();", chengren)#鼠标滑到到此元素
# ActionChains(driver).click_and_hold(chengren).perform()
# time.sleep(3)
# room1_area = driver.find_element_by_id("fellowTravelerAreaCode").find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[1]/div[4]/div/div/select/option[2]")
# room1_area.click()
#TETS
room2_xing = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[2]/div[1]/input")
driver.execute_script("arguments[0].scrollIntoView();", room2_xing)#鼠标滑到到此元素
ActionChains(driver).click_and_hold(room2_xing).perform()

nr = driver.find_element_by_id("fellowTravelerAreaCode")
select = Select(nr)
select.select_by_value("86")#使用select下拉选择中国区域码
room1_phone = driver.find_element_by_xpath("//*[@id='fellowTravelerPhoneNum']")
room1_phone.send_keys("13600136000")
print("填写联系人的手机号码1")
time.sleep(3)
#乘客2信息
# room2_xing = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[2]/div[1]/input")
# driver.execute_script("arguments[0].scrollIntoView();", room2_xing)#鼠标滑到到此元素
# ActionChains(driver).click_and_hold(room2_xing).perform()
room2_xing = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[2]/div[1]/input")
room2_xing.send_keys("lu")
#room2_xing.send_keys(Keys.TAB)
print("填写姓2")
time.sleep(3)
room2_ming = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[2]/div[2]/input")
room2_ming.send_keys("renjia")

js = "$('input[name=birthday]').removeAttr('readonly')" # jQuery，移除属性将日期设置为可以输入的文本框
driver.execute_script(js)
room2_date = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[3]/div[1]/input")
room2_date.send_keys("1988-12-05")
room2_date = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[3]/div[1]/input")
room2_date.send_keys(Keys.ENTER)
room2_nationality = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[3]/div[2]/input")
room2_nationality.send_keys("China")
room2_passport = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/section[3]/div/ul/li/div[2]/div[3]/div[3]/input")
room2_passport.send_keys("9527002")
order_remark = driver.find_element_by_name("remarks")
order_remark.send_keys("test order")
time.sleep(3)
now_agreement = driver.find_element_by_id("agreement")
now_agreement.click()
commit_order = driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/section/div/button[1]/span[1]")
now_price = commit_order.text
print("当前的订单价格%s"%now_price)
time.sleep(3)
commit_order.click()
time.sleep(20)



#支付页面
now_url = driver.current_url
print("当前页面的支付连接是：%s"%now_url)
driver.quit()


