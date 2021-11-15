import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(joke):
    jokes_list = []
    for i in range(joke):
        random_nouns = random.choice(nouns)
        random_adverbs = random.choice(adverbs)
        random_adjectives = random.choice(adjectives)
        jokes_list.append(f'{random_nouns}, {random_adverbs}, {random_adjectives}')
        return jokes_list


print(get_jokes(1))
