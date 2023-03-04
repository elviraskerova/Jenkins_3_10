import allure
from allure_commons.types import Severity

from demoqa_3_8.model.data.user import User
from demoqa_3_8.model.pages.practice_form import Form


def test_student_registration_form():
    elvira = User(first_name='Elvira',
                  last_name='Askerova',
                  email='elviraskerova@gmail.com',
                  phone='1234567891',
                  address='Plehanova Street 1',
                  gender='Female',
                  birthday_year='1990',
                  birthday_month='December',
                  birthday_day='08',
                  subject='Commerce',
                  hobby='Reading',
                  image='photo.jpg',
                  state='Uttar Pradesh',
                  city='Agra'
                  )

    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label('owner', 'elviraskerova')
    allure.dynamic.feature('Проверка отправки формы')

    practice_form = Form(elvira)

    with allure.step('Заполняем данные формы'):
        practice_form.submit_form(elvira)

    with allure.step('Проверяем результаты'):
        practice_form.validate_form(elvira)





