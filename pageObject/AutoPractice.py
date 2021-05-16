import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


#@pytest.fixture(scope="class")
class AutoPractice:


    def __init__(self, driver):
        self.driver = driver


    email = (By.ID, "email-input")
    password = (By.ID, "password-input")
    login_button = (By.ID, "login-button")


    def user_email(self):
        return self.driver.find_element(*AutoPractice.email)


    def user_password(self):
        return self.driver.find_element(*AutoPractice.password)


    def users_login(self):
        return self.driver.find_element(*AutoPractice.login_button)
