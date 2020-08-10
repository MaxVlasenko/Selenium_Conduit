from selenium import webdriver

name = "mandarin122111"
email = "gdf2kkd@jdfdddjbfj.com"
password = "qwerngffgtyu"


def test1():
    driver = webdriver.Chrome()
    driver.get("https://react-redux.realworld.io/#/?_k=x56v6i")
    driver.find_element_by_css_selector('[href="#register"]').click()
    driver.find_element_by_css_selector('[placeholder="Username"').send_keys(name)
    driver.find_element_by_css_selector('[placeholder="Email"').send_keys(email)
    driver.find_element_by_css_selector('[placeholder="Password"').send_keys(password)
    driver.find_element_by_css_selector('[Type="Submit"').click()

    driver.quit()


test1()
