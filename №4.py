"""
    4. Реализуйте базовый класс Car.
    У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
    Для классов TownCar и WorkCar переопределите метод show_speed.
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

    Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
    Выполните вызов методов и также покажите результат.
"""


class Car :
    def __init__(self, speed, color, name, is_police) :
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self) :
        return f'{self.name} поехала'

    def stop(self) :
        return f'{self.name} остановилась'

    def turn_right(self) :
        return f'{self.name} повернула на право'

    def turn_left(self) :
        return f'{self.name} повернула на лево'

    def show_speed(self) :
        return f'Текущая скорость {self.name} = {self.speed}'


class TownCar(Car) :
    def __init__(self, speed, color, name, is_police) :
        super().__init__(speed, color, name, is_police)

    def show_speed(self) :
        print(f'Текущая скорость {self.name} = {self.speed}')

        if self.speed > 60 :
            return f'Скорость {self.name} слишком высокая'
        else :
            return f'Текущая скорость {self.name} нормальная для городской среды'


class WorkCar(Car) :
    def __init__(self, speed, color, name, is_police) :
        super().__init__(speed, color, name, is_police)

    def show_speed(self) :
        print(f'Текущая скорость  {self.name} = {self.speed}')

        if self.speed > 40 :
            return f'Скорость {self.name} слишком высокая'
        else :
            return f'Текущая скорость {self.name} нормальная'


nisan = TownCar(30, 'Белый', 'Nisan', False)
audi = TownCar(70, 'Черный', 'Ауди', True)
tesla = WorkCar(70, 'Золотой', 'Тесла', True)
jaguar = WorkCar(25, 'Золотой', 'Ягуар', False)

print(tesla.turn_left())
print(f'Когда {nisan.turn_right()}, {tesla.stop()}')
print(f'{audi.name} {audi.color} цвета')
print(f'{audi.name} полицейская машина? {audi.is_police}')
print(f'{jaguar.name}  полицейская машина? {jaguar.is_police}')
print(audi.show_speed())
print(jaguar.show_speed())
print(tesla.show_speed())
print(nisan.show_speed())
