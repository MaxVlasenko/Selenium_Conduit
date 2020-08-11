from time import sleep

import pytest
from selenium import webdriver
from page import LoginPage

USER = {
    'login': 'kate198@gmail.com',
    'password': 'amid1516'
}

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(executable_path="c:/selenium/chromedriver.exe")
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


def test_article(driver):
    login_page = LoginPage(driver)
    login_page.login_as_registered_user(USER)

    new_post_link = driver.find_element_by_css_selector('#main > div > nav > div > ul > li:nth-child(2) > a');
    new_post_link.click()
    article_title_field = driver.find_element_by_css_selector(
        'form > fieldset > fieldset:nth-child(1) > input')
    article_title_field.send_keys("GB")
    about_article_field = driver.find_element_by_css_selector(
        'form > fieldset > fieldset:nth-child(2) > input')
    about_article_field.send_keys("about GB")
    article_field = driver.find_element_by_css_selector(
        'form > fieldset > fieldset:nth-child(3) > textarea')
    article_field.send_keys("London is a capital of GB")
    tag_field = driver.find_element_by_css_selector(
        'form > fieldset > fieldset:nth-child(4) > input')
    tag_field.send_keys("London")
    publish_article_button = driver.find_element_by_css_selector('form > fieldset > button')
    publish_article_button.click()
    sleep(4)
    edit_button = driver.find_element_by_css_selector('.banner > div > div > span > a')
    edit_button.click()
    sleep(4)
    article_title_field = driver.find_element_by_css_selector(
        'form > fieldset > fieldset:nth-child(1) > input')
    article_title_field.clear()
    article_title_field.send_keys("Great Britain")
    publish_article_button = driver.find_element_by_css_selector('form > fieldset > button')
    publish_article_button.click()

