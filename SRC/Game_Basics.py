from cmu_graphics import *
import Game_Char
import BT_Composite
import BT_Behavior

def onAppStart(app):
    reStart(app)
    app.gameOver = False
    app.rShuriLoc = '../Graphics/Shuriken/rShuriken'
    app.lShuriLoc = '../Graphics/Shuriken/lShuriken'
    app.rShuriSprite = [f'{app.rShuriLoc}/{i}-Photoroom.png' for i in range(3)]
    app.lShuriSprite = [f'{app.lShuriLoc}/{i}-Photoroom.png' for i in range(3)]
    

def reStart(app):
    app.aiMode = None
    app.counter = 0
    app.ground = 300
    app.projection = []
    #Player1 Basic Info and Sprite
    app.player1 = Game_Char.Donatello(app.width/4, app.height/4,'right', app.projection)
    app.player1StandInd = 0
    app.player1WalkInd = 0
    #Player2 Basic Info and Sprite
    app.player2 = Game_Char.Leonardo(3 * app.width/4, app.height/4,'left', app.projection)
    app.player2StandInd = 0
    app.player2WalkInd = 0
    app.player2AttackInd = 0
    #Bullet Fly
    app.bulletRightInd = 0
    app.bulletLeftInd = 0

# Start Screen

def start_redrawAll(app):
    drawLabel('Welcome to Smash-112', 200, 160, size=24, bold=True)
    drawLabel('Press a to enter AI player mode', 200, 200, size=24)
    drawLabel('Press m to enter Multi-player mode', 200, 240, size=24)

def start_onKeyPress(app, key):
    if key == 'a' or key == 'm':
        if key == 'a':
            app.aiMode = True
        elif key == 'm':
            app.aiMode = False
        setActiveScreen('game')

# Game Screen

def game_redrawAll(app):
    # Draw Background
    drawImage('../Graphics/Background/10615.png', 0, 0, width = app.width, height = app.height)
    drawInstruction(app)
    drawPlayer1(app)
    drawPlayer2(app)
    drawBullet(app)

def drawInstruction(app):
    drawLabel('Use w, a, s, d to move the Donatello', app.width/2, 20, size = 14)
    drawLabel('Use g to shoot the bullet from Donatello', app.width/2, 35, size = 14)
    drawLabel('Use up, left, down, right to move Leonardo', app.width/2, 50, size = 14)
    drawLabel('Use k to shoot the bullet from Leonardo', app.width/2, 65, size = 14)
    drawLabel('Red Circles indicate how many lives left', app.width/2, 80, size = 14)
    drawLabel('If game over, press r to restart', app.width/2, 95, size = 14)
    drawRect(0, app.ground, app.width, app.height, fill = 'black')
    # Gameover:
    if app.gameOver == True:
        drawLabel('GameOver', app.width/2, app.height/2, fill = 'red', size = 40)

def drawPlayer1(app):
    #Draw Player 1 lives left
    drawLabel('Donatello health', 70, app.height - 40, fill = 'purple')
    for i in range(app.player1.health):
        drawCircle(20+30*i, app.height - 20, 10, fill = 'red')
    # draw Player1 with Sprite
    if app.player1.direction == 'left': #Direction Left
        if app.player1.walk: 
            drawImage(app.player1.lWalkSprite[app.player1WalkInd], app.player1.x, app.player1.y,
                    width = app.player1.sizeX, height = app.player1.sizeY)
        else: 
            drawImage(app.player1.lStandSprite[app.player1StandInd], app.player1.x, app.player1.y,
                    width = app.player1.sizeX, height = app.player1.sizeY)
    else: # Direction Right or Initial
        if app.player1.walk:
            drawImage(app.player1.rWalkSprite[app.player1WalkInd], app.player1.x, app.player1.y,
                    width = app.player1.sizeX, height = app.player1.sizeY)
        else:
            drawImage(app.player1.rStandSprite[app.player1StandInd], app.player1.x, app.player1.y,
                    width = app.player1.sizeX, height = app.player1.sizeY)
    
    
