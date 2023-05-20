import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.Add_Customer import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.Logger import LogGenerator
from utilities.ReadConfig import Readconfig


class Test_Login:
    url = Readconfig.URL()
    email = Readconfig.Email()
    password = Readconfig.Password()
    log = LogGenerator.loggen()


    def test_addcustomer_005(self, setup):
        self.log.info("test_addcustomer_005 is started")
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
        self.ac = AddCustomer(self.driver)
        time.sleep(3)
        # self.ac.Click_Accounts()
        # time.sleep(3)
        # self.ac.Click_Customer()
        # time.sleep(3)
        # self.ac.Click_Add()
        time.sleep(3)
        self.ac.Url_Add_Customer()
        time.sleep(2)
        self.ac.Enter_FirstName("Credence")
        self.ac.Enter_lastName("It")
        self.ac.Enter_Email("Credence@credence.in")
        self.ac.Enter_Password("Credence@Pune123")
        self.ac.Enter_MobileNumber("9091929355")
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//a[@class ='select2-choice']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[1]/input[1]").send_keys("India")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//body/div[@id='layoutDrawer']/div[@id='layoutDrawer_content']/main/div[@class='container-xl p-4']/form[@class='row']/div[@class='row gx-3']/div[@class='col-lg-8']/div[@class='card card-raised mb-5']/div[@class='card-body p-5']/div[1]").click

        # Country = Select(self.driver.find_element(By.XPATH, "//select[@class ='chosen-select select2-offscreen']"))
        # Country.select_by_index(2)
        time.sleep(1)
        #self.ac.DropDown_Country("India")
        self.ac.Enter_Address1("Dhanakwadi, Pune")
        self.ac.Enter_Address2("411043, Maharashtra")
        time.sleep(2)
        self.ac.Click_Email_Newsletter_Subscriber()
        time.sleep(5)
        #self.ac.DropDown_Currency(4)
        self.ac.Enter_Balance("1000")
        time.sleep(5)
        self.ac.Click_Save()
        time.sleep(10)

