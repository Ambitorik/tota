dictionary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(translation):
    if translation[0].isupper():
        translation = translation.lower()
        return dictionary.get(translation).capitalize()
    else:
        return dictionary.get(translation)


print(num_translate_adv(input('Введите число от one до ten: ')))
