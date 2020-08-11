from time import sleep

import pytest
from selenium import webdriver
from page import LoginPage, ArticlePage

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
    article_page = ArticlePage(driver)
    login_page.login_as_registered_user(USER)
    sleep(4)
    new_post_link = driver.find_element_by_css_selector('div[class = \'container\'] > ul > li:nth-child(2) > a');
    new_post_link.click()
    sleep(4)
    article_page.create_article()
    sleep(4)
    edit_button = driver.find_element_by_css_selector('.banner > div > div > span > a')
    edit_button.click()
    sleep(4)
    article_page.update_article('Great Britain')


