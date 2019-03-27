import traceback
import time
import Base

Base.login()

code = "201903261346"
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