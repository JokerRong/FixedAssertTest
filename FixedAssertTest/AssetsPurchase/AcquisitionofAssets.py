import traceback
import time
import Base


Base.login()

"""
进入资产购置界面，新增资产购置订单，新增购置信息，获得订单号
"""
code = ""
order_number = ""
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
