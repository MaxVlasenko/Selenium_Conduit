from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, path):
        self.driver.get(path)

class LoginPage(BasePage):
    login_link_selector = 'a[href = \'#login\']'
    email_field_selector = '.form-group > input[type = \'email\']'
    login_field_selector = '.form-group > input[type = \'password\']'
    subm_button_selector = 'button[type = \'submit\']'

    def login_as_registered_user(self, user_data):
        self.open("https://react-redux.realworld.io/#/?_k=yawtxs")
        login_link = self.driver.find_element_by_css_selector(self.login_link_selector)
        login_link.click()
        email_field = self.driver.find_element_by_css_selector(self.email_field_selector);
        email_field.send_keys(user_data['login'])
        login_field = self.driver.find_element_by_css_selector(self.login_field_selector);
        login_field.send_keys(user_data['password'])
        subm_button = self.driver.find_element_by_css_selector(self.subm_button_selector);
        subm_button.click();

class ArticlePage(BasePage):
    article_title_field_selector = 'form > fieldset > fieldset:nth-child(1) > input'
    about_article_field_selector = 'form > fieldset > fieldset:nth-child(2) > input'
    article_field_selector = 'form > fieldset > fieldset:nth-child(3) > textarea'
    tag_field_selector = 'form > fieldset > fieldset:nth-child(4) > input'
    publish_article_button = 'form > fieldset > button'
    article_title_field = 'GB'
    about_article_field = 'about GB'
    article_field = 'London is a capital of GB'
    tag_field = 'London'

    def create_article(self):
        article_title_field = self.driver.find_element_by_css_selector(
            self.article_title_field_selector)
        article_title_field.send_keys(self.article_title_field)
        about_article_field = self.driver.find_element_by_css_selector(
            self.about_article_field_selector)
        about_article_field.send_keys(self.about_article_field)
        article_field = self.driver.find_element_by_css_selector(
            self.article_field_selector)
        article_field.send_keys(self.article_field)
        tag_field = self.driver.find_element_by_css_selector(
            self.tag_field_selector)
        tag_field.send_keys(self.tag_field)
        publish_article_button = self.driver.find_element_by_css_selector(self.publish_article_button)
        publish_article_button.click()

    def update_article(self, article_title):
        self.article_title_field = article_title
        article_title_field = self.driver.find_element_by_css_selector(
            self.article_title_field_selector)
        article_title_field.clear()
        article_title_field.send_keys(self.article_title_field)
        publish_article_button = self.driver.find_element_by_css_selector(self.publish_article_button)
        publish_article_button.click()
        sleep(4)
        article_title_label = self.driver.find_element_by_css_selector('.banner > div > h1')
        assert article_title == article_title_label.text