def drawPlayer2(app):
    #Draw Player 2 lives left
    drawLabel('Leonardo health', app.width - 70, app.height - 40, fill = 'blue')
    for i in range(app.player2.health):
        drawCircle(app.width-30*(i+1), app.height - 20, 10, fill = 'red')

    # draw Player2 with Sprite
    if app.player2.direction == 'right':
        if app.player2.attack:
            imageDimension = getImageSize(app.player2.rAttackSprite[app.player2AttackInd])
            imageWidth = imageDimension[0]
            drawImage(app.player2.rAttackSprite[app.player2AttackInd],
                      app.player2.x, app.player2.y,
                      width = imageWidth, height = app.player2.sizeY)
        elif app.player2.walk: #Walk
            drawImage(app.player2.rWalkSprite[app.player2WalkInd], app.player2.x, app.player2.y,
                    width = app.player2.sizeX, height = app.player2.sizeY)
        else: #Walk
            drawImage(app.player2.rStandSprite[app.player2StandInd], app.player2.x, app.player2.y,
                    width = app.player2.sizeX, height = app.player2.sizeY)
    else:
        if app.player2.attack:
            imageDimension = getImageSize(app.player2.lAttackSprite[app.player2AttackInd])
            imageWidth = imageDimension[0]
            drawImage(app.player2.lAttackSprite[app.player2AttackInd],
                      app.player2.x, app.player2.y,
                      width = imageWidth, height = app.player2.sizeY)
        elif app.player2.walk:
            drawImage(app.player2.lWalkSprite[app.player2WalkInd], app.player2.x, app.player2.y,
                    width = app.player2.sizeX, height = app.player2.sizeY)
        else:
            drawImage(app.player2.lStandSprite[app.player2StandInd], app.player2.x, app.player2.y,
                    width = app.player2.sizeX, height = app.player2.sizeY)


def drawBullet(app):
    for bullet in app.projection:
        if bullet.velocity > 0:
            drawImage(app.rShuriSprite[app.bulletRightInd], bullet.x - bullet.sizeX/2, 
                      bullet.y - bullet.sizeY/2, width = bullet.sizeX, height = bullet.sizeY)
        else:
            drawImage(app.lShuriSprite[app.bulletLeftInd], bullet.x - bullet.sizeX/2, 
                      bullet.y - bullet.sizeY/2, width = bullet.sizeX, height = bullet.sizeY)

def game_onKeyPress(app, key):
    
    #Jump
    if not app.gameOver:
        # Player1 Action
        if key == 'w':
            if app.player1.jump == False:
                jumpPlay(app.player1)
        # Player2 Action
        if key == 'up':
            if app.player2.jump == False:
                jumpPlay(app.player2)
        #Shoot the bullet
        # Player1 Action
        if key == 'h':
            app.player1.shoot()
        # Player2 Action
        if key == 'k':
            app.player2.shoot()
        if key == 'j':
            app.player2.attack = True
            if isHit(app.player1, app.player2) and app.player2.attack:
                app.player1.health -= 1
    #Restart the game
    if app.gameOver == True:
        if key == 'r':
            setActiveScreen('start')
            reStart(app)
            app.gameOver = False

def isHit(player1, player2):
    print(distance(player1.x+player1.sizeX/2, player1.y+player1.sizeY/2,
                player2.x+player2.sizeX/2, player2.y+player2.sizeY/2))
    if (distance(player1.x+player1.sizeX/2, player1.y+player1.sizeY/2,
                player2.x+player2.sizeX/2, player2.y+player2.sizeY/2)
                < 30):
        return True
    else:
        return False

def jumpPlay(player):
    player.jump = True
    player.dy = -35
    

def game_onKeyHold(app, keys):
    if app.gameOver:
        return
    # Still Player1 Movement
    if 'a' in keys:
        app.player1.x -= 5
        app.player1.direction = 'left'
        app.player1.walk = True #Determine Motion
    elif 'd' in keys:
        app.player1.x += 5
        app.player1.direction = 'right'
        app.player1.walk = True
    if app.player1.x + app.player1.sizeX > app.width: #Bounded Motion
        app.player1.x = app.width-app.player1.sizeX
    elif app.player1.x < 0:
        app.player1.x = 0
    # Player2 Movement:
    if 'left' in keys:
        app.player2.x -= 5
        app.player2.direction = 'left'
        app.player2.walk = True
    elif 'right' in keys:
        app.player2.x += 5
        app.player2.direction = 'right'
        app.player2.walk = True
    if app.player2.x + app.player2.sizeX > app.width: #Bounded Motion
        app.player2.x = app.width-app.player2.sizeX
    elif app.player2.x < 0:
        app.player2.x = 0

def game_onKeyRelease(app, key):
    if app.gameOver:
        return 
    if key == 'd':
        app.player1.walk = False
    elif key == 'a':
        app.player1.walk = False
    if key == 'left':
        app.player2.walk = False
    elif key == 'right':
        app.player2.walk = False


