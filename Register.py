from selenium import webdriver

name = "mandarin1111"
email = "gdfkkd@jdfdddjbfj.com"
password = "qwerngffgtyu"


def test1():
    driver = webdriver.Chrome()
    driver.get("https://react-redux.realworld.io/#/register?_k=0h18n4")
    driver.find_element_by_css_selector('[placeholder="Username"').send_keys(name)
    driver.find_element_by_css_selector('[placeholder="Email"').send_keys(email)
    driver.find_element_by_css_selector('[placeholder="Password"').send_keys(password)
    driver.find_element_by_css_selector('[Type="Submit"').click()
    time.sleep(5)
    driver.quit()


test1()