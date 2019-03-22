#  -*-coding:utf-8-*-

import traceback
import time


from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://fixedassets.zosv2.develop.local")
time.sleep(1)
try:                                        
    driver.find_element_by_id("Username").clear()
except:
    pass
driver.find_element_by_id("Username").send_keys("SystemAdmin")
driver.find_element_by_id("Password").clear()
driver.find_element_by_id("Password").send_keys("Admin")
driver.find_element_by_name("button").click()
time.sleep(3)
"""
基础参数配置
"""
time.sleep(2)
num = 0
for num in range(0,17):
    if num in {9,12,13,16,17}:
        pass
    else:
        time.sleep(1)
        driver.find_element_by_link_text("参数配置").click()
        ul = driver.find_element_by_xpath("/html/body/main/div/div/div/section/div/div/div/div/div/div")
        div_list = ul.find_elements_by_css_selector("div")
        driver.implicitly_wait(10)
        time.sleep(2)
        div_list[num].click()

        time.sleep(0.5)
        driver.find_element_by_class_name("ion-plus-round").click()
        time.sleep(0.5)
        name =driver.find_element_by_xpath("/html/body/main/div/div/content-top/div/ul/li").text
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[1]/div/div/input").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[1]/div/div/input").send_keys("001")
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[2]/div/div/input").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[2]/div/div/input").send_keys( name + "1")
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()
        # driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[2]").click()
        
        time.sleep(1.5)
        driver.find_element_by_class_name("ion-plus-round").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[1]/div/div/input").send_keys("002")
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[2]/div/div/input").send_keys( name + "2")
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()
        # driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[2]").click()

    

