from BT_Behavior import *
from BT_Composite import *

a = [1]

def deterNum():
    if len(a) > 0:
        return True
    else:
        return False
    
def printNum():
    print(1)

    
newCon = Condition(deterNum, 'newCon')
newNum = Action(printNum, 'newAct')

newSelector = Selector('newSelector')
newSelector.add(newCon)
newSelector.add(newNum)
newSelector.tick()


