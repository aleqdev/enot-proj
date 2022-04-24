from ..state import State

class Stage:
    def __init__(self, state: State):
        self.state = state

    def display(self):
        pass

    def start(self):
        pass

    def exit(self):
        pass

    def next(self) -> Stage:
        pass
