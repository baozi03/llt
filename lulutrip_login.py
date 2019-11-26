#condind = utf-8
def llt_login(driver):
    from selenium import  webdriver
    import time
    from selenium.webdriver.common.keys import Keys

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
    usr_name = driver.find_element_by_xpath("/html/body/div[3]/div/div/form[1]/div[1]/div/div[1]/input")
    print("找到账户输入框")
    usr_name.clear()
    usr_name.click()
    usr_name.send_keys("baozi.wu@ipptravel.com")
    print("输入账户")
    pwd = driver.find_element_by_xpath("/html/body/div[3]/div/div/form[1]/div[2]/div/div[1]/span/input")
    pwd.clear()
    pwd.click()
    pwd.send_keys("ceshi321")
    print("输入密码")
    remember = driver.find_element_by_xpath("/html/body/div[3]/div/div/form[1]/div[3]/div/label/input")
    remember.click()
    submit = driver.find_element_by_class_name("comm-btn1")
    submit.click()
    print("点击提交")
    cookie = driver.get_cookies()
    print("打印cookie信息%s"%cookie)
    driver.delete_all_cookies()
    print("删除所有的cookies")
    driver.implicitly_wait(3)
    driver.quit()

def cycle_login():
    from selenium import  webdriver
    #打开浏览器输入url
    driver = webdriver.Firefox()
    url1 = "https://www.lulutrip.com"
    driver.get(url1)
    driver.maximize_window()
    driver.implicitly_wait(3)#只能等待3s
    #捕获异常：
    try:
        llt_login(driver)
    except BaseException:
        cookie = driver.get_cookies()
        print("打印cookie信息%s"%cookie)
        driver.delete_all_cookies()
        print("删除所有的cookies")
        driver.implicitly_wait(3)
        driver.quit()
i = 0
while i < 200:
    cycle_login()
    i += 1
    print("执行登录成功的次数%s"%i)

def search_product():
    search = driver.find