from application_manager import ApplicationManager
from users.user import new_student


def test_simple_registration_form(browser):
    app = ApplicationManager(browser)
    app.left_panel.open_simple_registration_form()
    app.simple_registration_form.register(new_student).should_have_registered(new_student)
