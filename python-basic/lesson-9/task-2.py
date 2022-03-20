
class Road():
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_effect(self, mass_kg, depth):
        return int((self.__length * self.__width * mass_kg * depth) / 1000)


road = Road(20, 5000)
print(road.mass_effect(25, 5), 't.')
