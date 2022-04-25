from dataclasses import dataclass
import json
import websockets
import enum
import json

class MemberRole(enum.Enum):
    CAPTAIN = "cap"
    MEDIC = "med"
    TECH = "tec"
    PILOT = "pil"
    IMP = "imp"


@dataclass
class State:
    config: dict
    socket: websockets

    name: str
    role: MemberRole
    group: str

    async def wssend(self, cmd, cmd_d=None):
        if cmd_d is None:
            cmd_d = {}

        await self.socket.send(
            json.dumps(
                {"session":"123456",
                 "cmd":cmd,
                 "cmd-d":cmd_d},
                default=vars
            )
        )

        return await self.socket.recv()
    