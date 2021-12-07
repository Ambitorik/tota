class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} поехала'.format(self.name))

    def stop(self):
        print('{} остановилась'.format(self.name))

    def turn(self, direction):
        print('{} повернула {}'.format(self.name, direction))

    def show_speed(self):
        print('Текущая скорость', self.speed)


class TownCar(Car):
    def show_speed(self):
        print('Текущая скорость', self.speed)
        if self.speed > 60:
            print('Скорость превышена')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Текущая скорость', self.speed)
        if self.speed > 40:
            print('Скорость превышена')


class PoliceCar(Car):
    pass


town_car = TownCar(70, 'Черная', 'Городская машина', False)
sport_car = SportCar(180, 'Желтая', 'Спортивная машина', False)
work_car = WorkCar(90, 'Белая', 'Рабочая машина', False)
police_car = PoliceCar(140, 'Розовая', 'Полицейская машина', True)

sport_car.go()
sport_car.turn('направо')
work_car.go()
work_car.show_speed()
work_car.show_speed()
work_car.go()
