# All the images included come from this website: 
# https://www.spriters-resource.com/game_boy_advance/teenagemutantninjaturtlesubisoft/

class bullet:
    def __init__(self, name, x, y, velocity):
        self.x = x
        self.y = y
        self.sizeX = 16
        self.sizeY = 13
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
        self.attack = False
        self.attackAni = False
        self.attackCD = 0
        self.shuriCD = 0
        self.color = color
        self.dx = 0
        self.dy = 0
        self.direction = direction
        self.bulletList = bulletList
        self.health = 5
        self.attackComb = 1
        self.rise = False
        self.loc = None
        self.defend = False
        self.antiDefend = False
        self.antiDefCD = 0
        self.antiDefendAni = False

    def __repr__(self):
        return f'{self.name} with size {self.size} is at ({self.x},{self.y})'
    
    def shootChr(self):
        yPos = self.y
        velocity = None
        if self.direction == 'left':
            xPos = self.x - self.sizeX
            velocity = -7
        else:
            xPos = self.x + self.sizeX
            velocity = 7
        newBullet = bullet('bullet', xPos, yPos, velocity)
        self.bulletList.append(newBullet)
        self.shuriCD = 15

    def attackChr(self):
        self.attack = True
        self.attackAni = True
        self.attackCD = 15

    def jumpChr(self):
        self.jump = True
        self.dy = -35

    def antiDefendChr(self):
        self.antiDefend = True
        self.antiDefendAni = True


class Donatello(Char):
    def __init__(self, x, y, direction, bulletList):
        super().__init__('Donatello', x, y, 37, 43, 'Purple', direction, bulletList)
        self.rAttackLoc = f'../Graphics/Donatello_cropped/donatello_rAttack{self.attackComb}'
        self.lAttackLoc = '../Graphics/Donatello_cropped/donatello_lAttack'
        self.rStandLoc = '../Graphics/Donatello_cropped/donatello_rStand/'
        self.rWalkLoc = '../Graphics/Donatello_cropped/donatello_rWalk/'
        self.lStandLoc = '../Graphics/Donatello_cropped/donatello_lStand/'
        self.lWalkLoc = '../Graphics/Donatello_cropped/donatello_lWalk/'
        self.headLoc = '../Graphics/Donatello_cropped/donatello_head/sprite-removebg-preview.png'
        self.rDefLoc = '../Graphics/Donatello_cropped/donatello_rDefend/sprite-removebg-preview.png'
        self.lDefLoc = '../Graphics/Donatello_cropped/donatello_lDefend/sprite-removebg-preview.png'
        self.antiRDefLoc = '../Graphics/Donatello_cropped/donatello_antiRDefend/'
        self.antiLDefLoc = '../Graphics/Donatello_cropped/donatello_antiLDefend/'
        self.profileLoc = '../Graphics/Donatello_cropped/donatello_profile/sprite-removebg-preview.png'
        self.rAttackSprite = [f'{self.rAttackLoc}/{i}-removebg-preview.png' for i in range(6)]
        self.lAttackSprite = [f'{self.lAttackLoc}/{i}-removebg-preview.png' for i in range(6)]
        self.rStandSprite = [f'{self.rStandLoc}/{i}-removebg-preview.png' for i in range(12)]
        self.rWalkSprite = [f'{self.rWalkLoc}/{i}-removebg-preview.png' for i in range(12, 22)]
        self.lStandSprite = [f'{self.lStandLoc}/{i}-removebg-preview.png' for i in range(12)]
        self.lWalkSprite = [f'{self.lWalkLoc}/{i}-removebg-preview.png' for i in range(12, 22)]
        self.antiRDefSprite = [f'{self.antiRDefLoc}/{i}-removebg-preview.png' for i in range(5)]
        self.antiLDefSprite = [f'{self.antiLDefLoc}/{i}-removebg-preview.png' for i in range(5)]


