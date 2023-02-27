from selene import have, command
from selene.support.shared import browser
from demoqa_3_8.model.controls import dropdown
from demoqa_3_8.model.controls import datepicker
from demoqa_3_8.model.controls import radiobutton
from demoqa_3_8.model.controls import checkbox
from demoqa_3_8.model.data.user import User
from demoqa_3_8.utils import path_to_file
from demoqa_3_8.utils.scroll import scroll_to


class Form:

    def __init__(self, user: User):
        self.user = user

    def given_opened(self):
        browser.open('/automation-practice-form')

    def type_firstname(self, user):
        browser.element('#firstName').type(user.first_name)

    def type_lastname(self, user):
        browser.element('#lastName').type(user.last_name)

    def type_email(self, user):
        browser.element('#userEmail').type(user.email)

    def select_gender(self, user):
        radiobutton.gender('[name=gender]', user.gender)

    def type_phone_number(self, user):
        browser.element('#userNumber').type(user.phone)

    def click_on_datepicker(self):
        browser.element('#dateOfBirthInput').click()

    def pick_month(self, user):
        browser.element('.react-datepicker__month-select').click()
        datepicker.date('.react-datepicker__month-select', user.birthday_month)

    def pick_year(self, user):
        browser.element('.react-datepicker__year-select').click()
        datepicker.date('.react-datepicker__year-select', user.birthday_year)

    def pick_day(self, user):
        browser.element(f'.react-datepicker__day--0{user.birthday_day}').click()

    def type_subject(self, user):
        browser.element('#subjectsInput').type(user.subject).press_enter()

    def select_hobby(self, user):
        checkbox.hobby('[for^=hobbies-checkbox]', user.hobby)

    def upload_picture(self, user):
        path_to_file.create_path('#uploadPicture', user.image)

    def scroll_to_address(self):
        scroll_to('#currentAddress')

    def type_address(self, user):
        browser.element('#currentAddress').type(user.address)

    def submit(self):
        browser.element('#submit').press_enter()

    def select_state(self, user):
        dropdown.select('#state', user.state)

    def select_city(self, user):
        dropdown.select('#city', user.city)

    def assert_fields(self, *args):
        browser.element('.table').all('td').even.should(have.texts(args))

    def add_birthday(self, user):
        self.click_on_datepicker()
        self.pick_month(user)
        self.pick_year(user)
        self.pick_day(user)

    def submit_form(self, user):
        self.given_opened()
        self.type_firstname(user)
        self.type_lastname(user)
        self.type_email(user)
        self.type_phone_number(user)
        self.type_address(user)
        self.select_gender(user)
        self.add_birthday(user)
        self.type_subject(user)
        self.select_hobby(user)
        scroll_to('#state')
        self.select_state(user)
        self.select_city(user)
        self.submit()

    def validate_form(self, user):
        user_birthday = f'{user.birthday_day} {user.birthday_month},{user.birthday_year}'
        user_full_name = user.first_name + ' ' + user.last_name
        user_place = user.state + ' ' + user.city

        self.assert_fields(
            user_full_name,
            user.email,
            user.gender,
            user.phone,
            user_birthday,
            user.subject,
            user.hobby,
            '',
            user.address,
            user_place
        )
