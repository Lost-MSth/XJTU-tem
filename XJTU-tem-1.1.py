##西交健康每日报填报修改版v1.1  by Lost
import datetime

##设置选项
netid = "" #NetID
password = "" #密码
temperature = "36.5" #体温
start_date=datetime.date(2020,8,29) #填报起始日期，别太出格，自己把握，这里没测试填到很久以前会发生什么
end_date=datetime.date(2020,8,30) #填报终止日期，尽量别超过当天日期
am_pm_flag=0 #填报时间段模式，修改数字进行设定：0——填报上下午     1——只填报上午     2——只填报下午
##

'''
IE浏览器驱动，其下载地址是：https://www.selenium.dev/downloads/

对照自己电脑安装的浏览器和对应的版本，分别从上面的地址下载驱动文件，
下载解压后，将下载下来的驱动放到python的根目录中。

如有问题，请参考：http://blog.sina.com.cn/s/blog_6125ae360102yg2k.html
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def login(netid,password): #登陆
    driver = webdriver.Ie() #使用IE
    driver.get('http://one2020.xjtu.edu.cn/EIP/user/index.htm')
    i=0
    while driver.current_url == "https://org.xjtu.edu.cn/openplatform/login.html" and i<=5:
        i=i+1
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Account password login']")))
        driver.find_element_by_class_name("username").send_keys(netid)
        driver.implicitly_wait(0.5)
        driver.find_element_by_class_name("pwd").send_keys(password)
        driver.implicitly_wait(0.5)
        driver.find_element_by_id("account_login").send_keys(Keys.ENTER)
        
        try:
            driver.implicitly_wait(10)
            driver.get('http://jkrb.xjtu.edu.cn/EIP/user/index.htm')
        except:
            pass
    if i>=5:
        driver.quit()
        raise Exception("Error!")
    
    return driver


def one_punch(driver,temperature,date,am_pm):#核心 一次填报
    driver.get('http://jkrb.xjtu.edu.cn/EIP/cooperative/openCooperative.htm?flowId=4af591a971bc5d460171e279f192078d')#网页版
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src,'EIP/flow/flowForm')]")))
    iframe=driver.find_element_by_xpath("//iframe[contains(@src,'EIP/flow/flowForm')]")
    driver.switch_to.frame(iframe)
    
    driver.execute_script("mini.get('XWFQTS').setValue(0)")
    driver.execute_script("mini.get('SWFQTS').setValue(0)")
    driver.execute_script("mini.get('XWFQTS').doValueChanged()")
    driver.execute_script("mini.get('SWFQTS').doValueChanged()")
    js="mini.get('BRTW').setValue("+str(temperature)+")"
    driver.execute_script(js)
    driver.execute_script("mini.get('BRTW').doValueChanged()")
    driver.execute_script("mini.get('YMTYS').setValue('绿色')")
    driver.execute_script("mini.get('YMTYS').doValueChanged()")
    js="mini.get('TBRQ').setValue('"+date+"')"
    driver.execute_script(js)
    driver.execute_script("mini.get('TBRQ').doValueChanged()")
    js="mini.get('SJD').setValue('"+am_pm+"@#@"+am_pm+"')"
    driver.execute_script(js)
    driver.execute_script("mini.get('SJD').doValueChanged()")
    
    driver.switch_to.default_content()
    
    driver.execute_script("onSend()")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='确定']")))
    driver.execute_script("document.getElementById('mini-17').click()")



def main():
    try:
        driver=login(netid,password)
    except:
        print('登陆出错！')
    else:
        print("开始填报...")
        for i in range((end_date-start_date).days+1):
            date=str(start_date+datetime.timedelta(days=i))
            if am_pm_flag==0 or am_pm_flag==1:#上午填报
                try:
                    one_punch(driver,temperature,date,"上午")
                except:
                    print(date+"上午填报出错！")
                else:
                    print(date+"上午填报成功！")
                    
            if am_pm_flag==0 or am_pm_flag==2:#下午填报
                try:
                    one_punch(driver,temperature,date,"下午")
                except:
                    print(date+"下午填报出错！")
                else:
                    print(date+"下午填报成功！")
        print("填报完成！")
        driver.quit()


if __name__ == '__main__': main()
