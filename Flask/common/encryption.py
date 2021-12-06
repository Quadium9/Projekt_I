import hashlib


def createhash(password):
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), "1029384756".encode('utf-8'), 100000)
    storage = key
    return storage


def comparepassword(passwordin, storage):
    new_key = hashlib.pbkdf2_hmac('sha256', passwordin.encode('utf-8'), "1029384756".encode('utf-8'), 100000)
    if str(storage) == str(new_key):
        return True
    else:
        return False
