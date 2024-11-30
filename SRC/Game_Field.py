class Field:
    def __init__(self, name):
        self.name = name
        self.blocks = []

    def __repr__(self):
        return f'{self.blocks}'

    def add(self, other):
        if isinstance(other, Block):
            self.blocks.append(other)

class Block:
    def __init__(self,name, x, y, sizeX, sizeY):
        self.name = name
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY

    def __repr__(self):
        return f'{self.name}'
        