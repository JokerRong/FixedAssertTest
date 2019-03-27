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
    driver.get("http://fixedassets.zosv2.develop.local")
    time.sleep(1)                                     
    driver.find_element_by_id("Username").clear()
    driver.find_element_by_id("Username").send_keys("SystemAdmin")
    driver.find_element_by_id("Password").clear()
    driver.find_element_by_id("Password").send_keys("Admin")
    driver.find_element_by_name("button").click()
    driver.implicitly_wait(20)
    time.sleep(2)

# 进入备品备件各个子功能界面
def enter_estate_planing(tabplace):
    time.sleep(1)
    driver.find_element_by_link_text("备品备件").click()
    time.sleep(2)
    div = driver.find_element_by_xpath("/html/body/main/div/div/div/section/div/div/div")
    span_list = div.find_elements_by_css_selector("span")
    span_list[int(tabplace)].find_element_by_xpath("./img").click()
    time.sleep(3)

#进入行政审批
def enter_Approve():
    time.sleep(2)
    driver.find_element_by_link_text("行政审批").click()
    time.sleep(2)


#click approve button
def approve_button(button):
    if button is True:
        driver.find_element_by_class_name("btn-success").click()
    else :
        driver.find_element_by_class_name("btn-danger").click()
    time.sleep(3)
      

# 点击上表格上边的按钮 
def click_top_button(place):
    time.sleep(2)
    ul_top_xpath = "/html/body/main/div/div/div/section/div/div/div/div[2]/div[1]/ul"
    ul_top = driver.find_element_by_xpath(ul_top_xpath)
    li_list_top = ul_top.find_elements_by_css_selector("li")
    driver.implicitly_wait(5)
    li_list_top[int(place)].find_element_by_xpath("./button").click()

# 点击盘点计划上表格上边的按钮
def click_top_button_plan(place):
    time.sleep(2)
    ul_top_xpath = "/html/body/main/div/div/div/section/div/div/div/div[3]/div[1]/ul"
    ul_top = driver.find_element_by_xpath(ul_top_xpath)
    li_list_top = ul_top.find_elements_by_css_selector("li")
    driver.implicitly_wait(5)
    li_list_top[int(place)].find_element_by_xpath("./button").click()

#approve button   
def click_button():
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/main/div/div/div/section/div/div/div/div[2]/div[1]/div/ul/li/button").click()
    time.sleep(2)

#check button
def click_check_button():
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/main/div/div/div/section/div/div/div/div[2]/div[1]/ul/li/button").click()
    time.sleep(2)

# 点击下表格上方的按钮 
def click_below_button(place):
    time.sleep(1)
    ul_below_xpath = "/html/body/main/div/div/div/section/div/div/div/div[6]/div/ul"
    ul_below = driver.find_element_by_xpath(ul_below_xpath)
    li_list_below = ul_below.find_elements_by_css_selector("li")
    driver.implicitly_wait(5)
    li_list_below[int(place)].find_element_by_xpath("./button").click()

# 点击盘点计划下表格上方的按钮 
def click_below_button_plan(place,button):
    time.sleep(2)
    get_below_table_data_in_plan(0)
    time.sleep(1)
    ul_below_xpath = "/html/body/main/div/div/div/section/div/div/div/div[7]/div/ul"
    ul_below = driver.find_element_by_xpath(ul_below_xpath)
    li_list_below = ul_below.find_elements_by_css_selector("li")
    driver.implicitly_wait(5)
    li_list_below[int(place)].find_element_by_xpath("./button").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/table/thead/tr/th[1]/input").click()
    time.sleep(2)
    if button is True:
        driver.find_element_by_class_name("btn-primary").click()
    else :
        driver.find_element_by_class_name("btn-danger").click()

# 新增采购申请明细中的数据  
def fill_form(button):  
    time.sleep(3)
    select_from_list_by_name("spareParts", "A01-01-002-0002")
    time.sleep(1)
    driver.find_element_by_name("quantity").click()
    driver.find_element_by_name("quantity").send_keys("5")
    if button is True:
        driver.find_element_by_class_name("btn-primary").click()
    else :
        driver.find_element_by_class_name("btn-danger").click()
    time.sleep(3)

# 新增盘点计划中的数据
def project(button):
    time.sleep(2)
    select_from_list_by_name("warehouse", "铺镇紧固件库")
    ul="/html/body/div[1]/div/div/div/div[2]/form/div[2]/div/div/textarea"
    driver.find_element_by_xpath(ul).click()
    driver.find_element_by_xpath(ul).send_keys("China is so beautiful ！！！！")
    time.sleep(1)
    if button is True:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()
    else:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[2]").click()

