# -*-coding:utf-8-*-
import os 
import traceback
import time
from selenium import webdriver
ProgramPerform = [0,0] #程序执行个数，第一位为成功个数，第二位为失败个数
driver = webdriver.Chrome()#打开谷歌浏览器
driver.maximize_window()#最大化窗口
driver.implicitly_wait(10)#隐形等待
sleep_time = [0.5,1,1.5,2]  #等待页面加载的时间

#系统日志函数    
def log(logContent , filePath):
    fopen = open ( "D:\\Fixedtest\\FixedAssertTest\\Log\\"+ filePath +"\\log.txt" ,'a')
    fopen.write (logContent +"   " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "\n" )
    fopen.close()
    print(logContent + "   " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) )
    return None


#系统登录函数
def Login(username, password, file_path, url):
    """
    :param username: 用户名称
    :param password: 登录密码
    :param file_path: 存储log的文件夹名称
    :param url: 登录网址
    :return: 登录成功与否状态信息
    """
    driver.get(url)
    time.sleep(sleep_time[1])
    try:
        driver.find_element_by_id("Username").clear()
    except:
        pass
    try:
        driver.find_element_by_name("Password").clear()
    except:
        pass

    # 判断用户名或者密码是否为空
    if username is None:
        username = ""
    if password is None:
        password = ""
        
    driver.find_element_by_id("Username").send_keys(username)
    driver.find_element_by_id("Password").send_keys(password)
    driver.find_element_by_name("button").click()
   
    time.sleep(sleep_time[1])
    try :
        # 如果登录成功，界面会显示该图标
        driver.find_element_by_xpath("/html/body/main/page-top/div/a[1]/img")
        log_content = "用户:  " + username + "  登录成功"
        log(log_content, file_path)
    except:
        # 有警告的情况下得到警示内容
        log_content = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/ul/li").text
        time.sleep(sleep_time[1])
        # 关闭警示 点击“关闭”按钮
        log(log_content + "   登录失败", file_path)
    return log_content


#菜单导航函数
def MenuLocate(file_path, level_2="", level_1=""):
    if level_1 is not "":
        driver.find_element_by_link_text(level_1).click()
        time.sleep(sleep_time[3])#等待页面加载-2s
    if level_2 is not "":
        driver.find_element_by_link_text(level_2).click()
        time.sleep(sleep_time[1])#等待页面加载-1s

    log_content = "进入" + level_1 + "-" + level_2 + "界面"
    log(log_content, file_path)
    return None

#Tab切换函数
def TabSwitch(file_path, tab_name=""):
    driver.find_element_by_link_text(tab_name).click()
    time.sleep(sleep_time[1])
    log_content = "进入" + tab_name + "界面"
    log(log_content, file_path)
    return None    


