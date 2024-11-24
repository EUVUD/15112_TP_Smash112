class bullet:
    def __init__(self, name, x, y, size, velocity):
        self.x = x
        self.y = y
        self.size = size
        self.velocity = velocity

class Char:
    def __init__(self, name, x, y, sizeX, sizeY, color, direction, bulletList):
        self.name = name
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.jump = True
        self.walk = False
        self.color = color
        self.dy = 0
        self.direction = direction
        self.bulletList = bulletList
        self.health = 5

    def __repr__(self):
        return f'{self.name} with size {self.size} is at ({self.x},{self.y})'
    
    def shoot(self):
        yPos = self.y + self.sizeY/2
        velocity = None
        if self.direction == 'left':
            xPos = self.x
            velocity = -10
        else:
            xPos = self.x + self.sizeX
            velocity = 10
        newBullet = bullet('bullet', xPos, yPos, 3, velocity)
        self.bulletList.append(newBullet)

class Donatello(Char):
    rStandLoc = '../Graphics/Donatello_cropped/donatello_rStand/'
    rWalkLoc = '../Graphics/Donatello_cropped/donatello_rWalk/'
    lStandLoc = '../Graphics/Donatello_cropped/donatello_lStand/'
    lWalkLoc = '../Graphics/Donatello_cropped/donatello_lWalk/'


    def __init__(self, x, y, direction, bulletList):
        super().__init__('Donatello', x, y, 37, 43, 'Purple', direction, bulletList)
        self.rStandSprite = [f'{Donatello.rStandLoc}/{i}-removebg-preview.png' for i in range(12)]
        self.rWalkSprite = [f'{Donatello.rWalkLoc}/{i}-removebg-preview.png' for i in range(12, 22)]
        self.lStandSprite = [f'{Donatello.lStandLoc}/{i}-removebg-preview.png' for i in range(12)]
        self.lWalkSprite = [f'{Donatello.lWalkLoc}/{i}-removebg-preview.png' for i in range(12, 22)]

class Leonardo(Char):
    rStandLoc = '../Graphics/Leonardo_cropped/leonardo_rStand'
    rWalkLoc = '../Graphics/Leonardo_cropped/leonardo_rWalk'
    lStandLoc = '../Graphics/Leonardo_cropped/leonardo_lStand'
    lWalkLoc = '../Graphics/Leonardo_cropped/leonardo_lWalk'

    def __init__(self, x, y, direction, bulletList):
        super().__init__('Donatello', x, y, 37, 43, 'Blue', direction, bulletList)
        self.rStandSprite = [f'{Leonardo.rStandLoc}/{i}-removebg-preview.png' for i in range(12)]
        self.rWalkSprite = [f'{Leonardo.rWalkLoc}/{i}-removebg-preview.png' for i in range(12, 22)]
        self.lStandSprite = [f'{Leonardo.lStandLoc}/{i}-removebg-preview.png' for i in range(12)]
        self.lWalkSprite = [f'{Leonardo.lWalkLoc}/{i}-removebg-preview.png' for i in range(12, 22)]
        






