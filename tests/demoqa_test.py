import os.path
from selene.support.shared import browser
from selene import have


def test_student_registration_form():
    browser.open('/automation-practice-form')

    #WHEN
    browser.element('#firstName').type('Elvira')
    browser.element('#lastName').type('Askerova')
    browser.element('#userEmail').type('elviraskerova@gmail.com')
    browser.all('[name=gender]').element_by(have.value('Female')).element('./following-sibling::*').click()
    browser.element('#userNumber').type('1234567891')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('December')
    browser.element('.react-datepicker__year-select').type('1990')
    browser.element(f'.react-datepicker__day--00{8}').click()

    browser.element('#subjectsInput').type('Commerce').press_enter()

    browser.element('[for=hobbies-checkbox-2]').click()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), '../attachments/photo.jpeg')))

    browser.element('#currentAddress').type('Plehanova Street 1')
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()
    browser.element('#submit').press_enter()

    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
            'Elvira Askerova',
            'elviraskerova@gmail.com',
            'Female',
            '1234567891',
            '08 December,1990',
            'Commerce',
            'Reading',
            'photo.jpeg',
            'Plehanova Street 1',
            'Uttar Pradesh Agra'
        ))


