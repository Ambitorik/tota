from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = (('Красный', 5), ('Желтый', 2), ('Зеленый', 10))

    def running(self):
        for color, sec in cycle(self.__color):
            print(color, 'подождите {} секунд'.format(sec))
            sleep(sec)


traffic_lights = TrafficLight()
traffic_lights.running()
