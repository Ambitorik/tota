class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Ручка пишет')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш пишет')


class Handle(Stationery):
    def draw(self):
        print('Маркер пишет')


stat = Stationery('лист')
pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

stat.draw()
pen.draw()
pencil.draw()
handle.draw()
