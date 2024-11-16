from cmu_graphics import *
import Game_Char

def onAppStart(app):
    app.ground = 300
    app.player1 = Game_Char.Char('Orange', app.width/4, app.height/4, 20, 'orange')


def redrawAll(app):
    drawRect(0, app.ground, app.width, app.height, fill = 'black')
    drawRect(app.player1.x, app.player1.y, app.player1.size
             , app.player1.size, fill = app.player1.color)
        

def onKeyPress(app, key):
    if key == 'up':
        if app.player1.jump == False:
            app.player1.jump = True
            jumpPlay(app, app.player1)

def jumpPlay(app, player):
    app.player1.dy = -35
    

def onKeyHold(app, keys):
    if 'left' in keys:
        app.player1.x -= 5
    elif 'right' in keys:
        app.player1.x += 5
    if app.player1.x + app.player1.size > app.width: #Bounded Motion
        app.player1.x = app.width-app.player1.size
    elif app.player1.x < 0:
        app.player1.x = 0

def onStep(app):
    takeStep(app)

def takeStep(app):
    if app.player1.jump == True:
        app.player1.dy += 2
        app.player1.y += app.player1.dy
    if app.player1.y < app.ground - app.player1.size:
        app.player1.y += 10
    if app.player1.y >= app.ground - app.player1.size:
        app.player1.jump = False


runApp()