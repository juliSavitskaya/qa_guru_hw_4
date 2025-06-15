from selenium.webdriver.common.by import By
from users.user import NewUser


class SimpleRegistrationPage:
    URL = "https://demoqa.com/text-box"

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)
        return self

    def register(self, user: NewUser):
        self.browser.find_element(By.ID, "userName").send_keys(user.name)
        self.browser.find_element(By.ID, "userEmail").send_keys(user.email)
        self.browser.find_element(By.ID, "currentAddress").send_keys(user.current_address)
        self.browser.find_element(By.ID, "permanentAddress").send_keys(user.permanent_address)
        self.browser.find_element(By.ID, "submit").click()
        return self

    def should_have_registered(self, user: NewUser):
        output = self.browser.find_element(By.ID, "output")
        assert user.name in output.text
        assert user.email in output.text
        assert user.current_address in output.text
        assert user.permanent_address in output.text
        return self
