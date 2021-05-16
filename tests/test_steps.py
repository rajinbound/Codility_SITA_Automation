import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from Utilities.BaseClass import BaseClass
from pageObject.AutoPractice import AutoPractice

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestDemoQA(BaseClass):


    def test_empty_login(self, setup, getData):
        log = self.getLogger()
        #self.driver.get("https://codility-frontend-prod.s3.amazonaws.com/media/task_static/qa_login_page/9a83bda125cd7398f9f482a3d6d45ea4/static/attachments/reference_page.html")
        SITA = AutoPractice(self.driver)
        SITA.users_login().click()
        email_message = self.driver.find_element_by_xpath("//div[contains(text(),'Email is required')]").text
        assert email_message == "Email is required"
        password_message = self.driver.find_element_by_xpath("//div[contains(text(),'Password is required')]").text
        assert password_message == "Password is required"




    def test_unseccess_login(self, setup, getData):
        log = self.getLogger()
        #self.driver.get("https://codility-frontend-prod.s3.amazonaws.com/media/task_static/qa_login_page/9a83bda125cd7398f9f482a3d6d45ea4/static/attachments/reference_page.html")
        SITA = AutoPractice(self.driver)
        log.info("Entering the wrong email address")
        SITA.user_email().send_keys(getData[2])
        log.info("Entering password")
        SITA.user_password().send_keys(getData[1])
        log.info("Click on login button")
        SITA.users_login().click()
        #success = self.driver.find_element_by_class_name("message error").text
        #print(success)
        unsuccess_message = self.driver.find_element_by_xpath("//div[contains(text(),'You shall not pass! Arr!')]").text
        assert unsuccess_message == "You shall not pass! Arr!"


    def test_invalid_email_login(self, setup, getData):
        log = self.getLogger()
        #self.driver.get("https://codility-frontend-prod.s3.amazonaws.com/media/task_static/qa_login_page/9a83bda125cd7398f9f482a3d6d45ea4/static/attachments/reference_page.html")
        SITA = AutoPractice(self.driver)
        log.info("Entering invalid email address")
        SITA.user_email().clear()
        SITA.user_email().send_keys(getData[3])
        log.info("Entering password")
        SITA.user_password().clear()
        SITA.user_password().send_keys(getData[1])
        log.info("Click on login button")
        SITA.users_login().click()
        #success = self.driver.find_element_by_class_name("message success").text
        #print(success)
        success_invalid_email = self.driver.find_element_by_xpath("//div[contains(text(),'Enter a valid email')]").text
        assert success_invalid_email == "Enter a valid email"



    def test_success_login(self, setup, getData):
        log = self.getLogger()
        #self.driver.get("https://codility-frontend-prod.s3.amazonaws.com/media/task_static/qa_login_page/9a83bda125cd7398f9f482a3d6d45ea4/static/attachments/reference_page.html")
        SITA = AutoPractice(self.driver)
        log.info("Entering the email address")
        SITA.user_email().clear()
        SITA.user_email().send_keys(getData[0])
        log.info("Entering password")
        SITA.user_password().clear()
        SITA.user_password().send_keys(getData[1])
        log.info("Click on login button")
        SITA.users_login().click()
        #success = self.driver.find_element_by_class_name("message success").text
        #print(success)
        success = self.driver.find_element_by_xpath("//div[contains(text(),'Welcome to Codility')]").text
        assert success == "Welcome to Codility"




    # def test_element_presence(self, setup, getData):
    #     log = self.getLogger()
    #     #self.driver.get("https://codility-frontend-prod.s3.amazonaws.com/media/task_static/qa_login_page/9a83bda125cd7398f9f482a3d6d45ea4/static/attachments/reference_page.html")
    #     SITA = AutoPractice(self.driver)
    #     email_field_exist = len(SITA.user_email())
    #     password_field_exist = len(SITA.user_password())
    #     # get list size with len
    #     # check condition, if list size > 0, element exists
    #     if (email_field_exist > 0) and (password_field_exist > 0):
    #         email_field = "Email Field Present"
    #         password_field = "Password Field Present"
    #         print("Element exist -" + email_field)
    #         print("Element exist -" + password_field)
    #     else:
    #         print("Element does not exist")



    @pytest.fixture(params=[("login@codility.com", "password", "unknbown@codility.com", "dsafasfda@com")])
    def getData(self, request):
        return request.param
