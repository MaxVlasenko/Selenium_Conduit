from selenium import webdriver
import time
email = "deltaaa@gmail.com"
password = 1234567890


def test1():
    driver = webdriver.Chrome()
    driver.get("https://react-redux.realworld.io/#/?_k=x56v6i")
    driver.find_element_by_css_selector('[href="#login"]').click()
    driver.find_element_by_css_selector('[placeholder="Email"').send_keys(email)
    driver.find_element_by_css_selector('[placeholder="Password"').send_keys(password)
    driver.find_element_by_css_selector('[Type="Submit"').click()
    time.sleep(1)
    driver.find_element_by_css_selector('[href="#@deltateam"]').click()
    driver.find_element_by_css_selector('[href="#settings"]').click()
    driver.find_element_by_css_selector('[placeholder="Username"]').clear()
    driver.find_element_by_css_selector('[placeholder="Username"]').send_keys("Arnold")
    driver.find_element_by_css_selector('[placeholder="Short bio about you"]').clear()
    driver.find_element_by_css_selector('[placeholder="Short bio about you"]').send_keys("Mr.Olimpia")
    driver.find_element_by_css_selector('[placeholder="New Password"]').send_keys("qwertyqwerty")
    driver.find_element_by_css_selector('[Type="Submit"').click()
    driver.quit()


test1()