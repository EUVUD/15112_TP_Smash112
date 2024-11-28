def deterGameOver(app):
    if app.player1.health == 0 or app.player2.health == 0:
        app.gameOver = True


def attackCD(app):
    if app.player1.attackCD > 0:
        app.player1.attackCD -= 1
    if app.player2.attackCD > 0:
        app.player2.attackCD -= 1
        
def shuriKenCD(app):
    if app.player1.shuriCD > 0:
        app.player1.shuriCD -= 1
    if app.player2.shuriCD > 0:
        app.player2.shuriCD -= 1
            
def spriteInd(app):
    if app.counter % 2 == 0:
            #Player1 Sprite
            app.player1StandInd = (app.player1StandInd + 1) % len(app.player1.rStandSprite)
            app.player1WalkInd = (app.player1WalkInd + 1) % len(app.player1.rWalkSprite)
            if app.player1.attack:
                if app.player1AttackInd == len(app.player1.rAttackSprite)-1:
                    app.player1.attack = False
                    app.player1.attackCD = 15
                    app.player1.attackComb = 1
                    app.player1AttackInd = 0
                app.player1AttackInd += 1

            #Player2 Sprite
            app.player2StandInd = (app.player2StandInd + 1) % len(app.player2.rStandSprite)
            app.player2WalkInd = (app.player2WalkInd + 1) % len(app.player2.rWalkSprite)
            if app.player2.attack:
                if app.player2AttackInd == len(app.player2.rAttackSprite)-1:
                    app.player2.attack = False
                    app.player2.attackCD = 15
                    app.player2AttackInd = 0
                app.player2AttackInd += 1

            #Shuriken Sprite
            app.bulletRightInd = (app.bulletRightInd + 1) % len(app.rShuriSprite)
            app.bulletLeftInd = (app.bulletLeftInd + 1) % len(app.lShuriSprite)


#Gravity Simulation

def gravSimul(app):
    # Player 1 Sim
    if app.player1.jump == True:
        app.player1.dy += 2
        app.player1.y += app.player1.dy
    # In the air, the player keeps falling
    if app.player1.y < app.ground - app.player1.sizeY/2:
        app.player1.y += 10
    else: # Stay on ground
        app.player1.y = app.ground - app.player1.sizeY/2
    if app.player1.y >= app.ground - app.player1.sizeY/2:
        app.player1.jump = False

    # Player 2 Sim
    if app.player2.jump == True:
        app.player2.dy += 2
        app.player2.y += app.player2.dy
    # In the air, the player keeps falling
    if app.player2.y < app.ground - app.player2.sizeY/2:
        app.player2.y += 10
    else: # Stay on ground
        app.player2.y = app.ground - app.player2.sizeY/2
    if app.player2.y >= app.ground - app.player2.sizeY/2:
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
                     app.player1.x, app.player1.y)
            < app.projection[i].sizeX/2 + app.player1.sizeX/2):
            app.player1.health -= 1
            if app.player1.health == 1:
                app.projection[i].velocity = 0
            else:
                app.projection.pop(i)
        elif (distance(app.projection[i].x, app.projection[i].y, 
                       app.player2.x, app.player2.y)
            < app.projection[i].sizeX/2 + app.player2.sizeX/2):
            app.player2.health -= 1
            if app.player2.health == 1:
                app.projection[i].velocity = 0
            else:
                app.projection.pop(i)
        i += 1

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5