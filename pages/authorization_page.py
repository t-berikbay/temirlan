import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random

login_button = (By.ID, 'login-button')
username_field = (By.ID, 'user-name')
password_field = (By.ID, 'password')

users = ['standard_user'], ['visual_user']
random_user = random.choice(users)


class AuthorizationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.saucedemo.com')

    ####################################################################

    def login_button(self):
        return self.find(login_button)

    ####################################################################

    def username(self):
        return self.find(username_field)

    def username_click(self):
        return self.username().click

    def username_send(self):
        return self.username().send_keys(random_user)

    ####################################################################

    def password(self):
        return self.find(password_field)

    def password_click(self):
        return self.password().click

    def password_send(self):
        return self.password().send_keys('secret_sauce')