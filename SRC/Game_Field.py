#Field Images are from https://www.spriters-resource.com/ms_dos/dukenukem2/sheet/24155/
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
    def __init__(self,name, x, y, sizeX, sizeY, color):
        self.name = name
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.color = color

    def __repr__(self):
        return f'{self.name}'
    
    def __eq__(self, other):
        if isinstance(other, Block) and self.name == other.name:
            return True
        return False

def fieldSetUp(app):
    # Field 1
    app.defaultField = Field('City', '../Graphics/Background/10615.png')
    # Blocks
    app.ground = Block('ground', 0, app.height/4*3, app.width, app.height - app.height/4*3, 'black')
    app.level1 = Block('level1', app.width/4*3, 300, 100, 20, 'black')
    app.level2 = Block('level2', app.width/6, 300, 100, 20, 'black')
    app.level3 = Block('level3', app.width/3, 150, 300, 20, 'black')
    app.defaultField.add(app.ground)
    app.defaultField.add(app.level1)
    app.defaultField.add(app.level2)
    app.defaultField.add(app.level3)

    # Field 2
    app.field2 = Field('Mountain', '../Graphics/Background/mountain.png')
    app.brickGround = Block('brickG', 0, 505, app.width, app.height - 505, 'black')
    app.leftSideStand = Block('leftSideStand', 0, 400, app.width/6, app.height - 400, 'black')
    app.rightSideStand = Block('rightSideStand', app.width - app.width/6, 
                               400, app.width/6, app.height - 400, 'black')
    app.middleStand = Block('middleStand', app.width/7*2, 300, app.width - app.width/7*4, 30, 'black')
    app.field2.add(app.brickGround)
    app.field2.add(app.leftSideStand)
    app.field2.add(app.rightSideStand)
    app.field2.add(app.middleStand)

    #Field 3
    app.field3 = Field('Volcano', '../Graphics/Background/volcano.png')
    app.pyramidBottom = Block('pyramidBottom', 0, 500, app.width, app.height-500, 'darkRed')
    app.pyramidMiddle = Block('pyramidMiddle', app.width/4, 350, app.width/2, 150, 'darkRed')
    app.pyramidTop = Block('pyramidTop', app.width/3, 250, app.width/3, 100, 'darkRed')
    app.field3.add(app.pyramidBottom)
    app.field3.add(app.pyramidMiddle)
    app.field3.add(app.pyramidTop)

    #Field 4
    app.field4 = Field('Power of Nature', '../Graphics/Background/powerOfNature.png')
    app.grassGround = Block('grassG', 0, 450, app.width, app.height-450, 'green')
    app.shortLevel = Block('shortLevel', 100, 350, 200, 20, 'black')
    app.middleLevel = Block('middleLevel', 330, 250, 150, 20, 'black')
    app.upperLevel = Block('upperLevel', 480, 150, app.width-480, 20, 'black')
    app.field4.add(app.grassGround)
    app.field4.add(app.shortLevel)
    app.field4.add(app.middleLevel)
    app.field4.add(app.upperLevel)




def fieldList(app):
    app.fields = [[None, None], [None, None]]
    app.fields[0][0] = app.defaultField
    app.fields[0][1] = app.field2
    app.fields[1][0] = app.field3
    app.fields[1][1] = app.field4
