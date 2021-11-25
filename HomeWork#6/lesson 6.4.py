from itertools import zip_longest

with open('unification.txt', 'w', encoding='utf-8') as user_hobby:
    with open('users.txt', encoding='utf-8') as users:
        with open('hobby.txt', encoding='utf-8') as hobby:

            if sum(1 for line_1 in users) > sum(1 for line_2 in hobby):
                exit(1)

            users.seek(0)
            hobby.seek(0)
            for line_user, line_hobby in zip_longest(users, hobby):
                user_hobby.write(f'{line_user.strip()}:{line_hobby.strip()}\n')
