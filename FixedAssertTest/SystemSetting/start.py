#  -*-coding:utf-8-*-
import sys
sys.path.append("D:\\Fixedtest\\FixedAssertTest\\Common")
import PubFunction
# from Common import PubFunction
import traceback

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