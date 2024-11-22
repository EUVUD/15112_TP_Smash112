from BT_Behavior import *

class Composite:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def add(self, other):
        if isinstance(other, Behavior):
            self.children.append(other)
    

class Selector(Composite):
    def __init__(self, name):
        super().__init__(name)

    def tick(self):
        for child in self.children:
            child.tick()


class Sequence(Composite):
    def __init__(self, name):
        super().__init__(name)
    
    def tick(self):
        if self.children == []:
            raise Exception("Empty Selector")
        for child in self.children:
            if child.tick() == None:
                pass
            else:
                if child.tick() == True:
                    continue
                else:
                    break