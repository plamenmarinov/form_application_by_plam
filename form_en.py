import re

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

EMAIL_RE = re.compile('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
PHONE_RE = re.compile('\+[\d]{12}')

Builder.load_file('form_en.kv')


class FormValidationException(Exception):
    def __init__(self, msg: str):
        self._msg = msg

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>: {self._msg}"

    def __str__(self) -> str:
        return self._msg


def check_empty(firstname: str, lastname: str, email: str,
                phone: int, birthdate: str, password: str,
                password_confirm: str):
    if not firstname:
        raise FormValidationException('Тhe "Personal Name" field cannot be empty.')
    if not lastname:
        raise FormValidationException('Тhe "Family Name" field cannot be empty.')
    if not email:
        raise FormValidationException('The "E-mail address" field cannot be empty.')
    if not phone:
        raise FormValidationException('The "Phone number" field cannot be empty.')
    if not birthdate:
        raise FormValidationException('The "Birthdate" field cannot be empty.')
    if not password:
        raise FormValidationException('The "Password" field cannot be empty.')
    if not password_confirm:
        raise FormValidationException('The "Password Confirmation" field cannot be empty.')
    if password_confirm != password:
        raise FormValidationException('Invalid password')


def check_email(email: str):
    if not EMAIL_RE.search(email):
        raise FormValidationException("Invalid E-mail address")


def check_phone(phone):
    if not PHONE_RE.search(phone):
        raise FormValidationException("Invalid Phone number")


class Form(BoxLayout):
    def submit(self):
        self.l_status.text = ""
        firstname = self.f_firstname.text
        lastname = self.f_lastname.text
        email = self.f_email.text
        phone = self.f_phone.text
        birthdate = self.f_birthdate.text
        password = self.f_password.text
        password_confirm = self.f_password_confirm.text
        try:
            check_empty(firstname, lastname, email, phone, birthdate, password, password_confirm)
            check_email(email)
            check_phone(phone)

        except FormValidationException as e:
            self.l_status.color = (1, 0, 0)
            self.l_status.text = str(e)
            return
        print(
            f'Personal Name: {firstname}\n'
            f'Family Name: {lastname}\n'
            f'E-mail: {email}\n'
            f'Phone number: {phone}\n'
            f'Birthdate: {birthdate}'
        )
        exit()


class FormApplication(App):
    def build(self):
        return Form()


if __name__ == '__main__':
    FormApplication().run()
