# Created By SEAN CUNNIFFE on 14/01/2021

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ValueError('Can not divide by zero!!')
    return x / y
