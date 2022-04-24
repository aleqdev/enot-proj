from dataclasses import dataclass
import websockets


@dataclass
class State:
    socket: websockets.Websocket