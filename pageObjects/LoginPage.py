from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"  # Example of a more specific XPath, adjust as needed
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Adjust timeout as needed

    def enter_username(self, username):
        username_field = self.wait.until(EC.visibility_of_element_located((By.ID, self.textbox_username_id)))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, self.textbox_password_id)))
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath)))
        login_button.click()

    def click_logout(self):
        logout_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.link_logout_linktext)))
        logout_link.click()