from state import State
import websockets
import config
import colorama
import curses.textpad
from . import abstract_stage

class StartupStage(abstract_stage.Stage):
    @staticmethod
    async def new(config):
        return StartupStage(State(
            config=config,
            socket=None,
            scr=None,
            name="",
            role=None
        ))

    async def start(self):
        await super().start()
        print("Соединение...")
        self.state.socket = await websockets.connect(self.state.config.API_SOCKET_PATH)
        print("Соединение установлено")
        
    async def display(self):
        name = input("Введите своё имя :: ")
        print(f"\rВведённое имя: {colorama.Fore.GREEN}{name}{colorama.Style.RESET_ALL}")

        print(f"""
Доступные роли:""")
        print(''.join(f'\n {i}) {name}' for i, name in enumerate(config.ROLES_NAMES)))

        role = None
        while True:
            role = input("Выберите свою роль :: ")
            try:
                role = int(role)
                if role >= 0 and role <= 4:
                    break
            finally:
                print("Введите число от 0 до 4")

        print(f"\Ваша роль: {colorama.Fore.GREEN}{config.ROLES_NAMES[role]}{colorama.Style.RESET_ALL}")

        name = input("Введите своё имя :: ")
        print(f"\rВведённое имя: {colorama.Fore.GREEN}{name}{colorama.Style.RESET_ALL}")




