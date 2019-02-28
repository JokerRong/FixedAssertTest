#  -*-coding:utf-8-*-
import sys
sys.path.append("D:\\Fixedtest\\FixedAssertTest\\Common")
import PubFunction
# from Common import PubFunction
import traceback
import time

logContents = "+++++++++++++++++++++++++ begin"
PubFunction.log(logContents, "SystemSetting")

try:
    log_url = "http://fixedassets.zosv2.develop.local"
    logContents = PubFunction.Login("SystemAdmin", "Admin", "SystemSetting", log_url)
    PubFunction.ProgramPerform[0] += 1
except:
    fopen = open("D:\\Fixedtest\\FixedAssertTest\\Log\\SystemSetting\\log.txt")
    logContents = "登录失败"
    PubFunction.log(logContents, "SystemSetting")
    traceback.print_exc(file=fopen)
    traceback.print_exc()
    fopen.close()
    PubFunction.ProgramPerform[1] += 1


"""
基础参数配置
"""
# time.sleep(2)
num = 0
for num in range(0,17):
    if num in {9,12,13,16,17}:
        num += 1
    else:
        time.sleep(1)
        PubFunction.driver.find_element_by_link_text("参数配置").click()
        ul = PubFunction.driver.find_element_by_xpath("/html/body/main/div/div/div/section/div/div/div/div/div/ul")
        li_list = ul.find_elements_by_css_selector("li")
        li_list[num].find_element_by_xpath("./button").click()

        time.sleep(0.5)
        PubFunction.driver.find_element_by_class_name("ion-plus-round").click()
        time.sleep(0.5)
        name = PubFunction.driver.find_element_by_xpath("/html/body/main/div/div/content-top/div/ul/li").text
        PubFunction.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[1]/div/div/input").click()
        PubFunction.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[1]/div/div/input").send_keys("001")
        PubFunction.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[2]/div/div/input").click()
        PubFunction.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[2]/div/div/input").send_keys( name + "1")
        PubFunction.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()
        # PubFunction.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[2]").click()
        
        time.sleep(1)
        PubFunction.driver.find_element_by_class_name("ion-plus-round").click()
        time.sleep(0.5)
        PubFunction.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[1]/div/div/input").send_keys("002")
        PubFunction.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[2]/div/div/input").send_keys( name + "2")
        PubFunction.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()
        # PubFunction.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[2]").click()

    

