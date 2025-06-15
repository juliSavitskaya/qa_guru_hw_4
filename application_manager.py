from pages.left_panel import LeftPanel
from pages.simple_registration_page import SimpleRegistrationPage


class ApplicationManager:
    def __init__(self, browser):
        self.browser = browser
        self.left_panel = LeftPanel(browser)
        self.simple_registration_form = SimpleRegistrationPage(browser)
