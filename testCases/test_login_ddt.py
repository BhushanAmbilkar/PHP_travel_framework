import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert

from pageObjects.LoginPage import LoginPage
from utilities import XLutils
from utilities.Logger import LogGenerator
from utilities.ReadConfig import Readconfig


class Test_Login_DDT:
    url = Readconfig.URL()
    log = LogGenerator.loggen()
    path = "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\PhpTravel\\testCases\\TestData\\LoginData.xlsx"

    @pytest.mark.regression
    def test_login_ddt_04(self, setup):
        self.log.info("test_login_ddt_04 is started")
        self.driver = setup
        self.log.info("Opening Browser")
        self.lp = LoginPage(self.driver)
        self.driver.get(self.url)
        self.log.info("Going to Url -->" + str(self.url))
        self.lp = LoginPage(self.driver)

        self.row = XLutils.Rowcount(self.path, "Sheet1")
        print("Number of rows in sheet1 is-->" +  str(self.row))
        statusList = []
        for r in range(2, self.row + 1):
            self.Email = XLutils.ReadData(self.path, "Sheet1", r, 2)
            self.Password = XLutils.ReadData(self.path, "Sheet1", r, 3)
            self.exp_result = XLutils.ReadData(self.path, "Sheet1", r, 4)

            self.lp.EnterEmail(self.Email)
            self.log.info("Entering Email-->" + str(self.Email))
            self.lp.EnterPassword(self.Password)
            self.log.info("Entering Password-->" + self.Password)
            self.lp.ClickLogin()
            self.log.info("Clicking Login")
            self.lp.Alert()

            if self.lp.Title() == "Dashboard":
                if self.exp_result  == "Pass":
                    self.log.info("Page Title -->" + self.driver.title)
                    self.lp.ClickMenu()
                    self.log.info("Clicking Menu Button")
                    self.driver.save_screenshot(
                        "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\PhpTravel\\Screenshots"
                        "\\" + self.Email + self.Password + "test_login_Params_003_pass.PNG")
                    # time.sleep(2)
                    self.lp.ClickLogout()
                    self.log.info("Clicking Logout Button")
                    statusList.append("Pass")
                    XLutils.WriteData(self.path, "Sheet1", r, 5, "Pass")

                elif self.exp_result == "Fail":
                    self.log.info("Page Title -->" + self.driver.title)
                    self.lp.ClickMenu()
                    self.log.info("Clicking Menu Button")
                    self.driver.save_screenshot(
                        "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\PhpTravel\\Screenshots"
                        "\\" + self.Email + self.Password  + "test_login_Params_003_fail.PNG")
                    # time.sleep(2)
                    self.lp.ClickLogout()
                    self.log.info("Clicking Logout Button")
                    statusList.append("Fail")
                    XLutils.WriteData(self.path, "Sheet1", r, 5, "Fail")

            else:
                if self.exp_result == "Pass":
                    self.log.info("Page Title -->" + self.driver.title)
                    self.driver.save_screenshot(
                        "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\PhpTravel\\Screenshots"
                        "\\" + self.Email + self.Password  + "test_login_Params_003_fail.PNG")
                    statusList.append("Fail")
                    XLutils.WriteData(self.path, "Sheet1", r, 5, "Fail")

                elif self.exp_result == "Fail":
                    self.log.info("Page Title -->" + self.driver.title)
                    self.driver.save_screenshot(
                        "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\PhpTravel\\Screenshots"
                        "\\" + self.Email + self.Password  + "test_login_Params_003_pass.PNG")
                    statusList.append("Pass")
                    XLutils.WriteData(self.path, "Sheet1", r, 5, "Pass")
        print(statusList)
        if "Fail" not in statusList:
            assert True
            self.log.info("test_login_ddt_04 is Passed")
        else:
            self.log.info("test_login_ddt_04 is Failed")
            assert False
        self.log.info("test_login_ddt_04 is Completed")

