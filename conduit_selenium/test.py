from time import sleep

import pytest
from selenium import webdriver
from page import LoginPage, ArticlePage, SettingsPage, RegistrationPage, TestCase


class TestConduit(TestCase):
    USER = {
        'login': 'kate198@gmail.com',
        'password': 'amid1987'
    }

    def test_create_article(self):
        login_page = LoginPage(self.driver)
        article_page = ArticlePage(self.driver)
        login_page.login_as_registered_user(self.USER)
        sleep(4)
        new_post_link = self.driver.find_element_by_css_selector(
            'div[class = \'container\'] > ul > li:nth-child(2) > a');
        new_post_link.click()
        sleep(4)
        article_page.create_article()

    def test_update_article(self):
        login_page = LoginPage(self.driver)
        article_page = ArticlePage(self.driver)
        login_page.login_as_registered_user(self.USER)
        sleep(4)
        new_post_link = self.driver.find_element_by_css_selector(
            'div[class = \'container\'] > ul > li:nth-child(2) > a');
        new_post_link.click()
        sleep(4)
        article_page.create_article()
        sleep(4)
        edit_button = self.driver.find_element_by_css_selector('.banner > div > div > span > a')
        edit_button.click()
        sleep(4)
        article_page.update_article('Great Britain')

    def test_log_out(self):
        login_page = LoginPage(self.driver)
        login_page.login_as_registered_user(self.USER)
        sleep(4)
        settings_page = SettingsPage(self.driver)
        settings_page.log_out()

    def test_update_settings(self):
        login_page = LoginPage(self.driver)
        login_page.login_as_registered_user(self.USER)
        sleep(4)
        settings_page = SettingsPage(self.driver)
        settings_page.update_settings()

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login_as_registered_user(self.USER)

    def test_register(self):
        register_page = RegistrationPage(self.driver)
        register_page.register_user()
