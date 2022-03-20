class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Draw from base class')    


class Pen(Stationery):
    def draw(self):
        print(f'Draw {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Draw {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Draw {self.title}')


pen = Pen('pen') 
pencil = Pencil('pencil')       
handle = Handle('handle')

pen.draw()
pencil.draw()
handle.draw()
