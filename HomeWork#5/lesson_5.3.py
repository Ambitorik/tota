tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

from itertools import zip_longest

gen = ((tutor, klass) for tutor, klass in zip_longest(klasses, tutors))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(type(gen))
