import asyncio

import websockets
from websockets.legacy.server import WebSocketServerProtocol

WS_HOST = 'localhost'
WS_PORT = 8765
WS_URL = f'ws://{WS_HOST}:{WS_PORT}'


class Server:
    clients = set()

    async def handler(self, ws: WebSocketServerProtocol, uri: str) -> None:
        self.clients.add(ws)
        try:
            await self.distribute(ws)
        finally:
            self.clients.remove(ws)

    async def distribute(self, ws: WebSocketServerProtocol) -> None:
        async for message in ws:
            websockets.broadcast(self.clients, message)


async def run_server():
    async with websockets.serve(Server().handler, WS_HOST, WS_PORT):
        await asyncio.Future()  # run forever


if __name__ == '__main__':
    asyncio.run(run_server())
