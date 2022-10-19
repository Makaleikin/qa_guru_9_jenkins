import os
from typing import Tuple

import allure
from selene import have, command
from selene.support.shared import browser
from selenium.webdriver.common.keys import Keys

from demoqa_tests.model.contols import datepicker, dropdown, modal
from tests.test_data.user_data import Subject


@allure.step('Открываем страницу регистрации')
def given_opened():
    browser.open('https://demoqa.com/automation-practice-form')


def remove_advertisement():
    browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]').with_(timeout=10)\
        .should(have.size_less_than_or_equal(4))\
        .perform(command.js.remove)
#     ads = browser.all('[id^=google_ads][id$=container__]')
#     if ads.wait.until(have.size_less_than_or_equal(5)):
#         ads.perform(command.js.remove)


@allure.step('Заполняем имя')
def set_first_name(first_name: str):
    browser.element('#firstName').type(first_name)


@allure.step('Заполняем фамлиию')
def set_last_name(last_name: str):
    browser.element('#lastName').type(last_name)


@allure.step('Заполняем e-mail')
def set_email(email: str):
    browser.element('#userEmail').type(email)


@allure.step('Выбираем пол')
def set_gender(gender):
    browser.all('[for^=gender-radio]').by(have.exact_text(gender.value)).first.click()


@allure.step('Заполняем номер телефона')
def set_phone_number(user_number: str):
    browser.element('#userNumber').type(user_number)


def set_date_of_birth(birth_day, birth_month, birth_year):
    datepicker.select_date(birth_day, birth_month, birth_year)


@allure.step('Указываем дату рождения, вводя значения в поле')
def type_date_of_birth(day, month, year):
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL + 'a').type(day + month + year).press_enter()


@allure.step('Заполняем предметы')
def add_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter()


@allure.step('Выбираем хобби')
def add_hobbie_sport():
    browser.element('[for="hobbies-checkbox-1"][class="custom-control-label"]').click()


@allure.step('Загружаем изображение')
def upload_picture(picture_file: str):
    browser.element('#uploadPicture').send_keys(os.path.abspath(picture_file))


@allure.step('Указываем адрес')
def set_current_address(current_address: str):
    browser.element('#currentAddress').type(current_address)


def scroll_into():
    browser.element('#state').perform(command.js.scroll_into_view)

@allure.step('Выбираем страну')
def set_state(value: str):
    dropdown.select(browser.element('#state'), value)


@allure.step('Выбираем город')
def set_city(value: str):
    dropdown.select(browser.element('#city'), value)


@allure.step('Жмем на кнопку подтверждения формы')
def submit_form():
    browser.element('#submit').click()


@allure.step('Проверяем, что заполненные данные присутствуют на финальной форме')
def should_have_submitted(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
