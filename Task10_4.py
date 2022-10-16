class Car:
    def __init__(
            self,
            color: str,
            name: str,
            is_police: bool = False
    ):
        self.color = color
        self.name = name
        self.is_police = True if is_police else False

        self.speed = 0
        self._direction = ''

    def go(self, speed: float):
        try:
            self.speed = float(speed)
        except ValueError:
            pass

    def stop(self):
        self.speed = 0

    def turn(self, direction: str):
        if direction not in ('left', 'right'):
            print(f"'{direction}' неверное направление")
            return

        if not self.speed:
            print(f"'Не может принять направление {direction}' ")
            return

        self._direction = direction

    def show_speed(self):
        print(f'Моя скорость составляет {self.speed} км/ч')

        if (hasattr(self, '_max_granted_speed')
                and self._max_granted_speed
                and self.speed > self._max_granted_speed):
            print(f'Превышает скорость на {self.speed - self._max_granted_speed} км/ч')

    def direction(self):
        return self._direction


class TownCar(Car):
    _max_granted_speed = 60


class SportCar(Car):
    pass


class WorkCar(Car):
    _max_granted_speed = 40


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)


if __name__ == '__main__':
    cars_data = {
        ('Желтый', 'Aston Martin Cygnet'): TownCar,
        ('Зеленый', 'BMW M3'): SportCar,
        ('Белый', 'VAZ 2106'): WorkCar,
        ('Синий', 'Ford Crown'): PoliceCar,
    }

    for car_descr, car_cls in cars_data.items():
        car = car_cls(*car_descr)

        print('#######################################')
        print(f"Марка машины '{car.name}'")
        print(f"Цвет машины '{car.color}'")
        print(f"Полицейская машина '{car.is_police}'")
        print(f"Скорость машины '{car.speed}'")
        print(f"Направление машины '{car.direction}'")
        print(f"Скорость '{car.show_speed()}'")

        car.turn('asd')
        car.turn('left')
        car.go('asd')
        print("Скорость", car.speed)
        car.go(30)
        car.show_speed()
        car.go(45)
        car.show_speed()
        car.go(75)
        car.show_speed()
        car.turn('left')
        print(f"Направление '{car.direction}'")
        car.turn('right')
        print(f"Направление '{car.direction}'")
        car.stop()
        car.show_speed()
        print('#######################################\n\n')
