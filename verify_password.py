
def check_length(str_to_check):
    return len(str_to_check) >= 6


def has_number(str_to_check):

    return any(char.isdigit() for char in str_to_check)


def has_lower(str_to_check):

    return any(char.islower() for char in str_to_check)


def has_upper(str_to_check):

    return any(char.isupper() for char in str_to_check)


def make_upper(str_to_check):

    return str_to_check.upper()


def check_password(str):

    return check_length(str) and has_number(str) and has_lower(str) \
        and has_upper(str)


print(check_password("It57qwp91"))
