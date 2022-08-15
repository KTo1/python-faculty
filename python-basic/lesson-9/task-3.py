
class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._Worker__income['wage'] + self._Worker__income['bonus']


position1 = Position('Ivan', 'Ivanov', 'Software engineer', 1000, 10)
position2 = Position('Vasiliy', 'Vasiliev', 'Python developer', 300000, 300)

print(f'Position 1: {position1.get_full_name()} {position1.get_total_income()}')
print(f'Position 2: {position2.get_full_name()} {position2.get_total_income()}')


