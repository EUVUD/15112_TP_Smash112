class Char:
    def __init__(self, name, x, y, size, color):
        self.name = name
        self.x = x
        self.y = y
        self.size = size
        self.jump = False
        self.color = color
        self.dy = 0

    def __repr__(self):
        return f'{self.name} with size {self.size} is at ({self.x},{self.y})'