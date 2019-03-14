import Base

# 资产入账
Base.login()
Base.enter_estate_planing(5)
tbody_xpath = "/html/body/main/div/div/div/section/div/div/div/div[3]/table/tbody"
tbody = Base.driver.find_element_by_xpath(tbody_xpath)
tr_list = tbody.find_elements_by_css_selector("tr")
tr_top_xpath = "/html/body/main/div/div/div/section/div/div/div/div[3]/table/tbody/tr[1]/td[2]"
tr_top = Base.driver.find_element_by_xpath(tr_top_xpath)

while len(tr_list) > 0:
    Base.time.sleep(0.5)
    tr_top = Base.driver.find_element_by_xpath(tr_top_xpath)
    tr_top.click()
    Base.click_top_button(0)
    Base.time.sleep(0.25)
    tr_list = tbody.find_elements_by_css_selector("tr")
    