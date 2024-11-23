class Behavior:
    def __init__(self, func, name):
        self.func = func
        self.name = name


class Condition(Behavior):
    def __init__(self, func, name):
        super().__init__(func, name)

    def __repr__(self):
        return f'Condition {self.name}'

    def tick(self):
        return self.func()


class Action(Behavior):
    def __init__(self, func, name):
        super().__init__(func, name)

    def __repr__(self):
        return f'Action {self.name}'

    def tick(self):
        self.func()