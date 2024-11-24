from cmu_graphics import *
import Game_Char
import BT_Composite
import BT_Behavior

def onAppStart(app):
    reStart(app)
    app.gameOver = False
    

def reStart(app):
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


def redrawAll(app):
    # Draw Background
    drawImage('../Graphics/Background/10615.png', 0, 0, width = app.width, height = app.height)
    # Instruction:
    drawLabel('Use w, a, s, d to move the Donatello', app.width/2, 20, size = 14)
    drawLabel('Use g to shoot the bullet from Donatello', app.width/2, 35, size = 14)
    drawLabel('Use up, left, down, right to move Leonardo', app.width/2, 50, size = 14)
    drawLabel('Use k to shoot the bullet from Leonardo', app.width/2, 65, size = 14)
    drawLabel('Red Circles indicate how many lives left', app.width/2, 80, size = 14)
    drawLabel('If game over, press r to restart', app.width/2, 95, size = 14)
    drawRect(0, app.ground, app.width, app.height, fill = 'black')
    #Draw Lives Left
    #Player 1
    drawLabel('Donatello health', 70, app.height - 40, fill = 'purple')
    for i in range(app.player1.health):
        drawCircle(20+30*i, app.height - 20, 10, fill = 'red')
    #Player 2
    drawLabel('Leonardo health', app.width - 70, app.height - 40, fill = 'blue')
    for i in range(app.player2.health):
        drawCircle(app.width-30*(i+1), app.height - 20, 10, fill = 'red')
    # Gameover:
    if app.gameOver == True:
        drawLabel('GameOver', app.width/2, app.height/2, fill = 'red', size = 40)
    # draw Player1 with Sprite
    if app.player1.direction == 'left': #Direction Left
        # For Direction Test purpose
        # drawLine(app.player1.x+app.player1.sizeX, app.player1.y+app.player1.sizeY/2,
        #          app.player1.x, app.player1.y+app.player1.sizeY/2, arrowEnd = True)
        if not app.player1.walk: #Stand
            drawImage(app.player1.lStandSprite[app.player1StandInd], app.player1.x, app.player1.y,
                    width = app.player1.sizeX, height = app.player1.sizeY)
        else: #Walk
            drawImage(app.player1.lWalkSprite[app.player1WalkInd], app.player1.x, app.player1.y,
                    width = app.player1.sizeX, height = app.player1.sizeY)
    else: # Direction Right or Initial
        # For Direction Test purpose
        # drawLine(app.player1.x, app.player1.y+app.player1.sizeY/2,
        #          app.player1.x+app.player1.sizeX, app.player1.y+app.player1.sizeY/2, arrowEnd = True)
        if not app.player1.walk:
            drawImage(app.player1.rStandSprite[app.player1StandInd], app.player1.x, app.player1.y,
                    width = app.player1.sizeX, height = app.player1.sizeY)
        else:
            drawImage(app.player1.rWalkSprite[app.player1WalkInd], app.player1.x, app.player1.y,
                    width = app.player1.sizeX, height = app.player1.sizeY)
    # draw Player2 with Sprite
    if app.player2.direction == 'right':
        # For Direction Test purpose
        # drawLine(app.player2.x, app.player2.y+app.player2.sizeY/2,
        #          app.player2.x+app.player2.sizeX, app.player2.y+app.player2.sizeY/2, arrowEnd = True)
        if not app.player2.walk: #Stand
            drawImage(app.player2.rStandSprite[app.player2StandInd], app.player2.x, app.player2.y,
                    width = app.player2.sizeX, height = app.player2.sizeY)
        else: #Walk
            drawImage(app.player2.rWalkSprite[app.player2WalkInd], app.player2.x, app.player2.y,
                    width = app.player2.sizeX, height = app.player2.sizeY)
    else:
        # drawLine(app.player2.x+app.player2.sizeX, app.player2.y+app.player2.sizeY/2,
        #          app.player2.x, app.player2.y+app.player2.sizeY/2, arrowEnd = True)
        if not app.player2.walk:
            drawImage(app.player2.lStandSprite[app.player2StandInd], app.player2.x, app.player2.y,
                    width = app.player2.sizeX, height = app.player2.sizeY)
        else:
            drawImage(app.player2.lWalkSprite[app.player2WalkInd], app.player2.x, app.player2.y,
                    width = app.player2.sizeX, height = app.player2.sizeY)
        

    # draw the Bullet
    for bullet in app.projection:
        drawCircle(bullet.x, bullet.y, bullet.size, fill = 'red')

def onKeyPress(app, key):
    # Player1 Action
    #Jump
    if not app.gameOver:
        if key == 'w':
            if app.player1.jump == False:
                jumpPlay(app.player1)
        if key == 'up':
            if app.player2.jump == False:
                jumpPlay(app.player2)
        #Shoot the bullet
        if key == 'g':
            app.player1.shoot()
        if key == 'k':
            app.player2.shoot()
    #Restart the game
    if app.gameOver == True:
        if key == 'r':
            reStart(app)
            app.gameOver = False

def jumpPlay(player):
    player.jump = True
    player.dy = -35
    

def onKeyHold(app, keys):
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

def onKeyRelease(app, key):
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


def onStep(app):
    if not app.gameOver:
        gravSimul(app)
        bulletFly(app)
        bulletHit(app)
        app.counter += 1
        if app.counter % 2 == 0:
            app.player1StandInd = (app.player1StandInd + 1) % len(app.player1.rStandSprite)
            app.player1WalkInd = (app.player1WalkInd + 1) % len(app.player1.rWalkSprite)
            app.player2StandInd = (app.player2StandInd + 1) % len(app.player2.rStandSprite)
            app.player2WalkInd = (app.player2WalkInd + 1) % len(app.player2.rWalkSprite)
        if app.counter % 2 == 0:
            testSequence.tick()


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
        if app.projection[index].x - app.projection[index].size < 0:
            app.projection.pop(index)
        elif app.projection[index].x + app.projection[index].size > app.width:
            app.projection.pop(index)
        index += 1

# Bullet hit function
def bulletHit(app):
    i = 0
    while i < len(app.projection):
        if (distance(app.projection[i].x, app.projection[i].y, 
                     app.player1.x+app.player1.sizeX/2, 
                     app.player1.y+app.player1.sizeY/2)
            < app.projection[i].size + app.player1.sizeX/2):
            if app.player1.health == 1:
                app.projection[i].velocity = 0
                app.gameOver = True
            else:
                app.player1.health -= 1
                app.projection.pop(i)
        elif (distance(app.projection[i].x, app.projection[i].y, 
                       app.player2.x + app.player2.sizeX/2, 
                       app.player2.y + app.player2.sizeY/2)
            < app.projection[i].size + app.player2.sizeX/2):
            if app.player2.health == 1:
                app.projection[i].velocity = 0
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


runApp()