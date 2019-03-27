from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys
import traceback #获取错误信息 
from openpyxl import load_workbook

driver = webdriver.Chrome()
driver.maximize_window()

# 登陆
def login():
    driver.get("http://knowledgemanagement.zosv2.develop.local")
    time.sleep(1)                                     
    driver.find_element_by_id("Username").clear()
    driver.find_element_by_id("Username").send_keys("SystemAdmin")
    driver.find_element_by_id("Password").clear()
    driver.find_element_by_id("Password").send_keys("Admin")
    driver.find_element_by_name("button").click()
    driver.implicitly_wait(20)
    time.sleep(2)

# 进入题库管理

def subject():
    time.sleep(1)
    driver.find_element_by_link_text("题库管理").click()
    time.sleep(1)
    driver.find_element_by_id("1ff2a1d3-62eb-4b37-ad42-f8bf3e57dac7_anchor").click()
    time.sleep(1)
    driver.find_element_by_name("addLibrary").click() 
    time.sleep(1)
    driver.find_element_by_id("libraryNameForModel").click()
    driver.find_element_by_id("libraryNameForModel").send_keys("通用能力题库23")


# 点击确定按钮
def ensure_button(button):
    if button is True:
        driver.find_element_by_class_name("btn-primary").click()
    else:
        driver.find_element_by_class_name("btn-danger").click()

# 点击确定按钮
def ensure_button_m(button):
    if button is True:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()
    else:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[2]").click()

# 选中表格列表中的数据  
def get_below_table_data_out(place):
    time.sleep(2)
    ul_xpath="/html/body/main/div/div/div/section/div[2]/div/div/div/div[2]/div[3]/table/tbody"
    ul=driver.find_element_by_xpath(ul_xpath)
    tr_list=ul.find_elements_by_css_selector("tr")
    driver.implicitly_wait(5)
    tr_list[int(place)].click()

# 进入题目管理
def topic():
    time.sleep(3)
    #driver.find_element_by_xpath("/html/body/main/div/div/div/section/div[2]/div/div/div/div[2]/div[1]/div/ul/li[4]/button").click()
    driver.find_element_by_name("subjectsManagement").click()
    time.sleep(2)
   

def get_record(Filepath,sheet,cell):                       #定义函数
    workbook = load_workbook(Filepath)                     #打开指定的Excel文件
    worksheet = workbook.get_sheet_by_name(sheet)          #读取指定的sheet页
    record = worksheet[cell].value                         #将指定单元格的值赋值给record
    return record                                          #返回record值

# 单选题
def required():
    driver.find_element_by_name("addSubject").click()
    time.sleep(1)
    driver.find_element_by_name("subjectContent").click()
    driver.find_element_by_name("subjectContent").send_keys(get_record("D:/Fixedtest/FixedAssertTest/FixedAssertTest/TitleManage/subjectsManagement.xlsx","单选","A2"))
    driver.find_element_by_name("score").click()
    driver.find_element_by_name("score").send_keys("5")
    option()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()

# 单选题
def required1():
    time.sleep(1)
    driver.find_element_by_name("addSubject").click()
    driver.find_element_by_name("subjectContent").click()
    driver.find_element_by_name("subjectContent").send_keys(get_record("D:/QQdownload/subjectsManagement.xlsx","单选","A3"))
    # driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div/div[1]").click()
    # time.sleep(1)
    # driver.find_element_by_partial_link_text("中").click()
    # time.sleep(1)
    driver.find_element_by_name("score").click()
    driver.find_element_by_name("score").send_keys("5")
    option()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()

# 单选题
def required2():
    time.sleep(2)
    driver.find_element_by_name("addSubject").click()
    driver.find_element_by_name("subjectContent").click()
    driver.find_element_by_name("subjectContent").send_keys(get_record("D:/QQdownload/subjectsManagement.xlsx","单选","A4"))
    # driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div/div[1]").click()
    # time.sleep(1)
    # driver.find_element_by_id("ui-select-choices-row-31-2").click()
    # time.sleep(1)
    driver.find_element_by_name("score").click()
    driver.find_element_by_name("score").send_keys("5")
    option()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()

