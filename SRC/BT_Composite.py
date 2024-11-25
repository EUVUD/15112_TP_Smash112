# Following Website and Packages are studied to construct Behavior Tree
# https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter06_The_Behavior_Tree_Starter_Kit.pdf
# https://py-trees.readthedocs.io/en/devel/
# https://en.wikipedia.org/wiki/Behavior_tree_(artificial_intelligence,_robotics_and_control)
# https://robohub.org/introduction-to-behavior-trees/

from BT_Behavior import *

class Composite:
    def __init__(self, name):
        self.children = []
        self.name = name

    def __repr__(self):
        return f'{self.children}'
    
    def add(self, other):
        if isinstance(other, Behavior) or isinstance(other, Composite):
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
        for child in self.children:
            childStatus = child.tick()
            if childStatus == 'Failure':
                return 'Failure'
            elif childStatus == 'Running':
                return 'Running'
        return 'Success'