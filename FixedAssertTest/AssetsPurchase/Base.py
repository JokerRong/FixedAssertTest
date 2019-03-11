from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys
import traceback #获取错误信息 
from openpyxl import load_workbook

driver = webdriver.Chrome()
driver.maximize_window()


def login():
    driver.get("http://fixedassets.zosv2.develop.local")
    time.sleep(1)                                     
    driver.find_element_by_id("Username").clear()
    driver.find_element_by_id("Username").send_keys("SystemAdmin")
    driver.find_element_by_id("Password").clear()
    driver.find_element_by_id("Password").send_keys("Admin")
    driver.find_element_by_name("button").click()
    driver.implicitly_wait(20)
    time.sleep(3)


# 进入资产规划界面
def enter_estate_planing():
    driver.implicitly_wait(5)
    time.sleep(1)
    driver.find_element_by_link_text("资产购置").click()
    ul = driver.find_element_by_xpath("/html/body/main/div/div/div/section/div/div/div/div/div/ul")
    li_list = ul.find_elements_by_css_selector("li")
    li_list[0].find_element_by_xpath("./button").click()
    time.sleep(1)


# get assetPlanning top table data
def get_top_table_data(filepath):
    wb = load_workbook(filepath)
    sheet_Names = wb.sheetnames
    sheet = wb[sheet_Names[0]]
    record = {}
    
    # get planing_num
    plan_num = time.strftime("%Y%m%d%H%M", time.localtime())
    record['plan_num'] = plan_num
    
    # get ordername
    plan_name = random.randint(1, 200)
    plan_name = '名称' + str(plan_name)
    record['plan_name'] = plan_name

    # get using_department
    using_department = sheet['F2'].value
    record['using_department'] = using_department

    # get plan_type
    plan_type = sheet['B3'].value
    record['plan_type'] = plan_type

    # get plan_date
    plan_date = time.strftime("%Y-%m-%d", time.localtime())
    record['plan_date'] = plan_date

    # get use 
    use = "用途：测试 " + plan_name
    record['use'] = use
    return record
        

# get assetPlanning below table data
def get_below_table_data(filepath):
    wb = load_workbook(filepath)
    sheet_Names = wb.sheetnames
    sheet = wb[sheet_Names[0]]
    record = {}
    records = []
    # get maxrow 行
    total_num = sheet.max_row 
    for row in range(6, total_num+1):
        record['estate_name'] = sheet['A'+ str(row)].value
        record['specification'] = sheet['B' + str(row)].value
        record['estate_type'] = sheet['C' + str(row)].value
        record['number'] = sheet['D'+ str(row)].value
        record['budgetary_unit_price'] = sheet['E'+ str(row)].value
        if sheet['F' + str(row)].value is not None:
            record['supplier'] = sheet['F' + str(row)].value
        else:
            record['supplier'] = ''
        records.append(record)
        record = {}
    return records


# click the button above
def click_top_button(place):
    time.sleep(2)
    ul_top_xpath = "/html/body/main/div/div/div/section/div/div/div/div[2]/div[1]/ul"
    ul_top = driver.find_element_by_xpath(ul_top_xpath)
    li_list_top = ul_top.find_elements_by_css_selector("li")
    driver.implicitly_wait(5)
    li_list_top[int(place)].find_element_by_xpath("./button").click()


# click the botton below
def click_below_button(place):
    time.sleep(2)
    ul_below_xpath = "/html/body/main/div/div/div/section/div/div/div/div[6]/div/ul"
    ul_below = driver.find_element_by_xpath(ul_below_xpath)
    li_list_below = ul_below.find_elements_by_css_selector("li")
    driver.implicitly_wait(5)
    li_list_below[place].find_element_by_xpath("./button").click()


# fill plan form
def fill_plan_form(plan_data, button):
    time.sleep(2)
    form = driver.find_element_by_xpath("/html/body/div[1]/div/div/div")
    form.find_element_by_name("code").send_keys(plan_data['plan_num'])
    form.find_element_by_name("name").send_keys(plan_data['plan_name'])
    # department
    form.find_element_by_name("useDepartmentId").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[2]/div[1]/div/div/input[1]").send_keys(plan_data['using_department'])
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[2]/div[1]/div/div/input[1]").send_keys(Keys.ENTER)
    # type
    form.find_element_by_name("assetPlanningType").click()
    time.sleep(0.5)
    form.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[2]/div[2]/div/div/input[1]").send_keys(plan_data['plan_type'])
    form.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[2]/div[2]/div/div/input[1]").send_keys(Keys.ENTER)
    # date
    js = 'document.getElementsByName("planningDateTime")[0].removeAttribute("readonly");'
    driver.execute_script(js)
    driver.find_element_by_name("planningDateTime").send_keys(plan_data['plan_date'])
    # purpose
    form.find_element_by_name("mainPurpose").send_keys(plan_data['use'])

    if button is True:
        form.find_element_by_class_name("btn-primary").click()
    else :
        form.find_element_by_class_name("btn-danger").click()
    return plan_data['plan_num']


# input date 
def input_date(name, data):
    js = 'document.getElementsByName("' + name + '")[0].removeAttribute("readonly");' 
    driver.execute_script(js)
    driver.find_element_by_name("planningDateTime").send_keys(data)


# choose one line
def choose_one_line(code):
    driver.implicitly_wait(10)
    time.sleep(1)
    driver.find_element_by_xpath("//*[contains(text(),'"+ str(code) + "')]" ).click()
    

def fill_detail_table(record, button):
    time.sleep(1)
    driver.find_element_by_name("assetName").send_keys(record['estate_name'])
    driver.find_element_by_name("specificationModel").send_keys(record['specification'])
    driver.find_element_by_name("assetType").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[2]/div[1]/div/div/input[1]").send_keys(record['estate_type'])
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/div[2]/div[1]/div/div/input[1]").send_keys(Keys.ENTER)
    driver.find_element_by_name("purchaseQuantity").send_keys(record['number'])
    driver.find_element_by_name("unitPrice").send_keys(record['budgetary_unit_price'])
    
    if button is True:
        driver.find_element_by_class_name("btn-primary").click()
    else :
        driver.find_element_by_class_name("btn-danger").click()