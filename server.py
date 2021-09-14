import asyncio

import websockets
from websockets.legacy.server import WebSocketServerProtocol

WS_HOST = 'localhost'
WS_PORT = 8765
WS_URL = f'ws://{WS_HOST}:{WS_PORT}'


class Server:
    clients = set()

    async def handler(self, ws: WebSocketServerProtocol, uri: str) -> None:
        await self.register(ws)
        try:
            await self.distribute(ws)
        finally:
            await self.unregister(ws)

    async def register(self, ws: WebSocketServerProtocol) -> None:
        self.clients.add(ws)

    async def unregister(self, ws: WebSocketServerProtocol) -> None:
        self.clients.remove(ws)

    async def distribute(self, ws: WebSocketServerProtocol) -> None:
        async for message in ws:
            await self.send_to_clients(message)

    async def send_to_clients(self, message: str) -> None:
        if self.clients:
            await asyncio.wait([
                asyncio.create_task(client.send(message))
                for client in self.clients
            ])


async def run_server():
    async with websockets.serve(Server().handler, WS_HOST, WS_PORT):
        await asyncio.Future()  # run forever


if __name__ == '__main__':
    asyncio.run(run_server())
