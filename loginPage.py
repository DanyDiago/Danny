from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Loginpage():

    def __init__(self, driver):
        self.driver = driver

    def wait_for_login_page_to_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(self.driver.find_element_by_name('LoginForm')))

    def get_username_textbox(self):
        element = self.driver.find_element_by_name('username')
        return element

    def get_password_textbox(self):
        return self.driver.find_element_by_name('pwd')

    def get_login_button(self):
        return self.driver.find_element_by_xpath("//input[@type='submit]")

    def get_login_error_msg(self):
        return self.driver.find_element_by_xpath("//span[contains(text(), 'Username or Password')]")