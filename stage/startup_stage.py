from state import State
import websockets
import config
import colorama
import json
from . import abstract_stage

class StartupStage(abstract_stage.Stage):
    @staticmethod
    async def new(config):
        return StartupStage(State(
            config=config,
            socket=None,
            name=None,
            role=None,
            group=None
        ))

    async def start(self):
        await super().start()
        print("Соединение...")
        self.state.socket = await websockets.connect(self.state.config.API_SOCKET_PATH)
        print("\033[FСоединение установлено")
        
    async def display(self):
        name = input("Введите своё имя :: ")
        self.state.name = name
        print(f"\033[F\033[KВведённое имя: {colorama.Fore.GREEN}{name}{colorama.Style.RESET_ALL}")

        print(f"""Доступные роли:""")
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

        self.state.role = role
        print(f"\033[F\033[KВаша роль: {colorama.Fore.GREEN}{config.ROLES_NAMES[role]}{colorama.Style.RESET_ALL}")

        groups = json.loads(await self.state.wssend("get-groups"))
        print("Существующие команды:")
        for i, name in enumerate(x["name"] for x in groups):
            print(f" {i}) {name}")
        while True:
            group = input("Введите номер вашей команды :: ")
            try:
                group = int(group)
                if group >= 0 and group < len(groups):
                    break
            finally:
                print("Введите число от 0 до", len(groups))

        gname = groups[i]["name"]
        self.state.group = gname
        print(f"\033[F\033[KВаша команда: {colorama.Fore.GREEN}{gname}{colorama.Style.RESET_ALL}")

        await self.state.wssend("create-member", {
            "name": self.state.name,
            "role": self.state.role,
            "group": self.state.group
        })

        print(json.loads(await self.state.wssend("get-groups")))






