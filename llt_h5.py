#conding = utrf-8
#载入基础配置
from selenium import webdriver
import  time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#将浏览器H5化
mobileEmulation = {'deviceName': 'iPhone 6'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(chrome_options=options)

#打开浏览器输入URL且最大化
url_1 = 'https://app.lulutrip.com'
driver.get(url_1)
driver.maximize_window()

#登录
tab_me = driver.find_element_by_class_name("me")
tab_me.click()
time.sleep(3)
email_type = driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/span")
email_type.click()
email_account = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/div[1]/input")
#email_account.clear()
email_account.send_keys("baozi.wu@ipptravel.com")
time.sleep(3)
email_pwd = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/div[2]/input")
#email_pwd.clear()
email_pwd.send_keys("ceshi321")
commit = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/div[4]")
commit.click()
time.sleep(3)
#登录--获取当前的cookie
now_cookie = driver.get_cookies()
print(now_cookie)
driver.get(url_1)#登录后跳转至home_page


#搜索
time.sleep(3)
search_icon = driver.find_element_by_class_name("search-img")
search_icon.click()
time.sleep(3)
keyword = driver.find_element_by_xpath("//*[@id='destination']/div[1]/div[1]/div/span[1]/input")
keyword.send_keys("12504")
time.sleep(3)
search_icon1 = driver.find_element_by_xpath("//*[@id='destination']/div[1]/div[1]/div/span[1]/span")
search_icon1.click()
time.sleep(3)

#进入详情页
url_2 = driver.current_url
print("详情页的URL：%s"%url_2)
book_now = driver.find_element_by_xpath("//*[@id='container']/div[1]/div[3]/div[2]/p")
book_now.click()#立即订购
time.sleep(5)
price_date = driver.find_element_by_xpath("//*[@id='c_booking_calendar']")
price_date.click()
time.sleep(3)
print("层级定位")
book_date = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div[35]/div[1]")
book_date.click()#选择日期
time.sleep(8)
print("等待8s")
trip = driver.find_element_by_xpath("//*[@id='container']/div[1]/div[3]/div[1]/div/div")
trip.click()#勾选重要提示
time.sleep(5)

arrow = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]")
driver.execute_script("arguments[0].click();", arrow)
#arrow.click()
time.sleep(15)
print("等待15s打开行程选择页面")
#driver.find_element_by_xpath("//*[@id='c_acts_view']/div[2]").click()
choose_mandatory = driver.find_element_by_xpath("//*[@id='c_act_cell']/div[1]/div/div")
driver.execute_script("arguments[0].click();", choose_mandatory)#定位的原因有其他遮挡，采用此方法移除遮挡来点击
choose_mandatory = driver.find_element_by_xpath("//*[@id='c_act_cell']/div[1]/div/div")
driver.execute_script("arguments[0].click();", choose_mandatory)#定位的原因有其他遮挡，采用此方法移除遮挡来点击

print("勾选必填项")

choose_optional = driver.find_element_by_xpath("//*[@id='c_act_cell']/div[2]/div[1]")
driver.execute_script("arguments[0].click();", choose_optional)
print("勾选非必填项")

choose_btn = driver.find_element_by_xpath("//*[@id='c_acts_view']/div[3]")
choose_btn.click()
print("完成按钮")
time.sleep(3)

#资料填写页面
next_book = driver.find_element_by_class_name("nextBtn")
next_book.click()
time.sleep(6)
connect_tel = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/input")
connect_tel.send_keys("13600136000")
print("输入联系方式")

#成人1资料
frist_name = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/span[2]/input")
frist_name.send_keys("bao")
brith_date = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/span[2]/input[1]")
brith_date.send_keys("2016-08-08")
second_name =driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]/input")
second_name.send_keys("zi")
country = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/span[2]/input")
country.send_keys("China")
pass_port = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[2]/span[2]/input")
pass_port.send_keys("9527001")

#成人2资料
frist_name2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[1]/span[2]/input")
frist_name2.send_keys("bao")
brith_date2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/span[2]/input[1]")
brith_date2.send_keys("2012-08-08")
second_name2 =driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]/input")
second_name2.send_keys("zi01")
country2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/span[2]/input")
country2.send_keys("China")
pass_port2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[3]/div[2]/span[2]/input")
pass_port2.send_keys("9527002")

#提交订单
commit_order = driver.find_element_by_xpath("/html/body/div[1]/footer/div[2]")
commit_order.click()
time.sleep(5)
url_3 = driver.current_url
print("支付中心连接:%s"%url_3)



#关闭浏览器
driver.quit()