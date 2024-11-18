from cmu_graphics import *
import Game_Char

def onAppStart(app):
    reStart(app)
    app.gameOver = False
    print(app.player1.direction, app.player2.direction)

def reStart(app):
    app.ground = 300
    app.projection = []
    app.player1 = Game_Char.char('Orange', app.width/4, app.height/4, 20, 'orange', 'right', app.projection)
    app.player2 = Game_Char.char('Blue', 3 * app.width/4, app.height/4, 20, 'blue', 'left', app.projection)


def redrawAll(app):
    # Instruction:
    drawLabel('Use w, a, s, d to move the orange block', app.width/2, 20, size = 14)
    drawLabel('Use g to shoot the bullet from orange', app.width/2, 35, size = 14)
    drawLabel('Use up, left, down, right to move the blue block', app.width/2, 50, size = 14)
    drawLabel('Use k to shoot the bullet from orange', app.width/2, 65, size = 14)
    drawLabel('If game over, press r to restart', app.width/2, 80, size = 14)
    drawRect(0, app.ground, app.width, app.height, fill = 'black')
    # Gameover:
    if app.gameOver == True:
        drawLabel('GameOver', app.width/2, app.height/2, fill = 'red', size = 40)
    # draw the character 1
    drawRect(app.player1.x, app.player1.y, app.player1.size,
                 app.player1.size, fill = app.player1.color)
    if app.player1.direction == 'left':
        drawLine(app.player1.x+app.player1.size, app.player1.y+app.player1.size/2,
                 app.player1.x, app.player1.y+app.player1.size/2, arrowEnd = True)
    else:
        drawLine(app.player1.x, app.player1.y+app.player1.size/2,
                 app.player1.x+app.player1.size, app.player1.y+app.player1.size/2, arrowEnd = True)
    # draw the character 2
    drawRect(app.player2.x, app.player2.y, app.player2.size,
                 app.player2.size, fill = app.player2.color)
    if app.player2.direction == 'right':
        drawLine(app.player2.x, app.player2.y+app.player2.size/2,
                 app.player2.x+app.player2.size, app.player2.y+app.player2.size/2, arrowEnd = True)
    else:
        drawLine(app.player2.x+app.player2.size, app.player2.y+app.player2.size/2,
                 app.player2.x, app.player2.y+app.player2.size/2, arrowEnd = True)
        

    # draw the Bullet
    for bullet in app.projection:
        drawCircle(bullet.x, bullet.y, bullet.size, fill = 'black')

def onKeyPress(app, key):
    # Player1 Action
    #Jump
    if app.gameOver == False:
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
    # Still Player1 Movement
    if 'a' in keys:
        app.player1.x -= 5
        app.player1.direction = 'left'
    elif 'd' in keys:
        app.player1.x += 5
        app.player1.direction = 'right'
    if app.player1.x + app.player1.size > app.width: #Bounded Motion
        app.player1.x = app.width-app.player1.size
    elif app.player1.x < 0:
        app.player1.x = 0
    # Player2 Movement:
    if 'left' in keys:
        app.player2.x -= 5
        app.player2.direction = 'left'
    elif 'right' in keys:
        app.player2.x += 5
        app.player2.direction = 'right'
    if app.player2.x + app.player2.size > app.width: #Bounded Motion
        app.player2.x = app.width-app.player2.size
    elif app.player2.x < 0:
        app.player2.x = 0

def onStep(app):
    if app.gameOver:
        return
    gravSimul(app)
    bulletFly(app)
    bulletHit(app)

#Gravity Simulation

def gravSimul(app):
    # Player 1 Sim
    if app.player1.jump == True:
        app.player1.dy += 2
        app.player1.y += app.player1.dy
    # In the air, the player keeps falling
    if app.player1.y < app.ground - app.player1.size:
        app.player1.y += 10
    else: # Stay on ground
        app.player1.y = app.ground - app.player1.size
    if app.player1.y >= app.ground - app.player1.size:
        app.player1.jump = False

    # Player 2 Sim
    if app.player2.jump == True:
        app.player2.dy += 2
        app.player2.y += app.player2.dy
    # In the air, the player keeps falling
    if app.player2.y < app.ground - app.player2.size:
        app.player2.y += 10
    else: # Stay on ground
        app.player2.y = app.ground - app.player2.size
    if app.player2.y >= app.ground - app.player2.size:
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
    for i in range(len(app.projection)):
        if (distance(app.projection[i].x, app.projection[i].y, 
                     app.player1.x+app.player1.size/2, 
                     app.player1.y+app.player1.size/2)
            < app.projection[i].size + app.player1.size/2):
            app.projection[i].velocity = 0
            app.gameOver = True
        elif (distance(app.projection[i].x, app.projection[i].y, 
                       app.player2.x + app.player2.size/2, 
                       app.player2.y + app.player2.size/2)
            < app.projection[i].size + app.player2.size/2):
            app.projection[i].velocity = 0
            app.gameOver = True



def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5


runApp()