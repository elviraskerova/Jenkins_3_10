from demoqa_3_8.model.controls import datepicker
from selene.support.shared import browser


def click_on_datepicker():
    browser.element('#dateOfBirthInput').click()


def pick_month(user):
    browser.element('.react-datepicker__month-select').click()
    datepicker.date('.react-datepicker__month-select', user.birthday_month)


def pick_year(user):
    browser.element('.react-datepicker__year-select').click()
    datepicker.date('.react-datepicker__year-select', user.birthday_year)


def pick_day(user):
    browser.element(f'.react-datepicker__day--0{user.birthday_day}').click()


def add_birthday(user):
    click_on_datepicker()
    pick_month(user)
    pick_year(user)
    pick_day(user)
