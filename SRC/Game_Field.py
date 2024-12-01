class Field:
    def __init__(self, name, image):
        self.name = name
        self.blocks = []
        self.image = image

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

def fieldSetUp(app):
    # Field
    app.defaultField = Field('default', '../Graphics/Background/10615.png')
    # Blocks
    app.ground = Block('ground', 0, app.height/4*3, app.width, app.height - app.height/4*3)
    app.level1 = Block('level1', app.width/4*3, 300, 100, 20)
    app.level2 = Block('level2', app.width/6, 300, 100, 20)
    app.level3 = Block('level3', app.width/3, 150, 300, 20)
    app.defaultField.add(app.ground)
    app.defaultField.add(app.level1)
    app.defaultField.add(app.level2)
    app.defaultField.add(app.level3)


def fieldList(app):
    app.fields = [[None, None], [None, None]]
    app.fields[0][0] = app.defaultField
