# Following Website and Packages are studied to construct Behavior Tree
# https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter06_The_Behavior_Tree_Starter_Kit.pdf
# https://py-trees.readthedocs.io/en/devel/
# https://en.wikipedia.org/wiki/Behavior_tree_(artificial_intelligence,_robotics_and_control)
# https://robohub.org/introduction-to-behavior-trees/
import BT_Behavior
import BT_Composite

def btAiPlayer(app):
    #Root
    root = BT_Composite.Selector('root')


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
            app.player2.shootChr()
        else:
            app.player2.direction = 'left'
            app.player2.shootChr()
        return 'Success'

    # def actualJump(app):
    #     if app.player2.jump == False:
    #         app.player2.jumpChr()
    #         return 'Success'
    #     else:
    #         return 'Failure'
        
    def sameHeight(app):
        if app.player1.y == app.player2.y:
            return 'Success'
        elif app.player2.jump:
            return 'Running'
        return 'Failure'
    
    def deterJump(app):
        if app.player1.y < app.player2.y:
            return 'Success'
        else:
            return 'Failure'
        

    
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
    deterJum = BT_Behavior.Condition(deterJump, 'deterJum', app)
    #Composite Node 1223
    jumpShootTime = BT_Composite.Sequence('jumpShootTime')
    #Node 12221
    sameHei = BT_Behavior.Condition(sameHeight, 'sameHei', app)
    #Node 12222 (Reptition just for better understanding)
    actualSho = BT_Behavior.Action(actualShoot, 'actualSho', app)

    plainShoot.add(shootRan)
    plainShoot.add(actualSho)

    jumpShoot.add(deterJum)

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
            app.player2.direction = 'left'
        app.player2.attackChr()
        return 'Success'

    def attackRange(app):
        if isHit(app.player1, app.player2):
            return 'Success'
        return 'Failure'

    def towardEnemy(app):
        if isHit(app.player1, app.player2):
            app.player2.dx = 0
            app.player2.walk = False
            return 'Success'
        else:
            if app.player1.x < app.player2.x:
                app.player2.dx = -5
                app.player2.walk = True
                app.player2.direction = 'left'
            elif app.player1.x > app.player2.x:
                app.player2.dx = 5
                app.player2.walk = True
                app.player2.direction = 'right'
            return 'Running'
    
    def humanPlaHigher(app):
        if app.player1.y < app.player2.y:
            return 'Success'
        return 'Failure'
    
    def finClosJumpPoi(app):
        if closetPoint(app) is not None and not app.player1.jump:
            app.closetJumpPoint = closetPoint(app)
        return 'Success'
    
    def closetPoint(app):
        smallestDis = 1000
        closetJumPoint = None
        for point in app.selectedField.jumpPoint:
            if point.y == app.player2.y:
                if abs(app.player1.x - point.x) < smallestDis:
                    closetJumPoint = point
                    smallestDis = abs(app.player1.x - point.x)
        return closetJumPoint
    
    def goClosJumpPoi(app):
        if app.closetJumpPoint is None:
            return 'Failure'
        if (app.closetJumpPoint.x - 2.5 < app.player2.x 
            < app.closetJumpPoint.x + 2.5):
            return 'Success'
        elif app.closetJumpPoint.x > app.player2.x:
            app.player2.dx = 5
            app.player2.direction = 'right'
            app.player2.walk = True
            return 'Running'
        elif app.closetJumpPoint.x < app.player2.x:
            app.player2.dx = -5
            app.player2.direction = 'left'
            app.player2.walk = True
            return 'Running'
            
    
    def jumpLevel(app):
        if not app.player2.jump:
            if app.closetJumpPoint.direction == 'right':
                app.player2.direction = 'right'
                app.player2.dx = 5
                app.player2.jumpChr()
                return "Running"
            elif app.closetJumpPoint.direction == 'left':
                app.player2.direction = 'left'
                app.player2.dx = -5
                app.player2.jumpChr()
                return "Running"
        else:
            return "Running"
        
        

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
    #Node 222
    moveAtt = BT_Composite.Selector('moveAtt')
    #Node 2221
    jumpPoint = BT_Composite.Sequence('jumpPoints')
    #Node 22211
    humanPlaHigh = BT_Behavior.Condition(humanPlaHigher, 'humanPlaHigh', app)
    #Node 22212
    finClosJumpPoint = BT_Behavior.Condition(finClosJumpPoi, 'finClosJumpPoint',
                                             app)
    #Node 22213
    goClosJumpPoint = BT_Behavior.Action(goClosJumpPoi, 'goClosJumpPoint',
                                         app)
    #Node 22214
    jumpLevelHi = BT_Behavior.Action(jumpLevel, 'jumpLevelHi', app)
    #Node 2222
    towardAtt = BT_Composite.Sequence('towardAtt')
    #Node 22221
    towardEne = BT_Behavior.Action(towardEnemy, 'towardEne', app)
    #Node 22222
    directAtt1 = BT_Composite.Sequence('direct1Att')
    #Node 222221
    attackRan1 = BT_Behavior.Condition(attackRange, 'attackRan1', app)
    #Node 222222
    actualAtt1 = BT_Behavior.Condition(actualAttack, 'actualAtt1', app)


    root.add(attackLogic)
    attackLogic.add(CDAtt)
    attackLogic.add(directMoveAtt)
    directMoveAtt.add(directAtt)
    directAtt.add(attackRan)
    directAtt.add(actualAtt)
    directMoveAtt.add(moveAtt)
    moveAtt.add(jumpPoint)
    moveAtt.add(towardAtt)
    jumpPoint.add(humanPlaHigh)
    jumpPoint.add(finClosJumpPoint)
    jumpPoint.add(goClosJumpPoint)
    jumpPoint.add(jumpLevelHi)
    towardAtt.add(towardEne)
    towardAtt.add(directAtt1)
    directAtt1.add(attackRan1)
    directAtt1.add(actualAtt1)

    def distance(x1, y1, x2, y2):
        return ((x1-x2)**2+(y1-y2)**2)**0.5
    
    return root


