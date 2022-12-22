import os.path
from selene.support.shared import browser
from selene import have


def test_student_registration_form():
    browser.open('/automation-practice-form')

    #WHEN
    browser.element('#firstName').type('Elvira')
    browser.element('#lastName').type('Askerova')
    browser.element('#userEmail').type('elviraskerova@gmail.com')
    browser.element('[name=gender][value=Female]').click()
    browser.element('#userNumber').type('1234567891')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker_month-select').type('December')
    browser.element('.react-datepicker_year-select').type('1990')
    browser.element(f'.react-datepicker_day--0{8}').click()

    browser.element('#subjectsInput').type('Commerce').press_enter()

    browser.element('[for=hobbies-checkbox-2]').click()

    browser.element('#uploadPicture').send_keys(file_path)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path.join(current_dir, 'attachments/photo.jpeg')

    browser.element('#currentAddress').type('Plehanova Street 1')
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=options]').element_by(have.text('Uttar Pradesh')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=options]').element_by(have.text('Agra')).click()

    #THEN
    browser.element('.table').all('td:nth-of-type(2').should()
    have.text(
        'Elvira Askerova',
        'elviraskerova@gmail.com',
        'Female',
        '123456789',
        '8 December, 1990',
        'Commerce',
        'Reading',
        'foto.jpg',
        'Plehanova Street 1',
        'Uttar Pradesh',
        'Agra',
    )