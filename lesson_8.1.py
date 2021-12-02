import re
EMAIL = re.compile(r'([a-z0-9_\.]+)@([a-z0-9]+\.[a-z]+)')


def email_parse(email):
    found_info = EMAIL.findall(email)
    if found_info:
        name, address = found_info[0]
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, address)


email_parse('someone@geekbrains.ru')
email_parse('someonegeekbrains.ru')
