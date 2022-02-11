# 西交每日健康报填报修改版v1.3  by Lost
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import datetime
import random

# 设置选项
netid = ""  # NetID
password = ""  # 密码
temperature = 36.5  # 体温
delta_temperature = 0.1  # 体温波动范围，只能精确到第一位小数
start_date = datetime.date(2022, 2, 3)  # 填报起始日期，别太出格，自己把握，这里没测试填到很久以前会发生什么
end_date = datetime.date(2022, 2, 11)  # 填报终止日期，尽量别超过当天日期

check_date = str(datetime.datetime(2022, 1, 23, 14, 21))[:-3]
# 最近一次核酸采样时间，是否48小时默认填否
##

'''
IE浏览器驱动，其下载地址是：https://www.selenium.dev/downloads/

对照自己电脑安装的浏览器和对应的版本，分别从上面的地址下载驱动文件，
下载解压后，将下载下来的驱动放到python的根目录中。

如有问题，请参考：http://blog.sina.com.cn/s/blog_6125ae360102yg2k.html
'''


def login(netid, password):  # 登陆
    driver = webdriver.Ie()  # 使用IE
    driver.get('http://one2020.xjtu.edu.cn/EIP/user/index.htm')
    print('开始登录...')
    i = 0
    while driver.current_url == "http://org.xjtu.edu.cn/openplatform/login.html" or driver.current_url == "https://org.xjtu.edu.cn/openplatform/login.html" and i <= 5:
        i = i+1
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//span[text()='Account password login']")))
        driver.find_element_by_class_name("username").send_keys(netid)
        driver.implicitly_wait(0.5)
        driver.find_element_by_class_name("pwd").send_keys(password)
        driver.implicitly_wait(0.5)
        driver.find_element_by_id("account_login").send_keys(Keys.ENTER)
        time.sleep(1)

        try:
            driver.implicitly_wait(10)
            driver.get('http://jkrb.xjtu.edu.cn/EIP/user/index.htm')
        except:
            pass
    if i >= 5:
        driver.quit()
        raise Exception("Error!")

    return driver


def one_punch(driver, temperature, date):  # 核心 一次填报
    driver.get(
        'http://jkrb.xjtu.edu.cn/EIP/cooperative/openCooperative.htm?flowId=4af591ba740568b9017433ecca4139bc')  # 网页版
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//iframe[contains(@src,'EIP/flow/flowForm')]")))
    iframe = driver.find_element_by_xpath(
        "//iframe[contains(@src,'EIP/flow/flowForm')]")
    driver.switch_to.frame(iframe)

    driver.execute_script("mini.get('HTD2274E').setValue(1)")
    driver.execute_script("mini.get('HTD2274E').doValueChanged()")

    js = "mini.get('BRTW').setValue("+str(temperature)+")"
    driver.execute_script(js)
    driver.execute_script("mini.get('BRTW').doValueChanged()")

    driver.execute_script("mini.get('GLQK').setValue('未被隔离')")
    driver.execute_script("mini.get('GLQK').doValueChanged()")
    driver.execute_script("mini.get('JCJG').setValue('阴性')")
    driver.execute_script("mini.get('JCJG').doValueChanged()")
    driver.execute_script("mini.get('SFJYHSZM').setValue('否')")
    driver.execute_script("mini.get('SFJYHSZM').doValueChanged()")
    driver.execute_script("mini.get('YMTYS').setValue('绿色')")
    driver.execute_script("mini.get('YMTYS').doValueChanged()")

    js = "mini.get('TBRQ').setValue('"+date+"')"
    driver.execute_script(js)
    driver.execute_script("mini.get('TBRQ').doValueChanged()")
    js = "mini.get('ZJYCHSJCSJ').setValue('"+check_date+"')"
    driver.execute_script(js)
    driver.execute_script("mini.get('ZJYCHSJCSJ').doValueChanged()")
    js = "mini.get('JRRQ').setValue('"+date+"')"
    driver.execute_script(js)
    driver.execute_script("mini.get('JRRQ').doValueChanged()")
    

    driver.switch_to.default_content()

    driver.execute_script("onSend()")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='确定']")))
    driver.execute_script("document.getElementById('mini-17').click()")


def main():
    try:
        driver = login(netid, password)
        pass
    except:
        print('登陆出错！')
    else:
        print("开始填报...")
        random_range = int(delta_temperature/0.1)
        for i in range((end_date-start_date).days+1):
            date = str(start_date+datetime.timedelta(days=i))
            try:
                t = temperature + \
                    random.randint(-random_range, random_range) * \
                    delta_temperature
                one_punch(driver, str(t), date)
            except:
                print(date+"填报出错！")
            else:
                print(date+"填报成功！")

        print("填报完成！")
        driver.quit()


if __name__ == '__main__':
    main()
