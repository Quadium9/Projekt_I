import re

import Exceptions.Exceptions


def validate_text(value):
    regex = r'[0-9]+'
    if re.match(regex, str(value)):
        return True
    else:
        return False


def integer_number(value):
    if isinstance(value, int):
        return True
    else:
        return False


def password_validation(value):
    if 8 <= len(value) <= 64:
        return True
    return False


def email_validation(value):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(regex, value):
        return True
    return False


def validationNone(value):
    if value is None or value == "":
        return False
    return True
