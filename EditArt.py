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
    time.sleep(2)
    driver.find_element_by_css_selector('[href="#@deltateam"]').click()
    time.sleep(2)
    driver.find_element_by_css_selector('[href="#article/delta-team-article-4pbdfh"]').click()
    time.sleep(2)
    driver.find_element_by_css_selector('[href="#/editor/delta-team-article-4pbdfh"]').click()
    time.sleep(2)
    driver.find_element_by_css_selector('[placeholder="Article Title"]').send_keys(' TestDelta1')
    time.sleep(1)
    driver.find_element_by_css_selector('[type="button"]').click()
    driver.quit()

test1()