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