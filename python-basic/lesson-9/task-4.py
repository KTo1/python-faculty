class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = False

    def is_police(self):
        return self._is_police

    def go(self):
        print(f'{self.name} go')

    def stop(self):
        print(f'{self.name} stop')

    def turn(self, direction):
        print(f'{self.name} turn {direction}')

    def show_speed(self):
        print(f'{self.name} speed {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Speed limit {60} exceed')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Speed limit {40} exceed')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = True


class SportCar(Car):
    pass


town_car = TownCar(80, 'red', 'lancer')
work_car = WorkCar(60, 'green', 'dyna')
police_car = PoliceCar(120, 'blue', 'police')
sport_car = SportCar(100, 'yellow', 'celica')

town_car.go()
town_car.turn('left')

town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.show_speed()
