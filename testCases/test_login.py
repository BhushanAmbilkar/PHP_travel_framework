import time

import allure
from allure_commons.types import AttachmentType
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert

from pageObjects.LoginPage import LoginPage
from utilities.Logger import LogGenerator
from utilities.ReadConfig import Readconfig


class Test_Login:
    url = Readconfig.URL()
    email = Readconfig.Email()
    password = Readconfig.Password()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Valid Credentials")
    @allure.issue("ABC-123")
    @allure.title("Test Page Title")
    def test_page_title_001(self, setup):
        self.log.info("test_page_title_001 is started")
        self.driver = setup
        self.log.info("Opening Browser")
        self.lp = LoginPage(self.driver)
        self.driver.get(self.url)
        self.log.info("Going to Url -->" + self.url)
        if self.driver.title == "Administator Login":
            self.log.info("Page Title -->" + self.driver.title)
            self.driver.save_screenshot(
                "F:\\05.FrameWork\\MZR\\PHP_Travel\\PhpTravel\\Screenshots"
                "\\test_page_title_001_pass.PNG")
            assert True
            self.log.info("test_page_title_001 is Passed")
        else:
            self.log.info("Page Title -->" + self.driver.title)
            self.log.info("test_page_title_001 is Failed")
            self.driver.save_screenshot(
                "F:\\05.FrameWork\\MZR\\PHP_Travel\\PhpTravel\\Screenshots"
                "\\test_page_title_001_fail.PNG")
            assert False
        self.log.info("test_page_title_001 is Completed")

    @pytest.mark.sanity
    @allure.description("This test case verfying login fucntionality of the application")
    @allure.link(" https://phptravels.net/api/admin")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_002(self, setup):
        self.log.info("test_login_002 is started")
        self.driver = setup
        self.log.info("Opening Browser")
        self.lp = LoginPage(self.driver)
        self.driver.get(self.url)
        self.log.info("Going to Url -->" + str(self.url))
        self.lp = LoginPage(self.driver)
        self.lp.EnterEmail(self.email)
        self.log.info("Entering Email-->" + str(self.email))
        self.lp.EnterPassword(self.password)
        self.log.info("Entering Password-->" + self.password)
        self.lp.ClickLogin()
        self.log.info("Clicking Login")
        self.lp.Alert()
        if self.lp.Title() == "Dashboard":
            self.log.info("Page Title -->" + self.driver.title)
            self.lp.ClickMenu()
            self.log.info("Clicking Menu Button")
            self.driver.save_screenshot(
                "F:\\05.FrameWork\\MZR\\PHP_Travel\\PhpTravel\\Screenshots"
                "\\test_login_002_pass.PNG")
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

            # time.sleep(2)
            self.lp.ClickLogout()
            self.log.info("Clicking Logout Button")
            assert True
            self.log.info("test_login_002 is Passed")
        else:
            self.log.info("Page Title -->" + self.driver.title)
            self.driver.save_screenshot(
                "F:\\05.FrameWork\\MZR\\PHP_Travel\\PhpTravel\\Screenshots"
                "\\test_login_002_fail.PNG")
            assert False
            self.log.info("test_login_002 is Failed")
        self.log.info("test_login_002 is Completed")
