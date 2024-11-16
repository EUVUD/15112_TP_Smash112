from BT_Behavior import behavior

class composite:
    def __init__(self, childList):
        if isinstance(childList, list):
            self.children = list
            
        or isinstance(childList, composite)
            or isinstance(childList, behavior)):
            

    def addChild(self, child):
        if isinstance(child, behavior) or isinstance(child, composite):
            self.children.append(child)

class selector(composite):
    def __init__(self):
        super().__init__()

    def execute(self):
        for child in self.children:
            child.run()



class sequence: