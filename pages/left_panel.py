from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LeftPanel:
    def __init__(self, browser):
        self.browser = browser

    def open(self, main_section: str, sub_section: str):
        self.browser.get("https://demoqa.com/")
        section = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//h5[text()='{main_section}']"))
        )
        self.browser.execute_script("arguments[0].scrollIntoView(true);", section)
        section.click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".left-pannel"))
        )
        subitem = self.browser.find_element(By.XPATH, f"//span[text()='{sub_section}']")
        subitem.click()
        return self

    def open_simple_registration_form(self):
        # Shortcut: открытие текстовой формы через навигацию по панели
        return self.open('Elements', 'Text Box')
