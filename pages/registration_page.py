import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from enum import Enum


class Gender(Enum):
    MALE = "1"
    FEMALE = "2"
    OTHER = "3"


class Hobby(Enum):
    SPORTS = "1"
    READING = "2"
    MUSIC = "3"


class RegistrationPage:
    URL = "https://demoqa.com/automation-practice-form"

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)
        return self

    def scroll_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def fill_first_name(self, first_name: str):
        self.browser.find_element(By.ID, "firstName").send_keys(first_name)
        return self

    def fill_last_name(self, last_name: str):
        self.browser.find_element(By.ID, "lastName").send_keys(last_name)
        return self

    def fill_email(self, email: str):
        self.browser.find_element(By.ID, "userEmail").send_keys(email)
        return self

    def choose_gender(self, gender: Gender):
        self.browser.find_element(By.CSS_SELECTOR, f"label[for='gender-radio-{gender.value}']").click()
        return self

    def fill_phone(self, phone: str):
        self.browser.find_element(By.ID, "userNumber").send_keys(phone)
        return self

    def set_birth_date(self, day: str, month: str, year: str):
        self.browser.find_element(By.ID, "dateOfBirthInput").click()
        self.browser.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys(month)
        self.browser.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys(year)
        self.browser.find_element(By.CSS_SELECTOR, f".react-datepicker__day--0{day}").click()
        return self

    def fill_subject(self, subject: str):
        subject_field = self.browser.find_element(By.ID, "subjectsInput")
        subject_field.send_keys(subject)
        subject_field.send_keys(Keys.ENTER)
        return self

    def choose_hobby(self, hobby: Hobby):
        label = self.browser.find_element(By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{hobby.value}']")
        self.scroll_to_element(label)
        label.click()
        return self

    def upload_picture(self, file_path: str):
        abs_path = os.path.abspath(file_path)
        self.browser.find_element(By.ID, "uploadPicture").send_keys(abs_path)
        return self

    def fill_address(self, address: str):
        self.browser.find_element(By.ID, "currentAddress").send_keys(address)
        return self

    def select_state(self, state: str):
        self.browser.find_element(By.ID, "state").click()
        input_ = self.browser.find_element(By.ID, "react-select-3-input")
        input_.send_keys(state)
        input_.send_keys(Keys.ENTER)
        return self

    def select_city(self, city: str):
        self.browser.find_element(By.ID, "city").click()
        input_ = self.browser.find_element(By.ID, "react-select-4-input")
        input_.send_keys(city)
        input_.send_keys(Keys.ENTER)
        return self

    def submit(self):
        self.browser.find_element(By.ID, "submit").click()
        return self

    def should_have_registered(self, expected_data):
        # Проверка модального окна
        modal = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
        )
        assert modal.is_displayed()
        assert "Thanks for submitting the form" in modal.text

        # Сбор данных из модального окна
        modal_table = self.browser.find_element(By.CSS_SELECTOR, ".modal-body table")
        modal_rows = modal_table.find_elements(By.TAG_NAME, "tr")

        modal_data = {}
        for row in modal_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 2:
                key = cells[0].text.strip()
                value = cells[1].text.strip()
                modal_data[key] = value

        for key, expected_value in expected_data.items():
            assert key in modal_data, f"Поле '{key}' отсутствует в модальном окне"
            assert modal_data[
                       key] == expected_value, f"Значение поля '{key}': ожидалось '{expected_value}', получено '{modal_data[key]}'"
