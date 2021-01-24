#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/1/22 21:12 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司

# 打开浏览器函数
import time
def open_url(driver,url):
    driver.get(url)
    driver.maximize_window()

# 登录函数
def login_fun(driver,username,password):
    driver.find_element_by_id("username").send_keys(username)  # 输入用户名
    driver.find_element_by_id("password").send_keys(password)  # 输入密码
    driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
    driver.find_element_by_id("btnSubmit").click()

# 搜索函数
def sear_fun(driver,url,username,password,key):
    open_url(driver,url)
    login_fun(driver,username,password)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    time.sleep(2)
    id_li= driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")   # 找到元素-获取id熟悉
    id_frame = id_li + "-frame"   # 得到iframe id
    driver.switch_to.frame(id_frame)   # 通过iframe id进行iframe的切换
    driver.find_element_by_id("searchNumber").send_keys(key)   # 找到搜索输入框
    driver.find_element_by_id("searchBtn").click()  # 点击查询按钮
    time.sleep(1)
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num