class Leonardo(Char):
    def __init__(self, x, y, direction, bulletList):
        super().__init__('Leonardo', x, y, 37, 43, 'Blue', direction, bulletList)
        self.rAttackLoc = '../Graphics/Leonardo_cropped/leonardo_rAttack'
        self.lAttackLoc = '../Graphics/Leonardo_cropped/leonardo_lAttack'
        self.rStandLoc = '../Graphics/Leonardo_cropped/leonardo_rStand'
        self.rWalkLoc = '../Graphics/Leonardo_cropped/leonardo_rWalk'
        self.lStandLoc = '../Graphics/Leonardo_cropped/leonardo_lStand'
        self.lWalkLoc = '../Graphics/Leonardo_cropped/leonardo_lWalk'
        self.headLoc = '../Graphics/Leonardo_cropped/leonardo_head/sprite-removebg-preview.png'
        self.rDefLoc = '../Graphics/Leonardo_cropped/leonardo_rDefend/sprite-removebg-preview.png'
        self.lDefLoc = '../Graphics/Leonardo_cropped/leonardo_lDefend/sprite-removebg-preview.png'
        self.antiRDefLoc = '../Graphics/Leonardo_cropped/leonardo_antiRDefend/'
        self.antiLDefLoc = '../Graphics/Leonardo_cropped/leonardo_antiLDefend/'
        self.profileLoc = '../Graphics/Leonardo_cropped/leonardo_profile/sprite-removebg-preview.png'
        self.rAttackSprite = [f'{self.rAttackLoc}/{i}-removebg-preview.png' for i in range(6)]
        self.lAttackSprite = [f'{self.lAttackLoc}/{i}-removebg-preview.png' for i in range(6)]
        self.rStandSprite = [f'{self.rStandLoc}/{i}-removebg-preview.png' for i in range(12)]
        self.rWalkSprite = [f'{self.rWalkLoc}/{i}-removebg-preview.png' for i in range(12, 22)]
        self.lStandSprite = [f'{self.lStandLoc}/{i}-removebg-preview.png' for i in range(12)]
        self.lWalkSprite = [f'{self.lWalkLoc}/{i}-removebg-preview.png' for i in range(12, 22)]
        self.antiRDefSprite = [f'{self.antiRDefLoc}/{i}-removebg-preview.png' for i in range(7)]
        self.antiLDefSprite = [f'{self.antiLDefLoc}/{i}-removebg-preview.png' for i in range(7)]


class Raphael(Char):
    def __init__(self, x, y, direction, bulletList):
        super().__init__('Raphael', x, y, 37, 43, 'Red', direction, bulletList)
        self.rAttackLoc = '../Graphics/Raphael_cropped/raphael_rAttack'
        self.lAttackLoc = '../Graphics/Raphael_cropped/raphael_lAttack'
        self.rStandLoc = '../Graphics/Raphael_cropped/raphael_rStand'
        self.rWalkLoc = '../Graphics/Raphael_cropped/raphael_rWalk'
        self.lStandLoc = '../Graphics/Raphael_cropped/raphael_lStand'
        self.lWalkLoc = '../Graphics/Raphael_cropped/raphael_lWalk'
        self.headLoc = '../Graphics/Raphael_cropped/raphael_head/sprite-removebg-preview.png'
        self.rDefLoc = '../Graphics/Raphael_cropped/raphael_rDefend/sprite-removebg-preview.png'
        self.lDefLoc = '../Graphics/Raphael_cropped/raphael_lDefend/sprite-removebg-preview.png'
        self.antiRDefLoc = '../Graphics/Raphael_cropped/raphael_antiRDefend/'
        self.antiLDefLoc = '../Graphics/Raphael_cropped/raphael_antiLDefend/'
        self.profileLoc = '../Graphics/Raphael_cropped/raphael_profile/sprite-removebg-preview.png'
        self.rAttackSprite = [f'{self.rAttackLoc}/{i}-removebg-preview.png' for i in range(6)]
        self.lAttackSprite = [f'{self.lAttackLoc}/{i}-removebg-preview.png' for i in range(6)]
        self.rStandSprite = [f'{self.rStandLoc}/{i}-removebg-preview.png' for i in range(12)]
        self.rWalkSprite = [f'{self.rWalkLoc}/{i}-removebg-preview.png' for i in range(12, 22)]
        self.lStandSprite = [f'{self.lStandLoc}/{i}-removebg-preview.png' for i in range(12)]
        self.lWalkSprite = [f'{self.lWalkLoc}/{i}-removebg-preview.png' for i in range(12, 22)]
        self.antiRDefSprite = [f'{self.antiRDefLoc}/{i}-removebg-preview.png' for i in range(7)]
        self.antiLDefSprite = [f'{self.antiLDefLoc}/{i}-removebg-preview.png' for i in range(7)]

def characterList(app):
    app.chrList = []
    donatello = Donatello(None, app.height/4,None, app.projection)
    leonardo = Leonardo(None, app.height/4,None, app.projection)
    raphael = Raphael(None, app.height/4,None, app.projection)
    app.chrList.append(donatello)
    app.chrList.append(leonardo)
    app.chrList.append(raphael)