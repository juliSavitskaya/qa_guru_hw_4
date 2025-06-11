import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from users.user import User, Gender


class RegistrationPage:
    URL = "https://demoqa.com/automation-practice-form"

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)
        return self

    def scroll_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def register(self, user: User):
        self._fill_first_name(user.first_name)
        self._fill_last_name(user.last_name)
        self._fill_email(user.email)
        self._choose_gender(user.gender)
        self._fill_phone(user.phone)
        self._set_birth_date(user.birth_date)
        self._fill_subjects(user.subjects)
        self._fill_hobbies(user.hobbies)
        self._upload_picture(user.picture)
        self._fill_address(user.address)
        self._fill_state_city(user.state, user.city)
        self._submit()
        return self

    def should_have_registered(self, user: User):
        modal = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
        )
        assert "Thanks for submitting the form" in modal.text

        modal_table = self.browser.find_element(By.CSS_SELECTOR, ".modal-body table")
        rows = modal_table.find_elements(By.TAG_NAME, "tr")
        modal_data = {}
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 2:
                key = cells[0].text.strip()
                value = cells[1].text.strip()
                modal_data[key] = value

        # Проверка соответствия каждому полю
        assert modal_data["Student Name"] == f"{user.first_name} {user.last_name}"
        assert modal_data["Student Email"] == user.email
        assert modal_data["Gender"] == user.gender.value
        assert modal_data["Mobile"] == user.phone
        assert modal_data["Date of Birth"] == user.birth_date.strftime("%d %B,%Y")
        assert modal_data["Subjects"] == ", ".join(user.subjects)
        assert modal_data["Hobbies"] == ", ".join(user.hobbies)
        assert modal_data["Picture"] == os.path.basename(user.picture)
        assert modal_data["Address"] == user.address
        assert modal_data["State and City"] == f"{user.state} {user.city}"

    def _fill_first_name(self, first_name):
        self.browser.find_element(By.ID, "firstName").send_keys(first_name)

    def _fill_last_name(self, last_name):
        self.browser.find_element(By.ID, "lastName").send_keys(last_name)

    def _fill_email(self, email):
        self.browser.find_element(By.ID, "userEmail").send_keys(email)

    def _choose_gender(self, gender: Gender):
        self.browser.find_element(
            By.XPATH, f"//label[contains(text(),'{gender.value}')]"
        ).click()

    def _fill_phone(self, phone):
        self.browser.find_element(By.ID, "userNumber").send_keys(phone)

    def _set_birth_date(self, birth_date):
        self.browser.find_element(By.ID, "dateOfBirthInput").click()
        # Выбрать месяц
        month_select = self.browser.find_element(By.CLASS_NAME, "react-datepicker__month-select")
        month_select.click()
        month_select.find_element(By.XPATH, f"//option[text()='{birth_date.strftime('%B')}']").click()
        # Выбрать год
        year_select = self.browser.find_element(By.CLASS_NAME, "react-datepicker__year-select")
        year_select.click()
        year_select.find_element(By.XPATH, f"//option[text()='{birth_date.year}']").click()
        # Кликнуть по нужному дню
        day_str = birth_date.strftime('%d').lstrip('0')
        self.browser.find_element(By.XPATH,
                                  f"//div[contains(@class,'react-datepicker__day') and text()='{day_str}']").click()

    def _fill_subjects(self, subjects):
        input_ = self.browser.find_element(By.ID, "subjectsInput")
        for subject in subjects:
            input_.send_keys(subject)
            input_.send_keys(Keys.ENTER)

    def _fill_hobbies(self, hobbies):
        for hobby in hobbies:
            label = self.browser.find_element(By.XPATH, f"//label[text()='{hobby}']")
            self.scroll_to_element(label)
            label.click()

    def _upload_picture(self, file_path):
        abs_path = os.path.abspath(file_path)
        self.browser.find_element(By.ID, "uploadPicture").send_keys(abs_path)

    def _fill_address(self, address):
        self.browser.find_element(By.ID, "currentAddress").send_keys(address)

    def _fill_state_city(self, state, city):
        self.browser.find_element(By.ID, "state").click()
        state_input = self.browser.find_element(By.ID, "react-select-3-input")
        state_input.send_keys(state)
        state_input.send_keys(Keys.ENTER)

        self.browser.find_element(By.ID, "city").click()
        city_input = self.browser.find_element(By.ID, "react-select-4-input")
        city_input.send_keys(city)
        city_input.send_keys(Keys.ENTER)

    def _submit(self):
        self.browser.find_element(By.ID, "submit").click()
