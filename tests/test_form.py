from demoqa_3_8.model.pages import practice_form


def test_student_registration_form():
    practice_form.given_opened()


    practice_form.type_firstname('Elvira')
    practice_form.type_lastname('Askerova')
    practice_form.type_email('elviraskerova@gmail.com')
    practice_form.select_gender('Female')
    practice_form.type_phone_number('1234567891')

    practice_form.click_on_datepicker()
    practice_form.pick_month('December')
    practice_form.pick_year('1990')
    practice_form.pick_day('8')

    practice_form.type_subject('Commerce')

    practice_form.select_hobby('Reading')

    practice_form.upload_picture('photo.jpeg')

    practice_form.scroll_to_address()
    practice_form.type_address('Plehanova Street 1')
    practice_form.select_state('Uttar Pradesh')
    practice_form.select_city('Agra')
    practice_form.submit()

    practice_form.assert_fields(
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
        )


