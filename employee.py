# Created By SEAN CUNNIFFE on 14/01/2021
import random

import requests


class Employee:
    raise_amt = 1.2

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @property
    def email(self):
        return f'{self.first}.{self.last}{random.randint(0, 9)}@email.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
