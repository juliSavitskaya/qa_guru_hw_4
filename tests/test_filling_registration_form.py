from pages.registration_page import RegistrationPage, Gender, Hobby
from test_data import test_data, expected_modal_data


def test_registration_form(browser):
    registration_page = RegistrationPage(browser)
    (
        registration_page
        .open()
        .fill_first_name(test_data["first_name"])
        .fill_last_name(test_data["last_name"])
        .fill_email(test_data["email"])
        .choose_gender(Gender.MALE)
        .fill_phone(test_data["phone"])
        .set_birth_date("20", "May", "1995")
        .fill_subject(test_data["subject"])
        .choose_hobby(Hobby.SPORTS)
        .upload_picture("tests/test1.jpeg")
        .fill_address(test_data["address"])
        .select_state(test_data["state"])
        .select_city(test_data["city"])
        .submit()
        .should_have_registered(expected_modal_data)
    )
