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
            childStatus = child.tick()
            if childStatus == 'Success':
                return 'Success'
            elif childStatus == 'Running':
                return 'Running'
        return 'Failure'


class Sequence(Composite):
    def __init__(self, name):
        super().__init__(name)
    
    def tick(self):
        if self.children == []:
            raise Exception("Empty Selector")
        for child in self.children:
            childStatus = child.tick()
            if childStatus == 'Failure':
                return 'Failure'
            elif childStatus == 'Running':
                return 'Running'
        return 'Success'