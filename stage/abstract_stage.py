from __future__ import annotations

class Stage:
    def __init__(self, state):
        self.state = state
        self.running = False

    async def display(self):
        pass

    async def start(self):
        self.running = True

    async def exit(self):
        self.running = False

    async def next(self) -> Stage:
        pass
