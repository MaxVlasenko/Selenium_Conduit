from selenium import webdriver

email = "deltaaa@gmail.com"
password = 1234567890


def test1():
    driver = webdriver.Chrome()
    driver.get("https://react-redux.realworld.io/#/login?_k=o7rt7x")
    driver.find_element_by_css_selector('[placeholder="Email"').send_keys(email)
    driver.find_element_by_css_selector('[placeholder="Password"').send_keys(password)
    driver.find_element_by_css_selector('[Type="Submit"').click()
    driver.quit()


test1()