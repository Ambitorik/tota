one_minute = 60
one_hour = 3600
one_day = 86400
one_week = 604800

duration = int(input('Укажите продолжительность в секундах: '))

if duration < one_minute:
    print('{} секунд'.format(duration))

elif one_minute <= duration < one_hour:
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} минут {} секунд'.format(my_minute, my_second))

elif one_hour <= duration < one_day:
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} часов {} минут {} секунд'.format(my_hour, my_minute, my_second))

elif duration >= one_week:
    my_day = duration // one_day
    duration = duration % one_day
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} дней {} часов {} минут {} секунд '.format(my_day, my_hour, my_minute, my_second))