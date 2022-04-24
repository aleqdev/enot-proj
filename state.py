from dataclasses import dataclass
import websockets
import curses
import enum

class MemberRole(enum.Enum):
    CAPTAIN = 0
    MEDIC = 1
    TECH = 2
    PILOT = 3
    IMP = 4


@dataclass
class State:
    config: dict
    socket: websockets
    scr: curses.window

    name: str
    role: MemberRole
    