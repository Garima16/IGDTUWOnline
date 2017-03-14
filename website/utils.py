import re


def password_strength_ok(password):

    MIN_LENGTH = 8
    obj1 = re.compile(r'[a-z]').search(password)
    obj2 = re.compile(r'[A-Z]').search(password)
    obj3 = re.compile(r'[0-9]').search(password)
    obj4 = re.compile(r'[#.^&*_@-]').search(password)
    if obj1 and obj2 and obj3 and obj4 is not None and len(password) >= MIN_LENGTH:
        return True
    else:
        return False



