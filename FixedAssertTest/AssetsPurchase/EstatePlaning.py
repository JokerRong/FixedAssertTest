#  -*-coding:utf-8-*-
"""
资产规划新增、编辑、删除、提交评审、撤销提交
"""
import traceback
import time
import Base


Base.login()

Base.enter_estate_planing(0)
filepath = "D:\\Fixedtest\\FixedAssertTest\\FixedAssertTest\\AssetsPurchase\\data\\EstatePlanning.xlsx"


"""
资产购置-资产规划-新增资产规划单
"""
record_top = Base.get_top_table_data(filepath)
Base.click_top_button(0)
code = Base.fill_plan_form(record_top, True)
time.sleep(2)


"""
资产购置-资产规划-选择新增的资产规划单，新增规划明细
"""
record_below = Base.get_below_table_data(filepath)
while record_below:
    record = record_below.pop()
    Base.choose_one_line(code)
    Base.click_below_button(0)
    Base.fill_detail_table(record, True)


"""
提交新增的资产规划单
"""
Base.choose_one_line( code)
Base.click_top_button(3)


"""
进入资产购置-资产申购界面，通过规划调入新增申购单
"""
Base.enter_estate_planing(1)
Base.click_top_button(1)
order_number = Base.transfer_planing_bill(code , False, 6)

"""
提交新增的资产申购单
"""
Base.choose_one_line(code)
Base.click_top_button(6)


"""
进入资产购置界面，新增资产购置订单，新增购置信息，获得订单号
"""
Base.enter_estate_planing(3)
Base.click_top_button(0)
Base.add_order(code)
time.sleep(1)
Base.driver.find_element_by_xpath("/html/body/main/div/div/div/section/div/div/div/div[3]/table/thead/tr/th[2]").click()
time.sleep(1)

Base.choose_one_line(order_number)
Base.click_top_button(2)
upload_file_path = "D:\\Fixedtest\\FixedAssertTest\\FixedAssertTest\\AssetsPurchase\\data\\1.jpeg"
Base.fill_asset_acquisition_detail(upload_file_path)

"""
申请验收
"""
Base.choose_one_line(order_number)
Base.click_top_button(4)
time.sleep(1)
Base.driver.find_element_by_class_name("btn-primary").click()
