# Following Website and Packages are studied to construct Behavior Tree
# https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter06_The_Behavior_Tree_Starter_Kit.pdf
# https://py-trees.readthedocs.io/en/devel/
# https://en.wikipedia.org/wiki/Behavior_tree_(artificial_intelligence,_robotics_and_control)
# https://robohub.org/introduction-to-behavior-trees/

class Behavior:
    def __init__(self, func, name, app):
        self.func = func
        self.name = name
        self.app = app


class Condition(Behavior):
    def __init__(self, func, name, app):
        super().__init__(func, name, app)

    def __repr__(self):
        return f'Condition {self.name}'

    def tick(self):
        return self.func(self.app)


class Action(Behavior):
    def __init__(self, func, name, app):
        super().__init__(func, name, app)

    def __repr__(self):
        return f'Action {self.name}'

    def tick(self):
        return self.func(self.app)