from selenium.common import NoSuchElementException, NoAlertPresentException, TimeoutException, \
    ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class AddCustomer:
    Click_Accounts_XPATH = (By.XPATH,"/html[1]/body[1]/div[2]/div[1]/nav[1]/div[1]/div[1]/a[6]")
    Click_Customer_XPATH = (By.XPATH,"/html[1]/body[1]/div[2]/div[1]/nav[1]/div[1]/div[1]/div[5]/nav[1]/a[4]")
    Click_Add_XPATH = (By.XPATH, "//i[normalize-space()='add']")
    Text_FirstName_XPATH = (By.XPATH, "//input[@placeholder='First name']")
    Text_LastName_XPATH = (By.XPATH, "//input[@placeholder='Last name']")
    Text_Email_XPATH = (By.XPATH, "//input[@placeholder='Email address']")
    Text_Password_XPATH = (By.XPATH, "//input[@placeholder='Password']")
    Text_MobileNumber_XPATH = (By.XPATH, "//input[@placeholder='Mobile Number']")
    DropDown_Country_XPATH = (By.XPATH, "//a[@class ='select2-choice']")
    Text_address1_XPATH = (By.XPATH, "//input[@name='address1']")
    Text_address2_XPATH = (By.XPATH, "//input[@name='address2']")
    Click_Email_Newsletter_Subscriber_XPATH = (By.XPATH, "//input[@name='newssub']")
    DropDown_Currency_XPATH = (By.XPATH, "//div//select[@name='currency']")
    Text_Balance_XPATH = (By.XPATH, "//input[@placeholder='Balance']")
    Click_Save_XPATH = (By.XPATH, "/html[1]/body[1]/div[2]/div[2]/main[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[4]/button[1]")
    Url_addcustomer = "https://phptravels.net/api/admin/accounts/customers/add"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=0.2)

    def Click_Accounts(self):
        wait = WebDriverWait(self.driver, 15)
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.Click_Accounts_XPATH))
            self.driver.find_element(*AddCustomer.Click_Accounts_XPATH).click()
        except ElementClickInterceptedException:
            pass


    def Click_Customer(self):
        wait = WebDriverWait(self.driver, 15)
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.Click_Customer_XPATH))
            self.driver.find_element(*AddCustomer.Click_Customer_XPATH).click()
        except ElementNotInteractableException:
            pass


    def Click_Add(self):

        wait = WebDriverWait(self.driver, 15)
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.Click_Add_XPATH))
            self.driver.find_element(*AddCustomer.Click_Add_XPATH).click()
        except NoSuchElementException:
            pass


    def Enter_FirstName(self, firstname):
        self.driver.find_element(*AddCustomer.Text_FirstName_XPATH).send_keys(firstname)

    def Enter_lastName(self, lastname):
        self.driver.find_element(*AddCustomer.Text_LastName_XPATH).send_keys(lastname)

    def Enter_Email(self, email):
        self.driver.find_element(*AddCustomer.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*AddCustomer.Text_Password_XPATH).send_keys(password)

    def Enter_MobileNumber(self, mobilenumber):
        self.driver.find_element(*AddCustomer.Text_MobileNumber_XPATH).send_keys(mobilenumber)

    def DropDown_Country(self, country):
        Country = Select(self.driver.find_element(*AddCustomer.DropDown_Country_XPATH))
        Country.select_by_index(2)

    def Enter_Address1(self, address1):
        self.driver.find_element(*AddCustomer.Text_address1_XPATH).send_keys(address1)

    def Enter_Address2(self, address2):
        self.driver.find_element(*AddCustomer.Text_address2_XPATH).send_keys(address2)


    def Click_Email_Newsletter_Subscriber(self):
        wait = WebDriverWait(self.driver, 15)
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.Click_Email_Newsletter_Subscriber_XPATH))
            self.driver.find_element(*AddCustomer.Click_Email_Newsletter_Subscriber_XPATH).click()
        except ElementClickInterceptedException:
            pass

    def DropDown_Currency(self, currency):
        Currency = Select(self.driver.find_element(*AddCustomer.DropDown_Currency_XPATH))
        Currency.select_by_index(currency)

    def Enter_Balance(self, balance):
        self.driver.find_element(*AddCustomer.Text_Balance_XPATH).send_keys(balance)

    def Click_Save(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Save_XPATH))
            self.driver.find_element(*AddCustomer.Click_Save_XPATH).click()
        except ElementClickInterceptedException:
            pass

    def Url_Add_Customer(self):
        self.driver.get(self.Url_addcustomer)
