from cmu_graphics import *
import Game_Char

def onAppStart(app):
    app.ground = 300
    app.projection = []
    app.player1 = Game_Char.char('Orange', app.width/4, app.height/4, 20, 'orange', None, app.projection)


def redrawAll(app):
    # Instruction:
    drawLabel('Use left, up, right, down to move the block', app.width/2, 20, size = 14)
    drawLabel('Use k to shoot the bullet', app.width/2, 35, size = 14)
    # draw the character
    drawRect(0, app.ground, app.width, app.height, fill = 'black')
    if app.player1.direction == 'left':
        drawRect(app.player1.x, app.player1.y, app.player1.size,
                 app.player1.size, fill = app.player1.color)
        drawLine(app.player1.x+app.player1.size, app.player1.y+app.player1.size/2,
                 app.player1.x, app.player1.y+app.player1.size/2, arrowEnd = True)
    else:
        drawRect(app.player1.x, app.player1.y, app.player1.size
                , app.player1.size, fill = app.player1.color)
        drawLine(app.player1.x, app.player1.y+app.player1.size/2,
                 app.player1.x+app.player1.size, app.player1.y+app.player1.size/2, arrowEnd = True)
        

    # draw the Bullet
    for bullet in app.projection:
        drawCircle(bullet.x, bullet.y, bullet.size, fill = 'black')

def onKeyPress(app, key):
    # Player1 Action
    #Jump
    if key == 'up':
        if app.player1.jump == False:
            jumpPlay(app, app.player1)
    #Shoot the bullet
    if key == 'k':
        app.player1.shoot()

def jumpPlay(app, player):
    app.player1.jump = True
    app.player1.dy = -35
    

def onKeyHold(app, keys):
    # Still Player1 Movement
    if 'left' in keys:
        app.player1.x -= 5
        app.player1.direction = 'left'
    elif 'right' in keys:
        app.player1.x += 5
        app.player1.direction = 'right'
    if app.player1.x + app.player1.size > app.width: #Bounded Motion
        app.player1.x = app.width-app.player1.size
    elif app.player1.x < 0:
        app.player1.x = 0

def onStep(app):
    gravSimul(app)
    bulletFly(app)

#Gravity Simulation

def gravSimul(app):
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



runApp()