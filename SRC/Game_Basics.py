from cmu_graphics import *

def onAppStart(app):
    app.ground = 300
    app.player1x = app.width/4
    app.player1y = app.height/4
    app.jump = False

def redrawAll(app):
    drawRect(0, app.ground, app.width, app.height, fill = 'black')
    drawRect(app.player1x, app.player1y, 20, 20, fill = 'orange')

def onKeyPress(app):
    if app.jump = False:
        app.jump = True
        jumpPlay(app.player1y)

def jumpPlay(app, player):
    

def onKeyHold(app, keys):
    if 'left' in keys:
        app.player1x -= 5
    elif 'right' in keys:
        app.player1x += 5

def onStep(app):
    takeStep(app)

def takeStep(app):
    if app.player1y < 280:
        app.player1y += 10


runApp()