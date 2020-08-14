from time import sleep

from faker import Faker
from page import LoginPage, ArticlePage, SettingsPage, RegistrationPage, TestCase


class TestArticle(TestCase):

    def test_create_article(self):
        login_page = LoginPage(self.driver)
        article_page = ArticlePage(self.driver)
        login_page.login_as_registered_user(self.USER)
        sleep(4)
        article_page.create_article()

    def test_update_article(self):
        login_page = LoginPage(self.driver)
        article_page = ArticlePage(self.driver)
        login_page.login_as_registered_user(self.USER)
        sleep(4)
        article_page.create_article()
        sleep(4)
        edit_button = self.driver.find_element_by_css_selector('.banner > div > div > span > a')
        edit_button.click()
        sleep(4)
        article_page.update_article()

    def test_delete_article(self):
        login_page = LoginPage(self.driver)
        article_page = ArticlePage(self.driver)
        login_page.login_as_registered_user(self.USER)
        sleep(4)
        article_page.create_article()
        sleep(4)
        delete_button = self.driver.find_element_by_css_selector('.banner > div > div > span > button')
        delete_button.click()
        sleep(4)


class TestComment(TestCase):

    def test_post_comment(self):
        login_page = LoginPage(self.driver)
        article_page = ArticlePage(self.driver)
        login_page.login_as_registered_user(self.USER)
        sleep(4)
        article_page.create_article()
        sleep(4)
        article_page.create_comment()

    def test_delete_comment(self):
        login_page = LoginPage(self.driver)
        article_page = ArticlePage(self.driver)
        login_page.login_as_registered_user(self.USER)
        sleep(4)
        article_page.create_article()
        sleep(4)
        article_page.create_comment()
        sleep(4)
        trash = self.driver.find_element_by_css_selector('i[class = "ion-trash-a"]')
        trash.click()


class TestSettings(TestCase):

    def test_update_settings(self):
        login_page = LoginPage(self.driver)
        login_page.login_as_registered_user(self.USER)
        sleep(4)
        settings_page = SettingsPage(self.driver)
        settings_page.update_settings()


class TestLog(TestCase):

    def test_log_out(self):
        login_page = LoginPage(self.driver)
        login_page.login_as_registered_user(self.USER)
        sleep(4)
        settings_page = SettingsPage(self.driver)
        settings_page.log_out()

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login_as_registered_user(self.USER)


class TestRegister(TestCase):

    def test_register(self):
        register_page = RegistrationPage(self.driver)
        register_page.register_user()
