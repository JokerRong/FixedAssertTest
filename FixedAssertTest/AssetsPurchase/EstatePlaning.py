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

