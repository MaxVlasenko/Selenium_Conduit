from time import sleep

from selenium.common.exceptions import NoSuchElementException
from faker import Faker
from selenium import webdriver

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, path):
        self.driver.get(path)

    def check_exists_by_css_selector(self, css):
        try:
            self.driver.find_element_by_css_selector(css)
        except NoSuchElementException:
            return False
        return True


class TestCase(object):
    driver = None

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path="c:/selenium/chromedriver.exe")
        self.driver.set_window_size(1920, 1080)

    def teardown_method(self):
        self.driver.quit()


class LoginPage(BasePage):
    setting_selector = '[href="#settings"]'
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
        sleep(4)
        assert self.check_exists_by_css_selector(self.setting_selector)


class ArticlePage(BasePage):
    article_title_field_selector = 'form > fieldset > fieldset:nth-child(1) > input'
    about_article_field_selector = 'form > fieldset > fieldset:nth-child(2) > input'
    article_field_selector = 'form > fieldset > fieldset:nth-child(3) > textarea'
    tag_field_selector = 'form > fieldset > fieldset:nth-child(4) > input'
    write_comment_field = 'form > div:nth-child(1) > textarea[placeholder="Write a comment..."]'
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
        sleep(4)
        assert self.check_exists_by_css_selector(self.write_comment_field)

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


class SettingsPage(BasePage):
    setting_selector = '[href="#settings"]'
    log_out_button_selector = '.btn.btn-outline-danger'
    short_bio_selector = '[placeholder="Short bio about you"]'
    new_password_selector = '[placeholder="New Password"]'
    user_name_selector = '[placeholder="Username"]'
    submit_button_selector = '[Type="Submit"]'
    sign_in_selector = 'a[href = "#login"]'
    user_name_element = '.container > ul > li:nth-child(4) > a'
    faker = Faker()

    def log_out(self):
        self.driver.find_element_by_css_selector(self.setting_selector).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_css_selector(self.log_out_button_selector).click()
        sleep(4)
        assert self.check_exists_by_css_selector(self.sign_in_selector)

    def update_settings(self):
        self.driver.find_element_by_css_selector(self.setting_selector).click()
        user_name_field = self.driver.find_element_by_css_selector(self.user_name_selector)
        user_name_field.clear()
        faker_name = self.faker.name()
        user_name_field.send_keys(faker_name)
        short_bio_field = self.driver.find_element_by_css_selector(self.short_bio_selector)
        short_bio_field.clear()
        short_bio_field.send_keys(self.faker.text())
        password_field = self.driver.find_element_by_css_selector(self.new_password_selector)
        password_field.clear()
        self.driver.find_element_by_css_selector(self.submit_button_selector).click()
        sleep(4)
        user_name_element = self.driver.find_element_by_css_selector(self.user_name_element)
        assert user_name_element.text == faker_name


class RegistrationPage(BasePage):
    sign_up_selector = 'a[href="#register"]'
    user_name_selector = 'input[placeholder="Username"]'
    email_selector = 'input[placeholder="Email"]'
    password_selector = 'input[placeholder="Password"]'
    submit_button_selector = 'button[Type="Submit"]'
    setting_selector = '[href="#settings"]'
    user_name = 'Dima1997'
    user_password = 'amid1516'
    faker = Faker()

    def register_user(self):
        self.open("https://react-redux.realworld.io/#/?_k=yawtxs")
        self.driver.find_element_by_css_selector(self.sign_up_selector).click()
        self.driver.find_element_by_css_selector(self.user_name_selector).send_keys(self.user_name)
        self.driver.find_element_by_css_selector(self.email_selector).send_keys(self.faker.safe_email())
        self.driver.find_element_by_css_selector(self.password_selector).send_keys(self.user_password)
        self.driver.find_element_by_css_selector(self.submit_button_selector).click()
        sleep(4)
        assert self.check_exists_by_css_selector(self.setting_selector)
