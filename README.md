# XJTU-tem
西安交通大学每日健康报自动填报——修改加强版
## 简介
这是西安交通大学每日健康报的自动填报脚本，本脚本基于Python运行，可选择填报时间段和日期进行批量填报，程序并没有做太多测试，若有bug，敬请谅解。
## 运行环境
- Windows操作系统
- Python 2&3
- Selenium模块
- IE webdriver
- IE浏览器

**注：** 本脚本在Windows 10企业版、Python 3.7、IE 11.295.18362.0环境下运行通过（2020.8.24）

## 环境搭建
### Selenium模块安装
使用Python自带的pip进行安装即可  
```
pip install selenium
```
因为网络问题，无法从国外下载模块，则可以使用国内镜像源，比如使用清华镜像
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ selenium
```
### IE webdriver下载与部署
本脚本基于IE浏览器进行自动填报，需要IE浏览器相关驱动（选择IE就是因为我不用Chrome哈哈哈哈哈哈哈哈哈）  
IE浏览器驱动，其下载地址是：https://www.selenium.dev/downloads/  
若无法下载，也可以下载本项目中上传的zip，但不保证绝对能用

下载完进行解压，将其中的IEDriverServer.exe文件放置到Python根目录下（即与Python.exe在同一目录）

请打开IE浏览器进行设置（注意不是Edge浏览器，是IE！）
- 在工具-Internet选项-安全选项卡中关闭四个区域的保护模式（四个图案依次点击，保证每个底下的复选框都没有勾上）
- 在工具-缩放中调整缩放为100%

如仍然存在问题，请参考：http://blog.sina.com.cn/s/blog_6125ae360102yg2k.html
## 使用
用Python IDLE编辑代码，在设置选项中输入NetID和密码，设置所填体温、填报时间段、填报日期，运行脚本，等待运行完毕即可
```python
##设置选项
netid = "" #NetID
password = "" #密码
temperature = "36.5" #体温
start_date=datetime.date(2020,8,24) #填报起始日期，别太出格，自己把握，这里没测试填到很久以前会发生什么
end_date=datetime.date(2020,8,28) #填报终止日期，尽量别超过当天日期
am_pm_flag=0 #填报时间段模式，修改数字进行设定：0——填报上下午     1——只填报上午     2——只填报下午
##
```
## 注意
1. 本脚本利用了前端绕过漏洞，可以任意选择日期进行填报，请谨慎使用
2. 学校的填报时间限制目前无法绕过，请在以下时间段使用本程序`1、每天上午填报时间段：6:00—11:00。 2、每天下午填报时间段：12:00—17:00。`
3. 请务必保证环境搭建无误，IE配置错误将导致程序无法运行
4. 请保证网络环境畅通
## 鸣谢
本项目灵感来自https://github.com/chaoers/xjtu-temperature-selenium<br>
特别鸣谢[@chaoers](https://github.com/chaoers)
## 联系方式
如有必要，可以联系本人，微信号：Lost-MSth
## 使用许可
[MIT](LICENSE) © Lost
