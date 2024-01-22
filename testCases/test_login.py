import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, setup):
        self.driver = setup
        yield
        self.driver.close()

    def test_home_page_title(self):
        self.driver.get(self.baseURL)
        assert self.driver.title == "Your store. Login", "Home page title is not as expected."

    def test_login(self):
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        assert self.driver.title == "Dashboard / nopCommerce administration", "Login failed or title does not match."