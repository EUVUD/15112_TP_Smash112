# All the images included come from this website: 
# https://www.spriters-resource.com/game_boy_advance/teenagemutantninjaturtlesubisoft/

class bullet:
    def __init__(self, name, x, y, velocity):
        self.x = x
        self.y = y
        self.sizeX = 16
        self.sizeY = 13
        self.velocity = velocity

class Char: #Common values of characters
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
        self.defend = False
        self.antiDefend = False
        self.antiDefCD = 0
        self.antiDefendAni = False

    def __repr__(self):
        return f'{self.name} with size {self.size} is at ({self.x},{self.y})'
    
    # Characters' abilities
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
        super().__init__('Donatello', x, y, 37, 43, 'Purple', direction, 
                         bulletList)
        self.rAttackLoc = f'../Graphics/Donatello/donatello_rAttack{self.attackComb}'
        self.lAttackLoc = '../Graphics/Donatello/donatello_lAttack'
        self.rStandLoc = '../Graphics/Donatello/donatello_rStand/'
        self.rWalkLoc = '../Graphics/Donatello/donatello_rWalk/'
        self.lStandLoc = '../Graphics/Donatello/donatello_lStand/'
        self.lWalkLoc = '../Graphics/Donatello/donatello_lWalk/'
        self.headLoc = '../Graphics/Donatello/donatello_head/sprite-removebg-preview.png'
        self.rDefLoc = '../Graphics/Donatello/donatello_rDefend/sprite-removebg-preview.png'
        self.lDefLoc = '../Graphics/Donatello/donatello_lDefend/sprite-removebg-preview.png'
        self.antiRDefLoc = '../Graphics/Donatello/donatello_antiRDefend/'
        self.antiLDefLoc = '../Graphics/Donatello/donatello_antiLDefend/'
        self.profileLoc = '../Graphics/Donatello/donatello_profile/sprite-removebg-preview.png'
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
        super().__init__('Leonardo', x, y, 37, 43, 'Blue', direction, 
                         bulletList)
        self.rAttackLoc = '../Graphics/Leonardo/leonardo_rAttack'
        self.lAttackLoc = '../Graphics/Leonardo/leonardo_lAttack'
        self.rStandLoc = '../Graphics/Leonardo/leonardo_rStand'
        self.rWalkLoc = '../Graphics/Leonardo/leonardo_rWalk'
        self.lStandLoc = '../Graphics/Leonardo/leonardo_lStand'
        self.lWalkLoc = '../Graphics/Leonardo/leonardo_lWalk'
        self.headLoc = '../Graphics/Leonardo/leonardo_head/sprite-removebg-preview.png'
        self.rDefLoc = '../Graphics/Leonardo/leonardo_rDefend/sprite-removebg-preview.png'
        self.lDefLoc = '../Graphics/Leonardo/leonardo_lDefend/sprite-removebg-preview.png'
        self.antiRDefLoc = '../Graphics/Leonardo/leonardo_antiRDefend/'
        self.antiLDefLoc = '../Graphics/Leonardo/leonardo_antiLDefend/'
        self.profileLoc = '../Graphics/Leonardo/leonardo_profile/sprite-removebg-preview.png'
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
        self.rAttackLoc = '../Graphics/Raphael/raphael_rAttack'
        self.lAttackLoc = '../Graphics/Raphael/raphael_lAttack'
        self.rStandLoc = '../Graphics/Raphael/raphael_rStand'
        self.rWalkLoc = '../Graphics/Raphael/raphael_rWalk'
        self.lStandLoc = '../Graphics/Raphael/raphael_lStand'
        self.lWalkLoc = '../Graphics/Raphael/raphael_lWalk'
        self.headLoc = '../Graphics/Raphael/raphael_head/sprite-removebg-preview.png'
        self.rDefLoc = '../Graphics/Raphael/raphael_rDefend/sprite-removebg-preview.png'
        self.lDefLoc = '../Graphics/Raphael/raphael_lDefend/sprite-removebg-preview.png'
        self.antiRDefLoc = '../Graphics/Raphael/raphael_antiRDefend/'
        self.antiLDefLoc = '../Graphics/Raphael/raphael_antiLDefend/'
        self.profileLoc = '../Graphics/Raphael/raphael_profile/sprite-removebg-preview.png'
        self.rAttackSprite = [f'{self.rAttackLoc}/{i}-removebg-preview.png' for i in range(6)]
        self.lAttackSprite = [f'{self.lAttackLoc}/{i}-removebg-preview.png' for i in range(6)]
        self.rStandSprite = [f'{self.rStandLoc}/{i}-removebg-preview.png' for i in range(12)]
        self.rWalkSprite = [f'{self.rWalkLoc}/{i}-removebg-preview.png' for i in range(12, 22)]
        self.lStandSprite = [f'{self.lStandLoc}/{i}-removebg-preview.png' for i in range(12)]
        self.lWalkSprite = [f'{self.lWalkLoc}/{i}-removebg-preview.png' for i in range(12, 22)]
        self.antiRDefSprite = [f'{self.antiRDefLoc}/{i}-removebg-preview.png' for i in range(7)]
        self.antiLDefSprite = [f'{self.antiLDefLoc}/{i}-removebg-preview.png' for i in range(7)]

def characterList(app):
    # Load the character list
    app.chrList = []
    donatello = Donatello(None, app.height/4,None, app.projection)
    leonardo = Leonardo(None, app.height/4,None, app.projection)
    raphael = Raphael(None, app.height/4,None, app.projection)
    app.chrList.append(donatello)
    app.chrList.append(leonardo)
    app.chrList.append(raphael)