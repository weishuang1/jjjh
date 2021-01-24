#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/1/20 13:15 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司

"""
web页面的基本组成： HTML+CSS+JS（JavaScript）
html：定义页面的呈现的内容：标签语言 <>值</>
CSS:控制页面如何呈现--布局设置，字体颜色，字体大小
js：可以让页面在不同情形做不同事情
HTML页面：标签--属性

页面元素的定位：能唯一标识这个元素的内容
按照开发遵循原则的基础上-- 元素的属性里 id  name 唯一！！
id ：username
id: password
通过id name 可以找到这个元素。 大部分的元素没有的这两个属性，xpath ！
注意： 如果这个id是 变化的，不可以用来做元素定位！！

Xpath元素定位方法：
绝对路径：复制xpath：/html/body/div/div/div[1]/a/small   -从根开始，一级一级往下找-继承、顺序，
所以页面一旦发生变化，修改代码 ==不好用，用的少！
相对路径：//small     //*[@id="username"]  --- 以//开头的，不考虑兄弟，祖先，父亲，靠自己；
但是如果万一自己不行。偶尔靠亲戚。 --更多

Python三大等待：  一般当你打开新页面 （click操作之后），页面刷新时间 --等待
1、强制等待 --sleep（）： 设置等待时长没有到期，就算元素出现了，也还要等待；--速度慢
2、智能等待：
   1)隐性等待：默认等待时间，只要元素出现了，直接继续往执行 ==一个会话只执行一次
     默认等设置的时长，提前出现，提前执行；--- 有些地方不生效 + 强制等待
   2） 显示等待 -- 复杂 --了解

"""
from selenium import webdriver  # 从selenium这个工具里面导入webdriver这个库
import time
driver = webdriver.Chrome()   # 初始化一个浏览器  --会话session
driver.implicitly_wait(10)   # 隐性等待
driver.get("http://erp.lemfix.com")
driver.maximize_window()
# 获取页面的标题
page_title = driver.title
if page_title == "柠檬ERP":
    print("这个页面的标题：{}".format(page_title))
else:
    print("这个用例不通过！")

# 输入用户名 和密码  进行登录 操作
driver.find_element_by_id("username").send_keys("test123")   # 输入用户名
driver.find_element_by_id("password").send_keys("123456")   # 输入密码
driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
driver.find_element_by_id("btnSubmit").click()    # 点击登录按钮
# time.sleep(2)
# 确认登录用户名
page_name = driver.find_element_by_xpath("//p").text   # 获取这个元素的文本内容
if page_name == "测试用户":
    print("这个登录用户是：{}".format(page_name))
else:
    print("这个用例不通过！")

# 点击这个“零售出库”
'''
html里面 --嵌套了html -- 子页面，直接定位元素不会成功，先切换页面。
如何识别？ 1、 在页面里找子html； 2、识别路径-- 只要包含了iframe 
如何切换iframe子页面：
1、frame名字 -- 唯一标识 == id  name  ==多
2、元素定位识别 === 次
3、下标

'''
driver.find_element_by_xpath("//span[text()='零售出库']").click()
time.sleep(2)
# id 是变化的 不能直接使用！
# driver.switch_to.frame("tabpanel-8acbf12b8a-frame")
id_li= driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")   # 找到元素-获取id熟悉
id_frame = id_li + "-frame"   # 得到iframe id
# driver.switch_to.frame(id_frame)   # 通过iframe id进行iframe的切换
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_frame)))  # 通过web element切换子页面
# 接下来的操作就是针对子页面的操作
driver.find_element_by_id("searchNumber").send_keys("841")   # 找到搜索输入框
driver.find_element_by_id("searchBtn").click()  # 点击查询按钮
time.sleep(1)  # 隐式等待 + 强制等待的使用
# 获得单据编码的号码（文本）
num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
if "841" in num:
    print("搜索用例通过的！")
else:
    print("搜索失败！")






