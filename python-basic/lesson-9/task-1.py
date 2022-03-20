from itertools import cycle
from time import sleep


class TrafficLight:

    def __init__(self):
        self.__color_dict = {'красный': 7, 'желтый': 2, 'зеленый': 5}
        self.__color = ['красный', 'желтый', 'зеленый']

    def running(self):
        for color in cycle(self.__color):
            print(color)
            sleep(self.__color_dict[color])


traffic_light = TrafficLight()
traffic_light.running()
