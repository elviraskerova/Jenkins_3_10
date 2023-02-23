from selene import have, command
from selene.support.shared import browser
from demoqa_3_8.model.controls import dropdown
from demoqa_3_8.model.controls import datepicker
from demoqa_3_8.model.controls import radiobutton
from demoqa_3_8.model.controls import checkbox
from demoqa_3_8.utils import path_to_file
from demoqa_3_8.utils.scroll import scroll_to


def given_opened():
    browser.open('/automation-practice-form')


def type_firstname(text):
    browser.element('#firstName').type(text)


def type_lastname(text):
    browser.element('#lastName').type(text)


def type_email(text):
    browser.element('#userEmail').type(text)


def select_gender(gender):
    radiobutton.gender('[name=gender]', gender)


def type_phone_number(text):
    browser.element('#userNumber').type(text)


def click_on_datepicker():
    browser.element('#dateOfBirthInput').click()


def pick_month(month):
    browser.element('.react-datepicker__month-select').click()
    datepicker.date('.react-datepicker__month-select', month)


def pick_year(year):
    browser.element('.react-datepicker__year-select').click()
    datepicker.date('.react-datepicker__year-select', year)


def pick_day(day):
    browser.element(f'.react-datepicker__day--00{day}').click()


def type_subject(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def select_hobby(hobby):
    checkbox.hobby('[for^=hobbies-checkbox]', hobby)


def upload_picture(path_to_picture):
    path_to_file.create_path('#uploadPicture', path_to_picture)


def scroll_to_address():
    scroll_to('#currentAddress')


def type_address(text):
    browser.element('#currentAddress').type(text)


def submit():
    browser.element('#submit').press_enter()


def select_state(value):
    dropdown.select('#state', by_text=value)


def select_city(value):
    dropdown.select('#city', by_text=value)


def assert_fields(*args):
    browser.element('.table').all('td').even.should(have.texts(args))


def scroll_to_address():
    scroll_to('#currentAddress')

