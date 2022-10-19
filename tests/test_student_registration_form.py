import allure

from demoqa_tests.model.pages import registration_form
from test_data.user_data import student


@allure.tag("web")
@allure.label('owner', 'MlynskijArtem')
@allure.feature('Регистрация пользователя в системе')
@allure.story('Я, как пользователь, хочу иметь возможность регистрации на сайте')
@allure.link('https://demoqa.com/automation-practice-form', name='Testing')
def test_filling_registration_form():
    # GIVEN
    registration_form.given_opened()
    registration_form.remove_advertisement()
    # WHEN
    registration_form.set_first_name(student.first_name)
    registration_form.set_last_name(student.last_name)
    registration_form.set_email(student.email)
    registration_form.set_gender(student.gender)
    registration_form.set_phone_number(student.user_number)
    registration_form.type_date_of_birth(student.birth_day, student.birth_month, student.birth_year)
    registration_form.add_subjects(student.subjects)
    registration_form.add_hobbie_sport()
    registration_form.upload_picture(student.picture_file)
    registration_form.set_current_address(student.current_address)
    registration_form.remove_advertisement()
    registration_form.set_state(student.state)
    registration_form.set_city(student.city)
    registration_form.submit_form()

    # THEN
    registration_form.should_have_submitted(
        [
            ('Student Name', f'{student.first_name} {student.last_name}'),
            ('Student Email', student.email),
            ('Gender', student.gender.value),
            ('Mobile', student.user_number),
            ('Date of Birth', f'{student.birth_day} {student.birth_month},{student.birth_year}'),
            ('Subjects', 'History, Maths'),
            ('Hobbies', 'Sports'),
            ('Picture', 'qapicture.png'),
            ('Address', student.current_address),
            ('State and City', f'{student.state} {student.city}')
        ],
    )