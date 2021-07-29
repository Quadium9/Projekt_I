import re


def validate_text(value):
    return not str(value).isalpha()


def onechar_text(value):
    if len(value) == 1:
        return True
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
    for v in value:
        if v is None:
            return False
    return True
