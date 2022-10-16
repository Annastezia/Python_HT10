class Road:
    def __init__(self, _length, _width, _weight, _thickness):
        self._length = _length
        self._width = _width
        self._weight = _weight
        self._thickness = _thickness
        
    def get_mass(self):
        print(f'{self._length} м * {self._width} м * {self._weight} кг * {self._thickness} см / 1000') # делим на 1000, тк нужны тонны
        return self._length * self._width * self._weight * self._thickness / 1000
        
r1 = Road(20, 5000, 25, 5)
r2 = Road(10, 10, 36, 7)

print(int(r1.get_mass()))
print(int(r2.get_mass()))