# 新增入库申请中入库的数据
def fill_form_laid(button):  
    time.sleep(3)
    select_from_list_by_name("warehouseInfo", "新区元器件库")
    time.sleep(2)
    get_below_table_data_in(0)
    time.sleep(2)
    tl="/html/body/div[1]/div/div/div/div[2]/div/div/div/div[5]/table/tbody/tr/td[9]/input"
    driver.find_element_by_xpath(tl).click()
    driver.find_element_by_xpath(tl).send_keys("4")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div/div[5]/table/thead/tr/th[2]/input").click()
    time.sleep(1)
    if button is True:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()
    else:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[2]").click()
    time.sleep(3)

# 物料收发中的入库
def send(button):
    time.sleep(2)
    get_below_table_data_out(0)
    time.sleep(1)
    if button is True:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[1]").click()
    else:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/button[2]").click()
    time.sleep(2)

# 新增采购申请上表格中的数据
def fill_plan_form(button):
    time.sleep(2)
    ul=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[4]/div/div")
    ul.click()
    time.sleep(1)
    driver.find_element_by_name("applicationCause").send_keys("请输入你的原因")
    time.sleep(1)
    if button is True:
        driver.find_element_by_class_name("btn-primary").click()
    else :
        driver.find_element_by_class_name("btn-danger").click()

# 选中表格列表中的数据 
def get_below_table_data(place):
   ul_xpath="/html/body/main/div/div/div/section/div/div/div/div[3]/table/tbody"
   ul=driver.find_element_by_xpath(ul_xpath)
   tr_list=ul.find_elements_by_css_selector("tr")
   driver.implicitly_wait(5)
   tr_list[int(place)].click()

# 选中表格列表中的数据(物料收发中入库)  /html/body/main/div/div/div/section/div[2]/div/div/div/div[2]/div[3]/table/tbody
def get_below_table_data_out(place):
   ul_xpath="/html/body/div[1]/div/div/div/div[2]/div[2]/table/tbody"
   ul=driver.find_element_by_xpath(ul_xpath)
   tr_list=ul.find_elements_by_css_selector("tr")
   driver.implicitly_wait(5)
   tr_list[int(place)].click()

# 选中入库表格中的数据  
def get_below_table_data_in(place):
   ul_xpath="/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/table/tbody"
   ul=driver.find_element_by_xpath(ul_xpath)
   tr_list=ul.find_elements_by_css_selector("tr")
   driver.implicitly_wait(5)
   tr_list[int(place)].click()

# 选中盘点计划表格中的数据  /html/body/main/div/div/div/section/div/div/div/div[4]/table/tbody
def get_below_table_data_in_plan(place):
   ul_xpath="/html/body/main/div/div/div/section/div/div/div/div[4]/table/tbody"
   ul=driver.find_element_by_xpath(ul_xpath)
   tr_list=ul.find_elements_by_css_selector("tr")
   driver.implicitly_wait(5)
   tr_list[int(place)].click()

# 审批
def department(opinion):
    enter_Approve()
    get_below_table_data(0)
    click_button()
    if opinion is True:
        driver.find_element_by_name("memo").click()
        driver.find_element_by_name("memo").send_keys("部门同意！！！")
    else:
        driver.find_element_by_name("memo").click()
        driver.find_element_by_name("memo").send_keys("公司同意啦！！！")
    time.sleep(3)
    approve_button(True)


# 通过下拉列表name选择参数
def select_from_list_by_name(name, value):
    time.sleep(0.5)
    outbox = driver.find_element_by_name(name)
    outbox.click()
    outbox.find_element_by_xpath("./input[1]").send_keys(value)
    time.sleep(0.5)
    outbox.find_element_by_xpath("./input[1]").send_keys(Keys.ENTER)

# 盘点处理
def ready(button):
    time.sleep(1)
    al="/html/body/div[1]/div/div/div/div[2]/div[1]/form/table/tbody/tr[1]/td[6]/input"
    driver.find_element_by_xpath(al).click()
    driver.find_element_by_xpath(al).send_keys("3")
    # bl="/html/body/div[1]/div/div/div/div[2]/div[1]/form/table/tbody/tr[2]/td[6]/input"
    # driver.find_element_by_xpath(bl).click()
    # driver.find_element_by_xpath(bl).send_keys("3")
    # cl="/html/body/div[1]/div/div/div/div[2]/div[1]/form/table/tbody/tr[3]/td[6]/input"
    # driver.find_element_by_xpath(cl).click()
    # driver.find_element_by_xpath(cl).send_keys("3")
    time.sleep(1)
    if button is True:
        driver.find_element_by_class_name("btn-primary").click()
    else :
        driver.find_element_by_class_name("btn-danger").click()
    time.sleep(3)