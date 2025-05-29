import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data import test_data, expected_modal_data


def scroll_to_element(browser, element):
    browser.execute_script("arguments[0].scrollIntoView(true);", element)


def test_filling_registration_form(browser):
    browser.get("https://demoqa.com/automation-practice-form")

    # Имя
    first_name = browser.find_element(By.ID, "firstName")
    first_name.send_keys(test_data["first_name"])

    # Фамилия
    last_name = browser.find_element(By.ID, "lastName")
    last_name.send_keys(test_data["last_name"])

    # Email
    user_email = browser.find_element(By.ID, "userEmail")
    user_email.send_keys(test_data["email"])

    # Пол
    gender_radio = browser.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
    gender_radio.click()

    # Телефон
    user_number = browser.find_element(By.ID, "userNumber")
    user_number.send_keys(test_data["phone"])

    # Дата рождения
    birth_input = browser.find_element(By.ID, "dateOfBirthInput")
    scroll_to_element(browser, birth_input)
    birth_input.click()

    # Выбор месяца и года
    month_select = browser.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    month_select.send_keys("May")

    year_select = browser.find_element(By.CLASS_NAME, "react-datepicker__year-select")
    year_select.send_keys("1995")

    # Клик по дню месяца
    day = browser.find_element(By.CSS_SELECTOR, ".react-datepicker__day--020")
    day.click()

    # Предмет
    subject = browser.find_element(By.ID, "subjectsInput")
    scroll_to_element(browser, subject)
    subject.send_keys(test_data["subject"])
    subject.send_keys(Keys.ENTER)

    # Хобби
    hobby_checkbox = browser.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    scroll_to_element(browser, hobby_checkbox)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")))
    hobby_checkbox.click()

    # Загрузка файла
    file_path = os.path.abspath("tests/test1.jpeg")
    upload = browser.find_element(By.ID, "uploadPicture")
    scroll_to_element(browser, upload)
    upload.send_keys(file_path)

    # Адрес
    address = browser.find_element(By.ID, "currentAddress")
    scroll_to_element(browser, address)
    address.send_keys(test_data["address"])

    # Штат
    state = browser.find_element(By.ID, "state")
    scroll_to_element(browser, state)
    state.click()
    state_input = browser.find_element(By.ID, "react-select-3-input")
    scroll_to_element(browser, state_input)
    state_input.send_keys(test_data["state"])
    state_input.send_keys(Keys.ENTER)

    # Город
    city = browser.find_element(By.ID, "city")
    scroll_to_element(browser, city)
    city.click()
    city_input = browser.find_element(By.ID, "react-select-4-input")
    scroll_to_element(browser, city_input)
    city_input.send_keys(test_data["city"])
    city_input.send_keys(Keys.ENTER)

    # Кнопка отправить
    submit_btn = browser.find_element(By.ID, "submit")
    scroll_to_element(browser, submit_btn)
    submit_btn.click()

    # Проверка появления модального окна после отправки
    modal = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )
    assert modal.is_displayed()
    assert "Thanks for submitting the form" in modal.text

    # Дополнительная проверка данных в модальном окне
    modal_table = browser.find_element(By.CSS_SELECTOR, ".modal-body table")
    modal_rows = modal_table.find_elements(By.TAG_NAME, "tr")

    modal_data = {}
    for row in modal_rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) == 2:
            key = cells[0].text.strip()
            value = cells[1].text.strip()
            modal_data[key] = value

    # Проверяем, что все ожидаемые данные присутствуют в модальном окне
    for key, expected_value in expected_modal_data.items():
        assert key in modal_data, f"Поле '{key}' отсутствует в модальном окне"
        assert modal_data[key] == expected_value, f"Значение поля '{key}': ожидалось '{expected_value}', получено '{modal_data[key]}'"

