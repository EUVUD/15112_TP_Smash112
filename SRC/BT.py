import BT_Behavior
import BT_Composite

def btAiPlayer(app):
    def jumpPlay(player):
        player.jump = True
        player.dy = -35
    def isHit(player1, player2):
        if (distance(player1.x+player1.sizeX/2, player1.y+player1.sizeY/2,
                    player2.x+player2.sizeX/2, player2.y+player2.sizeY/2)
                    < 40):
            return True
        else:
            return False

    def shootCD(app):
        if app.player2.shuriCD == 0:
            return 'Success'
        return 'Failure'

    def shootRange(app):
        if app.player1.y == app.player2.y:
            return 'Success'
        return 'Failure'

    def actualShoot(app):
        if app.player1.x > app.player2.x:
            app.player2.direction = 'right'
            app.player2.shoot()
            app.player2.shuriCD = 15
        else:
            app.player2.direction = 'left'
            app.player2.shoot()
            app.player2.shuriCD = 15
        return 'Success'

    def actualJump(app):
        if app.player2.jump == False:
            jumpPlay(app.player2)
            return 'Success'
        else:
            return 'Failure'
        
    def sameHeight(app):
        if app.player1.y == app.player2.y:
            return 'Success'
        elif app.player2.jump:
            return 'Running'
        return 'Failure'
        

    #Root
    root = BT_Composite.Selector('root')
    #Composite Node 1
    shootLogic = BT_Composite.Sequence('shootLogic')
    #Node 11
    shoCD = BT_Behavior.Condition(shootCD, 'shoCD', app)
    #Composite Node 12
    jumShoDeter = BT_Composite.Selector('jumShoDeter')
    #Composite Node 121
    plainShoot = BT_Composite.Sequence('plainShoot')
    #Node 1211
    shootRan = BT_Behavior.Condition(shootRange, 'chootRan', app)
    #Node 1212
    actualSho = BT_Behavior.Action(actualShoot, 'actualSho', app)
    #Composite Node 122
    jumpShoot = BT_Composite.Sequence('jumpShoot')
    #Node 1221
    actualJum = BT_Behavior.Action(actualJump, 'actualJum', app)
    #Composite Node 1222
    jumpShootTime = BT_Composite.Sequence('jumpShootTime')
    #Node 12221
    sameHei = BT_Behavior.Condition(sameHeight, 'sameHei', app)
    #Node 12222 (Reptition just for better understanding)
    actualSho = BT_Behavior.Action(actualShoot, 'actualSho', app)

    plainShoot.add(shootRan)
    plainShoot.add(actualSho)

    jumpShoot.add(actualJum)

    jumpShootTime.add(sameHei)
    jumpShootTime.add(actualSho)

    jumpShoot.add(jumpShootTime)

    jumShoDeter.add(plainShoot)
    jumShoDeter.add(jumpShoot)

    shootLogic.add(shoCD)
    shootLogic.add(jumShoDeter)

    root.add(shootLogic)

    def deterAttack(app):
        if app.player2.attackCD == 0:
            return 'Success'
        return 'Failure'

    def actualAttack(app):
        if app.player1.x > app.player2.x:
            app.player2.direction = 'right'
        else:
            app.player2.direction = 'right'
        app.player2.attack = True
        app.player2.attackCD = 15
        if isHit(app.player1, app.player2) and app.player2.attack:
            app.player1.health -= 1
        return 'Success'

    def attackRange(app):
        if isHit(app.player1, app.player2):
            return 'Success'
        return 'Failure'

    def towardEnemy(app):
        if isHit(app.player1, app.player2):
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

    #Node 2
    attackLogic = BT_Composite.Sequence('attackLogic')
    #Node 21
    CDAtt = BT_Behavior.Condition(deterAttack, 'CDAtt', app)
    #Node 22
    directMoveAtt = BT_Composite.Selector('directMoveAtt')
    #Node 221
    directAtt = BT_Composite.Sequence('directAtt')
    #Node 2211
    attackRan = BT_Behavior.Condition(attackRange, 'attackRan', app)
    #Node 2212
    actualAtt = BT_Behavior.Condition(actualAttack, 'actualAtt', app)
    #Node222
    moveAtt = BT_Composite.Sequence('moveAtt')
    #Node 2221
    towardEne = BT_Behavior.Action(towardEnemy, 'towardEne', app)
    #Node 2222
    directAtt1 = BT_Composite.Sequence('direct1Att')
    #Node 22221
    attackRan1 = BT_Behavior.Condition(attackRange, 'attackRan1', app)
    #Node 22222
    actualAtt1 = BT_Behavior.Condition(actualAttack, 'actualAtt1', app)


    root.add(attackLogic)
    attackLogic.add(CDAtt)
    attackLogic.add(directMoveAtt)
    directMoveAtt.add(directAtt)
    directAtt.add(attackRan)
    directAtt.add(actualAtt)
    directMoveAtt.add(moveAtt)
    moveAtt.add(towardEne)
    moveAtt.add(directAtt1)
    directAtt1.add(attackRan1)
    directAtt1.add(actualAtt1)

    def distance(x1, y1, x2, y2):
        return ((x1-x2)**2+(y1-y2)**2)**0.5
    
    return root


