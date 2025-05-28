
test_data = {
    "first_name": "Ivan",
    "last_name": "Ivanov",
    "email": "ivanov@fake.com",
    "gender": "Male",
    "phone": "9555555555",
    "birth": "20 May,1995",
    "subject": "Physics",
    "hobby": "Sports",
    "file_name": "test1.jpeg",
    "address": "Test address",
    "state": "NCR",
    "city": "Delhi"
}


# Ожидаемые данные для проверки модального окна
expected_modal_data = {
    "Student Name": f"{test_data['first_name']} {test_data['last_name']}",
    "Student Email": test_data["email"],
    "Gender": test_data["gender"],
    "Mobile": test_data["phone"],
    "Date of Birth": test_data["birth"],
    "Subjects": test_data["subject"],
    "Hobbies": test_data["hobby"],
    "Picture": test_data["file_name"],
    "Address": test_data["address"],
    "State and City": f"{test_data['state']} {test_data['city']}"
}