# 单选题
def required3():
    time.sleep(2)
    driver.find_element_by_name("addSubject").click()
    driver.find_element_by_name("subjectContent").click()
    driver.find_element_by_name("subjectContent").send_keys(get_record("D:/QQdownload/subjectsManagement.xlsx","单选","A5"))
    driver.find_element_by_name("score").click()
    driver.find_element_by_name("score").send_keys("5")
    option()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()

# 单选题
def required4():
    time.sleep(2)
    driver.find_element_by_name("addSubject").click()
    driver.find_element_by_name("subjectContent").click()
    driver.find_element_by_name("subjectContent").send_keys(get_record("D:/QQdownload/subjectsManagement.xlsx","单选","A6"))
    driver.find_element_by_name("score").click()
    driver.find_element_by_name("score").send_keys("5")
    option()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()

# 单选题
def required5():
    time.sleep(2)
    driver.find_element_by_name("addSubject").click()
    driver.find_element_by_name("subjectContent").click()
    driver.find_element_by_name("subjectContent").send_keys(get_record("D:/QQdownload/subjectsManagement.xlsx","单选","A7"))
    driver.find_element_by_name("score").click()
    driver.find_element_by_name("score").send_keys("5")
    option()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()

# 单选题
def required6():
    time.sleep(2)
    driver.find_element_by_name("addSubject").click()
    driver.find_element_by_name("subjectContent").click()
    driver.find_element_by_name("subjectContent").send_keys(get_record("D:/QQdownload/subjectsManagement.xlsx","单选","A8"))
    driver.find_element_by_name("score").click()
    driver.find_element_by_name("score").send_keys("5")
    option()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()

# 单选题
def required7():
    time.sleep(2)
    driver.find_element_by_name("addSubject").click()
    driver.find_element_by_name("subjectContent").click()
    driver.find_element_by_name("subjectContent").send_keys(get_record("D:/QQdownload/subjectsManagement.xlsx","单选","A9"))
    driver.find_element_by_name("score").click()
    driver.find_element_by_name("score").send_keys("5")
    option()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()


# 单选题
def required8():
    time.sleep(2)
    driver.find_element_by_name("addSubject").click()
    driver.find_element_by_name("subjectContent").click()
    driver.find_element_by_name("subjectContent").send_keys(get_record("D:/QQdownload/subjectsManagement.xlsx","单选","A10"))
    driver.find_element_by_name("score").click()
    driver.find_element_by_name("score").send_keys("5")
    option()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()

# 单选题
def required9():
    time.sleep(2)
    driver.find_element_by_name("addSubject").click()
    driver.find_element_by_name("subjectContent").click()
    driver.find_element_by_name("subjectContent").send_keys(get_record("D:/QQdownload/subjectsManagement.xlsx","单选","A11"))
    driver.find_element_by_name("score").click()
    driver.find_element_by_name("score").send_keys("5")
    option()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()

# 多选题
def chose():
    time.sleep(2)
    driver.find_element_by_name("addSubject").click()
    driver.find_element_by_name("subjectContent").click()
    driver.find_element_by_name("subjectContent").send_keys(get_record("D:/QQdownload/subjectsManagement.xlsx","单选","C2"))
    
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/form/div[2]/div[1]/div/div").click()
    time.sleep(3)
    driver.find_element_by_partial_link_text("多选题").click()
    
    driver.find_element_by_name("score").click()
    driver.find_element_by_name("score").send_keys("5")
    option()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()

# 选项和答案
def option():
    time.sleep(1)
    x=0
    while x<4:
      driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[2]/ul/button").click()
      x+=1
    driver.find_element_by_name("content").click()
    driver.find_element_by_name("content").send_keys("选项1")
    driver.find_element_by_name("answer").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/table/tbody/tr[1]/td[4]/form/button[1]").click()

    driver.find_element_by_name("content").click()
    driver.find_element_by_name("content").send_keys("选项2")
    driver.find_element_by_name("answer").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td[4]/form/button[1]").click()

    driver.find_element_by_name("content").click()
    driver.find_element_by_name("content").send_keys("选项3")
    driver.find_element_by_name("answer").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/table/tbody/tr[3]/td[4]/form/button[1]").click()

    driver.find_element_by_name("content").click()
    driver.find_element_by_name("content").send_keys("选项4")
    driver.find_element_by_name("answer").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/table/tbody/tr[4]/td[4]/form/button[1]").click()
















