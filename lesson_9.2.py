class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        form = self._width * self._length * 5 * 25 / 1000
        return form


asphalt_mass = Road(int(input('Введите длину ')), int(input('Введите ширину ')))
print(asphalt_mass.calc(), 'т')
