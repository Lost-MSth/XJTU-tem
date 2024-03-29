# XJTU-tem
西安交通大学健康每日报自动填报——修改加强版

> 因为你懂的的原因，此项目恐怕再无作用，应该也不会更新了，仅于此处留档纪念  
> 很难受啊，谁知道什么时候才能真正结束呢？ 2023.5.20

## 简介
这是西安交通大学本科生健康每日报的自动填报脚本，本脚本基于Python运行，可选择填报时间段和日期进行批量填报，程序并没有做太多测试，若有bug，敬请谅解。

## 更新日志

# Version 1.3
- 更改接口地址，针对当前填报页面修复脚本功能
- 新增体温波动范围选择

> **注**：Beta版懒得修，1.3仍然可用，不用在意页面上的报错

# Version Beta 1.1
- 修改了登陆方式，增加了登陆成功率
  
# Version 1.2
- 修改了登陆方式，增加了登陆成功率

# Version Beta 1.0
- 因学校修改了填报界面，故开发出应对新填报方式的Beta版本，这个版本**只能填报当天的健康报**，实用性大大下降
- 修改了登陆成功的测试方法，增加了登陆成功率

**注：** 原填报通道似乎没有封锁，现在仍然可以使用1.1版本进行批量填报
# Version 1.1
- 修改了登陆成功的测试方法，增加了登陆成功率

## 运行环境
- Windows操作系统
- Python 2&3
- Selenium模块
- IE webdriver
- IE浏览器

**注：** 本脚本在Windows 10企业版、Python 3.7、IE 11.295.18362.0环境下运行通过（2020.8.24）

## 环境搭建
这里默认了使用的是Windows系统且存在IE浏览器，Python的安装过程略去
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
netid = ""  # NetID
password = ""  # 密码
temperature = 36.5  # 体温
delta_temperature = 0.1  # 体温波动范围，只能精确到第一位小数
start_date = datetime.date(2022, 2, 3)  # 填报起始日期，别太出格，自己把握，这里没测试填到很久以前会发生什么
end_date = datetime.date(2022, 2, 11)  # 填报终止日期，尽量别超过当天日期

check_date = str(datetime.datetime(2022, 1, 23, 14, 21))[:-3]
# 最近一次核酸采样时间，是否48小时默认填否
##
```
## 注意
1. 本脚本利用了前端绕过漏洞，可以任意选择日期进行填报，请谨慎使用
2. 学校的填报时间限制目前无法绕过，**请在以下时间段使用本程序：**`1、每天上午填报时间段：6:00—11:00。 2、每天下午填报时间段：12:00—17:00。`
   > 貌似现在没有这个限制了（2022.2.11注）
3. 请务必保证环境搭建无误，IE配置错误将导致程序无法运行
4. 请保证网络环境畅通
5. 请确保曾经进行过健康报的填报，否则无法从服务器上获取到其它信息（例如，存在班级号变动情况，需先进行一次手动填报，才可以正常使用）
6. 是**IE浏览器**！不是Edge也不是Chrome更不是Firefox绝不可能是360极速！当然如果您有实力，请自行下载其他浏览器驱动并修改代码，选用IE是为了更广泛的适用性
7. 经过测试，程序在登陆部分存在一些问题，可能导致无法正常填报，若发现浏览器内没有出现填报表单而卡在了登陆界面，请关闭程序后重新运行
## 鸣谢
本项目灵感来自[xjtu-temperature-selenium|西安交通大学每日健康报自动化脚本](https://github.com/chaoers/xjtu-temperature-selenium)<br>
特别鸣谢[@chaoers](https://github.com/chaoers)
## 联系方式
如有必要，可以联系本人   
邮箱：th84292@foxmail.com
## 使用许可
[MIT](LICENSE) © Lost
