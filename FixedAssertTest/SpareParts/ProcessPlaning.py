#  -*-coding:utf-8-*-
"""
资产规划新增、编辑、删除、提交评审、撤销提交
"""
import traceback
import time
import Basics

'''
登陆系统
'''
Basics.login()

"""
备品备件-采购申请-新增采购申请
"""
Basics.enter_estate_planing(0)
Basics.click_top_button(0)
Basics.fill_plan_form(True)
time.sleep(2)


"""
备品备件-采购申请-选择新增的采购申请，新增采购明细
"""
Basics.get_below_table_data(0)
Basics.click_below_button(0)
Basics.fill_form(True)


"""
提交新增的采购申请单
"""
Basics.get_below_table_data(0)
Basics.click_top_button(4)


"""
部门审批
"""
Basics.department(True)


"""
公司审批
"""
Basics.department(False)


"""
备品备件-采购验收
"""
Basics.enter_estate_planing(1)
Basics.get_below_table_data(0)
Basics.click_check_button()


'''
备品备件-入库申请
'''
Basics.enter_estate_planing(2)
Basics.click_top_button(0)
Basics.fill_form_laid(True)

"""
提交新增的入库申请单
"""
Basics.get_below_table_data(0)
Basics.click_top_button(2)


"""
部门审批
"""
Basics.department(True)


"""
公司审批
"""
Basics.department(False)

'''
备品备件-物料收发
'''
Basics.enter_estate_planing(4)
Basics.click_top_button(0)
Basics.send(True)

'''
备品备件-盘点计划
'''
Basics.enter_estate_planing(5)
Basics.click_top_button_plan(0)
Basics.project(True)
Basics.click_below_button_plan(0,True)
Basics.click_top_button_plan(3)

"""
部门审批
"""
Basics.department(True)

"""
公司审批
"""
Basics.department(False)

'''
备品备件-盘点处理-盘后输入
'''
Basics.enter_estate_planing(6)
Basics.get_below_table_data(0)
Basics.click_top_button(0)
Basics.ready(True)

'''
备品备件-盘点处理-平账审批
'''
Basics.get_below_table_data(0)
Basics.click_top_button(1)

"""
部门审批
"""
Basics.department(True)

"""
公司审批
"""
Basics.department(False)