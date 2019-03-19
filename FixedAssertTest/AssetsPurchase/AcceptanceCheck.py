import Base

Base.login()
# 进入资产验收界面
Base.enter_estate_planing(4)
code = "201903150001"
Base.choose_one_line(code)

tbody_xpath = "/html/body/main/div/div/div/section/div/div/div/div[6]/table/tbody"
tbody = Base.driver.find_element_by_xpath(tbody_xpath)
tr_list = tbody.find_elements_by_css_selector("tr")

# 开箱检验单
for number in range (0, len(tr_list)):
    Base.time.sleep(0.5)
    tbody = Base.driver.find_element_by_xpath(tbody_xpath)
    tr_list = tbody.find_elements_by_css_selector("tr")
    tr_list[number].click()
    Base.click_below_button(0, 1)
    Base.add_check_list()

# 安装验收单
filepath = "D:\\Fixedtest\\FixedAssertTest\\FixedAssertTest\\AssetsPurchase\\data\\1.jpeg"
for number in range (0, len(tr_list)):
    Base.time.sleep(0.5)
    tbody = Base.driver.find_element_by_xpath(tbody_xpath)
    tr_list = tbody.find_elements_by_css_selector("tr")
    tr_list[number].click()
    Base.click_below_button(1, 1)
    Base.install_list(number, filepath)