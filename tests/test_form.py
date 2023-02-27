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
    practice_form = Form(elvira)
    practice_form.submit_form(elvira)
    practice_form.validate_form(elvira)