def game_onStep(app):
    if app.player1.health == 0 or app.player2.health == 0:
        app.gameOver = True
    if not app.gameOver:
        if app.aiMode == True:
            testSequence.tick()
        gravSimul(app)
        bulletFly(app)
        bulletHit(app)
        spriteInd(app)
        app.counter += 1
        
            
def spriteInd(app):
    if app.counter % 2 == 0:
            #Player1 Sprite
            app.player1StandInd = (app.player1StandInd + 1) % len(app.player1.rStandSprite)
            app.player1WalkInd = (app.player1WalkInd + 1) % len(app.player1.rWalkSprite)

            #Player2 Sprite
            app.player2StandInd = (app.player2StandInd + 1) % len(app.player2.rStandSprite)
            app.player2WalkInd = (app.player2WalkInd + 1) % len(app.player2.rWalkSprite)
            if app.player2.attack:
                if app.player2AttackInd == len(app.player2.rAttackSprite)-1:
                    app.player2.attack = False
                    app.player2AttackInd = 0
                app.player2AttackInd += 1

            #Player3 Sprite
            app.bulletRightInd = (app.bulletRightInd + 1) % len(app.rShuriSprite)
            app.bulletLeftInd = (app.bulletLeftInd + 1) % len(app.lShuriSprite)


#Gravity Simulation

def gravSimul(app):
    # Player 1 Sim
    if app.player1.jump == True:
        app.player1.dy += 2
        app.player1.y += app.player1.dy
    # In the air, the player keeps falling
    if app.player1.y < app.ground - app.player1.sizeY:
        app.player1.y += 10
    else: # Stay on ground
        app.player1.y = app.ground - app.player1.sizeY
    if app.player1.y >= app.ground - app.player1.sizeY:
        app.player1.jump = False

    # Player 2 Sim
    if app.player2.jump == True:
        app.player2.dy += 2
        app.player2.y += app.player2.dy
    # In the air, the player keeps falling
    if app.player2.y < app.ground - app.player2.sizeY:
        app.player2.y += 10
    else: # Stay on ground
        app.player2.y = app.ground - app.player2.sizeY
    if app.player2.y >= app.ground - app.player2.sizeY:
        app.player2.jump = False

#Bullet fly function
def bulletFly(app):
    index = 0
    while index < len(app.projection):
        app.projection[index].x += app.projection[index].velocity
        if app.projection[index].x - app.projection[index].sizeX < 0:
            app.projection.pop(index)
        elif app.projection[index].x + app.projection[index].sizeX > app.width:
            app.projection.pop(index)
        index += 1

# Bullet hit function
def bulletHit(app):
    i = 0
    while i < len(app.projection):
        if (distance(app.projection[i].x, app.projection[i].y, 
                     app.player1.x+app.player1.sizeX/2, 
                     app.player1.y+app.player1.sizeY/2)
            < app.projection[i].sizeX/4 + app.player1.sizeX/2):
            if app.player1.health == 1:
                app.projection[i].velocity = 0
                app.player1.health -= 1
                app.gameOver = True
            else:
                app.player1.health -= 1
                app.projection.pop(i)
        elif (distance(app.projection[i].x, app.projection[i].y, 
                       app.player2.x + app.player2.sizeX/2, 
                       app.player2.y + app.player2.sizeY/2)
            < app.projection[i].sizeX/4 + app.player2.sizeX/2):
            if app.player2.health == 1:
                app.projection[i].velocity = 0
                app.player2.health -= 1
                app.gameOver = True
            else:
                app.player2.health -= 1
                app.projection.pop(i)
        i += 1


#Behavior Tree Part(Will be put into another file later)
def towardEnemy(app):
    if abs(app.player1.x - app.player2.x) < 70:
        app.player2.walk = False
        return 'Success'
    else:
        if app.player1.x < app.player2.x:
            app.player2.x -= 5
            app.player2.walk = True
            app.player2.direction = 'left'
        elif app.player1.x > app.player2.x:
            app.player2.x += 5
            app.player2.walk = True
            app.player2.direction = 'right'
        return 'Running'
    
def attackEnemy(app):
    if abs(app.player1.x - app.player2.x) > 50:
        app.player2.shoot()


mvTwdEnemy = BT_Behavior.Action(towardEnemy, 'mvTwdEnemy', app)
attack = BT_Behavior.Action(attackEnemy, 'attack', app)

testSequence = BT_Composite.Sequence('testSequence')
testSequence.add(mvTwdEnemy)
testSequence.add(attack)




def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5


runAppWithScreens(initialScreen = 'start')